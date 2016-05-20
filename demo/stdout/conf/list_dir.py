import subprocess

def result(cmd):
    p=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    stdout,stderror = p.communicate()
   # print stdout
    return stdout,stderror


#print result(raw_input('---->'))[0]   
