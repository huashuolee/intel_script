try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='watch_video.xml')
root =tree.getroot()
for elem in root.iter('pass_count'):
    print 'PASS:', elem.text
for elem in tree.iter(tag='TBD__count'):
    print 'TBD:', elem.text
for elem in tree.iter(tag='fail_count'):
    print 'FAIL:', elem.text
#for elem in tree.iter():
#    print elem
#for elem in root.iter():
#    print elem
