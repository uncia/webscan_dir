# webscan_dir
## *****************************************************
## 
##            轻量级web目录扫描器 - webscan_dir.py
##            作者：by_wm
##            邮箱：by_wm@qq.com
##            blog：www.0day.pub
## 
## *****************************************************

## python 渣渣写的，轻喷。

Example:webscan_dir.py -u http://192.168.1.1/ -t 50 -f php,dir -n 403 \n \
-u     Example:-u http://baidu.com/  This is required \n \
-t     Example:-t 40   default -t 50 \n \
-f     Example:-t php,dir    php|dir|asp|aspx|mdb|jsp optional This is required \n \
-n     Example:-n 403,301   You don't want the tools to detect the status code default 503|404|400 \n \
-h     help

## 2017年11月28日
## 更新带端口的时候无法保存成文件的bug。
## 增加返回页面内容长度统计，方便查看。
##  因为test404那个扫描工具需要强制联网更新，看着不爽就随便用python写写自己用的，不好用请换其它工具，看心情优化更新
## -t 可自定义线程 默认线程50
## -u 指定url 
## -f 指定扫描类型php|dir|asp|aspx|mdb|jsp  可根据目录下的*.txt 自行增加字典
## -n 指定过滤状态码  默认过滤 503|404|400
## 程序默认随机ua.txt 里面的user agent 可根据需求自定义增加
##### github地址：https://github.com/0daysec/webscan_dir