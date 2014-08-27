import subprocess

check_adb=subprocess.Popen('adb devices',shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)

