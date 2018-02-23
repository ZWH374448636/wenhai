# -*- coding: gbk -*-

import cookielib
import json
import urllib2,urllib
import requests
from config.suning.mall_mgr_config import *






def MallMGRLogin(self,username,password):

    login_path = mgr_host_url+mgr_mall_login_url
    print login_path
    print username
    print password
    host = 'http://sit.mall-mgr-sn.1332255.com/mall-mgr-sn-api//authentication'
    d = {'username': username, 'password': password}
    r = requests.post(login_path, data=d)
    html = r.text
    print html
    decodejson = json.loads(html)
    statusCode = decodejson['statusCode']
    if statusCode=='200':
        token = decodejson['responseContent']['token']
        print token
    else:
        print decodejson['statusMessage']



#商城概况
def MGR_shopGeneralSituation(self,username,password):
    login_path = mgr_host_url + mgr_mall_login_url
    print login_path
    print username
    print password
    d = {'username': username, 'password': password}
    r = requests.post(login_path, data=d)
    html = r.text
    print html
    decodejson = json.loads(html)
    statusCode = decodejson['statusCode']
    if statusCode == '200':
        token = decodejson['responseContent']['token']
        print token
        url1='http://sit.mall-mgr-sn.1332255.com/mall-mgr-sn-api//api/home/shopGeneralSituation'
        aa= requests.get(login_path)
        print aa
        cookies = aa.cookies
        print 'cookies:{}'.format(cookies)
        headers = {
            "token": token,
            "Host": mgr_host_url,
            "User-Agent": " Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "cookie": cookies
        }
        data2 = {}
        s = requests.post(url1, data2, headers=headers)
        # 打印返回结果
        print(s)
        print(s.status_code, s.text)

    else:
        print decodejson['statusMessage']





