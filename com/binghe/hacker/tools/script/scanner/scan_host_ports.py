#!/usr/bin/env python
# -*- coding: gbk -*-
# -*- coding: utf-8 -*-
# Date: 2019/2/12
# Created by ����
# Description �˿�ɨ����  �÷���  python xxx.py -H targetHost -p targetPort[s]
#                              python scan_hosts01.py -H 10.2.2.250 -p 21,22,80,443,135,445
#                              python scan_hosts01.py -H 10.2.2.250 -p 21
#                       ע��: ɨ���˿ڣ��˿���˿�֮�䲻Ҫ�пո�
# ���� https://blog.csdn.net/l1028386804

import optparse
from socket import *
from threading import *

#�ź���
screenLock = Semaphore(value=1)

#����Ŀ�������Ͷ˿ڣ����ӳɹ���ӡĿ��˿ڿ��ţ����Ӳ��ɹ����ӡĿ��˿ڹر�
def connScan(tgtHost, tgtPort):
    try:
        # print '\n[*] Scanning port ' + str(tgtPort)
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        #����Ŀ�������ض��˿ڷ���һ�����ݴ����ȴ���Ӧ�������ռ�������Ӧ�������ƶϳ���Ŀ�������Ͷ˿������е�Ӧ��
        connSkt.send('ViolentPython\r\n')
        #������Ӧ��Ϣ
        results = connSkt.recv(100)
        #���ź�����������֤��ͬһ��ʱ��ֻ��һ���̴߳�ӡ���
        screenLock.acquire()
        print '\n[+] %d/tcp open' % tgtPort
        print '[+] ' + str(results)

    except:
        #�ź�����������֤��ͬһ��ʱ��ֻ��һ���̴߳�ӡ���
        screenLock.acquire()
        print '\n[-] %d/tcp closed' % tgtPort
    finally:
        #�ͷ���
        screenLock.release()
        connSkt.close()

#ɨ��Ŀ������ָ���Ķ˿��б�
def portScan(tgtHost, tgtPorts):
    try:
        #ȷ����������Ӧ��IP��ַ
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s' : Unknown host" % tgtHost
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan Results for: ' + tgtName[0]
    except:
        print '\n[+] Scan Results for: ' + tgtIP

    #����Ĭ�ϳ�ʱʱ��
    setdefaulttimeout(2)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()


#���������������������ö˿�ɨ�跽��
def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port[s]>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s]')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print '[-] You must specify a target host and port[s]: ' + parser.usage
        exit(0)
    portScan(tgtHost, tgtPorts)

#�������
if __name__ == '__main__':
    main()