import os,subprocess,threading,sys
from multiprocessing import Process,Pool


def download(item):
    fdname = sys.argv[1].split("/")[-2]
    date = sys.argv[1].split("/")[-4]
    dest = '~/work/build/' + date + '_' + fdname + '/' 
    url = sys.argv[1] + item
    cmd = 'wget --no-check-certificate --no-proxy ' + url + ' -P ' + dest
    os.system(cmd) 


downlist = ['boot.fls', 'cache.fls', 'mobilevisor.fls', 'modem.fls', 'mvconfig.fls', 'mvconfig_smp.fls', 'psi_flash.fls', 'recovery.fls', 'secvm.fls', 'slb.fls', 'splash_img.fls', 'system.fls', 'ucode_patch.fls', 'userdata.fls', 'elf.zip'] 

Pool(5).map(download,downlist)
#pool = Pool(5)
#pool.map(function,list)
