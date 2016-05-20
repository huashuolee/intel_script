import multiprocessing as mul
import os

def download(url):
    os.system('wget '+url)


dlist = ['www.163.com','www.qq.com','www.ifeng.com','www.baidu.com','www.sina.com.cn']

pool = mul.Pool(3)
pool.map(download,dlist)
