# -*- coding: UTF-8 -*-
import urllib2
import re
import sys
import os
url = "http://www.360kb.com/kb/2_122.html"
# req = urllib2.Request(url)
html = urllib2.urlopen(url).read()
# head_ver = html.find(r'<strong>google hosts </strong><strong>')
# ver_before = len("<strong>google hosts </strong><strong>")
# tail_ver = html.find(r' </strong>更新')

head_span = html.find('#base services')
tail_span = html.find('#google source end')
raw_hosts = html[head_span:tail_span]
result, number = re.subn(r'<.*>', '', raw_hosts)
pure_hosts, number = re.subn(r' ', ' ', result)
arch = """127.0.0.1       localhost
255.255.255.255 broadcasthost
::1     localhost
127.0.0.1       hecom.cc
"""
f = file(r'/tmp/hosts' ,'w+')
new_host = [arch,pure_hosts]
f.writelines(new_host)
f.close()
os.system('sudo mv /tmp/hosts /etc/hosts')
os.system('dscacheutil -flushcache')
print "Update success!"