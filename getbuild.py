import os,subprocess,threading,sys

def read_xml():
    tree = ET.parse('~/work/sofia/build/index.xml')
    root = tree.getroot()


def download():
    fdname = sys.argv[1].split("/")[-2]
    date = sys.argv[1].split("/")[-4]
    dest = '~/work/build/' + date + '_' + fdname + '/' 
    cmd = 'wget --no-check-certificate --no-proxy ' + url + ' -P ' + dest
    os.system(cmd) 


downlist = ['boot.fls', 'cache.fls', 'mobilevisor.fls', 'modem.fls', 'mvconfig.fls', 'mvconfig_smp.fls', 'psi_flash.fls', 'recovery.fls', 'secvm.fls', 'slb.fls', 'splash_img.fls', 'system.fls', 'ucode_patch.fls', 'userdata.fls', 'elf.zip'] 

if __name__ == "__main__":
    for item in downlist:
        url = sys.argv[1] + item
        it = threading.Thread(target= download)
        it.start()
        it.join()
