#dom_parser.py
import xml.dom.minidom
import datetime

def parse_go_with_dom(xml_file):
    
    #record start time
    start_time = datetime.datetime.now()
    
    #parse the XML file
    dom_tree = xml.dom.minidom.parse(xml_file)
    
    #get all term elements
    terms = dom_tree.getElementsByTagName('term')
    
    #initialize counters for each ontology
    #ontology types: molecular_function, biological_process, cellular_component
    max_counts = {
        'molecular_function': {'id': '', 'count': 0},
        'biological_process': {'id': '', 'count': 0},
        'cellular_component': {'id': '', 'count': 0}
    }
    
    #iterate through each term
    for term in terms:
        #get GO ID
        id_elements = term.getElementsByTagName('id')
        if id_elements and id_elements[0].firstChild:
            go_id = id_elements[0].firstChild.data
        else:
            continue
        
        #get namespace (ontology type)
        namespace_elements = term.getElementsByTagName('namespace')
        if namespace_elements and namespace_elements[0].firstChild:
            namespace = namespace_elements[0].firstChild.data
        else:
            continue
        
        #count is_a elements
        is_a_elements = term.getElementsByTagName('is_a')
        is_a_count = len(is_a_elements)
        
        #update max count for this ontology
        if namespace in max_counts:
            if is_a_count > max_counts[namespace]['count']:
                max_counts[namespace]['count'] = is_a_count
                max_counts[namespace]['id'] = go_id
    
    #record end time
    end_time = datetime.datetime.now()
    elapsed_time = (end_time - start_time).total_seconds()
    
    #print results
    print("DOM API Results:")
    print("Molecular Function:")
    print(f"  GO Term: {max_counts['molecular_function']['id']}")
    print(f"  Number of is_a elements: {max_counts['molecular_function']['count']}")
    print("\nBiological Process:")
    print(f"  GO Term: {max_counts['biological_process']['id']}")
    print(f"  Number of is_a elements: {max_counts['biological_process']['count']}")
    print("\nCellular Component:")
    print(f"  GO Term: {max_counts['cellular_component']['id']}")
    print(f"  Number of is_a elements: {max_counts['cellular_component']['count']}")
    print(f"\nExecution time: {elapsed_time:.4f} seconds")
    
    return elapsed_time, max_counts

if __name__ == "__main__":
    parse_go_with_dom('go_obo.xml')