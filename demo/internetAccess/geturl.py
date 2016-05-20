import urllib2

f=open('a.html','aw')
for line in urllib2.urlopen(raw_input('input the url')):
    f.write(line)
f.close
