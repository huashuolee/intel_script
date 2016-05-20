import os,subprocess,threading,sys
from multiprocessing import Process


def download(url):
    fdname = sys.argv[1].split("/")[-2]
    date = sys.argv[1].split("/")[-4]
    dest = '~/work/build/' + date + '_' + fdname + '/' 
    cmd = 'wget --no-check-certificate --no-proxy ' + url + ' -P ' + dest
    os.system(cmd) 


downlist = ['boot.fls', 'cache.fls', 'mobilevisor.fls', 'modem.fls', 'mvconfig.fls', 'mvconfig_smp.fls', 'psi_flash.fls', 'recovery.fls', 'secvm.fls', 'slb.fls', 'splash_img.fls', 'system.fls', 'ucode_patch.fls', 'userdata.fls', 'elf.zip'] 

if __name__ == "__main__":
    for item in downlist:
        url = sys.argv[1] + item
        it = Process(target= download,args=(url,))
        it.start()
        it.join()
