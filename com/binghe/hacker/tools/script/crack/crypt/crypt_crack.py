#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf-8 -*-
# Date: 2019/2/11
# Created by ����
# Description �����ֵ��ƽ�Unix/Linux���������ʾ��������Ҫ�ƽ�������ļ����ֵ��ļ�����
# ���� https://blog.csdn.net/l1028386804

import crypt

#���ֵ��ļ��е�ÿһ���ַ������м��ܣ�����ԭʼ������бȶԣ��Ƿ���ͬ����ͬ���ƽ��ԭʼ��������Ĳ���ӡ����
def testPass(cryptPass, dictFilePath):
    salt = cryptPass[0:2]
    try:
        dictFile = open(dictFilePath, 'r')
    except Exception, e:
        print e
        return

    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if(cryptWord == cryptPass):
            print "[+] Found Password: " + word + "\n"
            return

    print "[-] Password Not Found.\n"

#��ȡ�����������ļ���ͬʱ����testPass������������жԱ�
def crack(passwordFile, dictFile):
    try:
        passFile = open(passwordFile, 'r')
    except Exception, e:
        print e
        return

    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            cryptPass = line.split(":")[1].strip(' ')
            print "[*] Cracking Password For: " + user
            testPass(cryptPass, dictFile)

#��������������ʾ�����������ļ����ֵ��ļ���·��
def main():
    passwordFile = raw_input("Please input PassWord File Path: ")
    while not passwordFile:
        passwordFile = raw_input("Please input PassWord File Path: ")

    dictFile = raw_input("Please input Dictionary File Path: ")
    while not dictFile:
        dictFile = raw_input("Please input Dictionary File Path: ")

    print 'Start Crack Crypt Password...\n'
    crack(passwordFile, dictFile)

#����Ŀ���
if __name__ == "__main__":
    main()