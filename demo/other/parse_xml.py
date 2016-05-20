from xml.etree import ElementTree

def print_node(node):
    print "====================================="
    for key,value in node.items():
      print "%s:%s" % (key, value)   
      print "????"
    for subnode in node.getchildren():
      print "%s:%s" % (subnode.tag, subnode.text)   

def read_xml(text = '', xmlfile = ''):
    #root = ElementTree.parse(xmlfile)
    root = ElementTree.fromstring(text)
    
    # 1 getiterator([tag=None]) 
    # only elements whose tag equals tag are returned from the iterator
    eitor = root.getiterator("employee")
    for e in eitor:
        print_node(e)
    
    

if __name__ == '__main__':
    read_xml(open("employees.xml").read())
