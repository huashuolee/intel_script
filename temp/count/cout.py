"""
f = open('file','r')
f.read()
for line in f.read():
    print line 
"""
with open('file','r') as f:
    for line in f:
        print line
