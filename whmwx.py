# !/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
from sys import argv
from urllib import request
import requests
from datetime import datetime

timeout = 10
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
key = 'Server酱申请KEY'
title = "WHMCS面板VPS上货监测"
pid = sys.argv[1]
#需要WHMCS面板对应监控的URL
url = 'https://www.example.com/cart.php?a=add&pid='+str(pid)
head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
try:
    req = request.Request(url, headers=head)
    response = request.urlopen(req, timeout=timeout)
    html = response.read()
    html = html.decode("utf-8").lower()
    str="out of stock"
    if str in html:
        print("缺货" + "\n" + time)
    else:
        print("不缺货" + "\n" + time)
        content = "当前上货啦~" + "\n" + time + "\n" + url

        payload = {
            'text': title,
            'desp': content
        }
        fturl = 'https://sc.ftqq.com/{}.send'.format(key)
        requests.post(fturl, params=payload, timeout=timeout)
except Exception:
    print("Error" + "\n" + time)