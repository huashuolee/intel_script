from conf import list_dir

def list1(cmd='ls'):
    
    print list_dir.result(cmd)[0]    
    
if __name__=='__main__':
    list1()
    
  
