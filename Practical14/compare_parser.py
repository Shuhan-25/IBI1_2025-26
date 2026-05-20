#compare_parser.py
import datetime
from dom_parser import parse_go_with_dom
from sax_parser import parse_go_with_sax

def main():
    
    xml_file = 'go_obo.xml'
    

    #run DOM parser
    dom_time, dom_results = parse_go_with_dom(xml_file)
    
    #run SAX parser
    sax_time, sax_results = parse_go_with_sax(xml_file)
    
    #performance comparison
    print("Performance Comparison:")
    print(f"DOM API execution time: {dom_time:.4f} seconds")
    print(f"SAX API execution time: {sax_time:.4f} seconds")
    
    #determine which API ran faster
    #SAX API generally runs faster
    if dom_time < sax_time:
        print(f"\nDOM API was faster by {sax_time - dom_time:.4f} seconds")
        fastest = "DOM"
    else:
        print(f"\nSAX API was faster by {dom_time - sax_time:.4f} seconds")
        fastest = "SAX"
    
    print(f"\nFastest API: {fastest}")
    
    #verify both parsers return identical results
    print("Result Verification:")
    if dom_results == sax_results:
        print("DOM and SAX returned identical results")
    else:
        print("DOM and SAX returned different results")
        print("DOM results:", dom_results)
        print("SAX results:", sax_results)

if __name__ == "__main__":
    main()