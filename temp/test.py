from xml.etree import ElementTree

tree = ElementTree.parse('employees.xml')
root = tree.getroot()
print root.tag,root.text,root.attrib

for i in root:
    print i.tag,i.text,i.attrib

employee =  root.findall("employee")
for i1 in employee:
    print i1.find('name').text
    print i1.get('age')
