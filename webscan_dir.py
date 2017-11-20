#!/usr/bin/env python2
# -*- coding=utf-8 -*-
import sys 
import os 
import time
import requests
import threadpool
import urllib
import random
import getopt
import urlparse
import string
from urlparse import *

def savehtml():
    parsed_uri = urlparse(argv_url)
    domain = '{uri.netloc}'.format(uri=parsed_uri)
    f = open(domain+".html",'w')
    f.write(''.join(save_urllist))
    f.close()
    print 'The html save in the '+os.path.split(os.path.realpath(__file__))[0]+'\\'+domain+'.html'


def http_(url_):
    User_Agent=random_ua()
    headers = {'Referer': 'http://baidu.com','User-Agent': User_Agent,}
    url_=urllib.quote(url_, safe=string.printable)
    try:
        htmlcode = requests.get(url=url_.decode('utf-8'),headers=headers,allow_redirects=False,timeout=10).status_code
        
        if(str(htmlcode) not in notcode_list):
            print url_+'\t'+str(htmlcode).decode('utf-8')
            save_urllist.append('<a href='+url_+'>'+url_+'<a>&nbsp;&nbsp;&nbsp;&nbsp;'+str(htmlcode)+'<br>')
    except :
        pass


def random_ua():
    ua=random.sample(ualist, 1)
    return ua[0]

def main():
    geturl=argv_url
    url_list=[]
    for file_ in file_list:
        file = open("dir/%s.txt" % file_)
        for  line in  file.readlines():
            url_list.append(geturl+line.strip('\n'))
    print len(url_list)
    task_pool=threadpool.ThreadPool(argv_Thread_num)
    #
    requests = threadpool.makeRequests(http_, url_list)

    for req  in requests:
        task_pool.putRequest(req)
    #
    task_pool.wait()




if __name__=="__main__":
    # 版权区域

    mycopyright = '''
*****************************************************

            轻量级web目录扫描器 - webscan_dir.py
            作者：by_wm
            邮箱：by_wm@qq.com
            blog：www.0day.pub

*****************************************************
'''
    print mycopyright.decode('utf-8')
    argv=sys.argv[1:]
    if(len(argv)==0):
        print("Example:webscan_dir.py -u http://192.168.1.1/ -t 50 -f php,dir -n 403 \n \
-u     Example:-u http://baidu.com/  This is required \n \
-t     Example:-t 40   default -t 50 \n \
-f     Example:-t php,dir    php|dir|asp|aspx|mdb|jsp optional This is required \n \
-n     Example:-n 403,301   You don't want the tools to detect the status code default 503|404|400 \n \
-h     help")
        exit()
    try:
        
        options, args = getopt.getopt(argv, "ht:u:f:n:")
    except getopt.GetoptError:
        print("Example:webscan_dir.py -u http://192.168.1.1/ -t 50 -f php,dir -n 403 \n \
-u     Example:-u http://baidu.com/  This is required \n \
-t     Example:-t 40   default -t 50 \n \
-f     Example:-t php,dir    php|dir|asp|aspx|mdb|jsp optional This is required \n \
-n     Example:-n 403,301   You don't want the tools to detect the status code default 503|404|400 \n \
-h     help")
        sys.exit()
    argv_Thread_num=50
    notcode_list=['503','404','400']
    save_urllist=[]
    for option, value in options:
        if option in ("-h"):
            print("Example:webscan_dir.py -u http://192.168.1.1/ -t 50 -f php,dir -n 403 \n \
-u     Example:-u http://baidu.com/  This is required \n \
-t     Example:-t 40   default -t 50 \n \
-f     Example:-t php,dir    php|dir|asp|aspx|mdb|jsp optional This is required \n \
-n     Example:-n 403,301   You don't want the tools to detect the status code default 503|404|400 \n \
-h     help")
            exit()
        if option in ("-u"):
            argv_url=format(value) #获取url
        if option in ("-t"):
            argv_Thread_num=int(value) #获取线程数量 默认50
        if option in ("-f"):
            # 
            file_list=list(set(format(value).lower().split(',')))
        if option in ("-n"):
            # 
            notcode_list+=list(set(format(value).lower().split(',')))
    print("url is: "+argv_url)
    print("Thread num is: "+str(argv_Thread_num))
    print("Scan type: "+','.join(file_list))
    print("Not detected code: "+','.join(notcode_list))
    arg=format(args)
    if(arg!='[]'):
        print("error args: "+arg)
        exit()
    file = open("dir/ua.txt")
    ualist=[line.strip('\n') for  line in  file.readlines()]
    main()
    savehtml()
    print 'scan over'