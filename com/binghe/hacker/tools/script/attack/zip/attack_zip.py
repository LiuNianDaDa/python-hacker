#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf-8 -*-
# Date: 2019/2/11
# Created by ����
# Description �����ƽ�Zip�ļ�
#             �÷��� python attack_zip.py -f <zipFile> -d <dictionary>
# ���� https://blog.csdn.net/l1028386804

import zipfile
import optparse
from threading import Thread

#��ѹzip�ļ�
def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Found Password ' + password + '\n'
    except Exception, e:
        pass


#������
def main():
    parser = optparse.OptionParser("usage%prog -f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='sepcify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)

    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
#�������
if __name__ == "__main__":
    main()