#sax_parser.py
import xml.sax
import datetime

class GOTermHandler(xml.sax.ContentHandler):
    
    def __init__(self):
        super().__init__()
        self.current_tag = ""
        self.current_go_id = ""
        self.current_namespace = ""
        self.current_is_a_count = 0
        self.in_term = False
        
        #store max counts for each ontology
        self.max_counts = {
            'molecular_function': {'id': '', 'count': 0},
            'biological_process': {'id': '', 'count': 0},
            'cellular_component': {'id': '', 'count': 0}
        }
        
        #buffer for accumulating text content
        self.content_buffer = ""
    
    def startElement(self, tag, attributes):
        self.current_tag = tag
        
        if tag == 'term':
            #start of a new term, reset temporary variables
            self.in_term = True
            self.current_go_id = ""
            self.current_namespace = ""
            self.current_is_a_count = 0
            self.content_buffer = ""
        elif tag == 'is_a' and self.in_term:
            #increment is_a counter when we see an is_a element
            self.current_is_a_count += 1
    
    def endElement(self, tag):
        if tag == 'term':
            #term finished, update max counts if this term has more is_a elements
            if self.current_namespace in self.max_counts:
                if self.current_is_a_count > self.max_counts[self.current_namespace]['count']:
                    self.max_counts[self.current_namespace]['count'] = self.current_is_a_count
                    self.max_counts[self.current_namespace]['id'] = self.current_go_id
            self.in_term = False
        
        elif tag == 'id' and self.in_term:
            self.current_go_id = self.content_buffer.strip()
        
        elif tag == 'namespace' and self.in_term:
            self.current_namespace = self.content_buffer.strip()
        
        #reset content buffer
        self.content_buffer = ""
        self.current_tag = ""
    
    def characters(self, content):
        # Accumulate text content (handles multi-part text)
        self.content_buffer += content

def parse_go_with_sax(xml_file):
    #record start time
    start_time = datetime.datetime.now()
    
    #create SAX parser and handler
    parser = xml.sax.make_parser()
    handler = GOTermHandler()
    parser.setContentHandler(handler)
    
    #parse the file
    parser.parse(xml_file)
    
    #record end time
    end_time = datetime.datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()
    
    #print results
    print("SAX API Results:")
    print("Molecular Function:")
    print(f"  GO Term: {handler.max_counts['molecular_function']['id']}")
    print(f"  Number of is_a elements: {handler.max_counts['molecular_function']['count']}")
    print("\nBiological Process:")
    print(f"  GO Term: {handler.max_counts['biological_process']['id']}")
    print(f"  Number of is_a elements: {handler.max_counts['biological_process']['count']}")
    print("\nCellular Component:")
    print(f"  GO Term: {handler.max_counts['cellular_component']['id']}")
    print(f"  Number of is_a elements: {handler.max_counts['cellular_component']['count']}")
    print(f"\nExecution time: {elapsed_time:.4f} seconds")
    
    return elapsed_time, handler.max_counts

if __name__ == "__main__":
    parse_go_with_sax('go_obo.xml')