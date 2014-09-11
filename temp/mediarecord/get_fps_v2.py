import subprocess

def getmediainfo(item,n):
    mediainfo = subprocess.Popen(['mediainfo ' +item], shell=True, stdout=subprocess.PIPE)
    stdmediainfo, stderr = mediainfo.communicate()
    #print stdmediainfo
    #print stdmediainfo.split('\n')
    f=open('mediainfo.log','aw')
    properties= stdmediainfo.split('\n')
    f.write(item+'\n')
    f.write(stdmediainfo)
    f.close()
     
    f=open('mediainfo.log','r')
    f1=open('fps.log','aw')
    for elem in properties:
       # f1.write('---------\n')
        if 'Frame rate' in elem and 'Frame rate mode' not in elem:
            f1.write(str(n)+'\n'+item+'\n')
            f1.write(elem+'\n')
    f.close()
    f1.close()




p=subprocess.Popen('ls',shell=True,stdout=subprocess.PIPE)
stdlist, stderr = p.communicate()
file_list=stdlist.split('\n')
f2=open('file.log','aw')
f=open('mediainfo.log','aw')
n=1
for item in file_list:
    f2.write(item+'\n')
    if 'aaceld' in item: 
        f.write(item+'\n')
        continue  
        
    elif item[-3:]=='mp4' or item[-3:]=='3gp':
        getmediainfo(item,n)
    n +=1
f2.close()
f.close()
