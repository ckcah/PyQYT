#!/usr/bin/python3.4
# -*- coding=utf-8 -*-
#本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
#教主QQ:605658506
#亁颐堂官网www.qytang.com
#乾颐盾是由亁颐堂现任明教教主开发的综合性安全课程
#包括传统网络安全（防火墙，IPS...）与Python语言和黑客渗透课程！
from http.client import HTTPSConnection
from base64 import b64encode
import ssl
import getpass
from xml.etree.ElementTree import parse
from xml.etree.ElementTree import XML
def ise_m_activecount(ip,username,password,port=443):

	#This sets up the https connection
	context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)#ssl支持的协议版本
	context.verify_mode = ssl.CERT_NONE#CERT_NONE, CERT_OPTIONAL or CERT_REQUIRED（并不检查证书有效性）
	context.load_verify_locations('/usr/share/kde4/apps/kssl/ca-bundle.crt')#根证书文件
	c = HTTPSConnection(ip, port=port, context=context)
	user_pass_str = username + ':' + password
	user_pass_str_encode = user_pass_str.encode()
	userAndPass = b64encode(user_pass_str_encode).decode("ascii")
	headers = { 'Authorization' : 'Basic %s' %  userAndPass }
	c.request('GET', '/admin/API/mnt/Session/ActiveCount', headers=headers)
	res = c.getresponse()
	data = res.read()
	root = XML(data.decode())
	activecount = root.find('count').text
	return activecount

if __name__ == "__main__":
	ipaddr = input('ISE地址: ')
	username = input('用户名: ')
	password = getpass.getpass('密码: ')
	activecount = ise_m_activecount(ipaddr,username,password)
	print('活动账号数量: ' + activecount)
