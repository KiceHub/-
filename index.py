# -*- coding: utf8 -*-
import requests,json

# 获取token
def gettoken():
    url_token = 'https://auth.xiaoyuanjijiehao.com/oauth2/token'
    headers_token = {
        'Authorization': '此处填登录时抓取的Authorization',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'auth.xiaoyuanjijiehao.com',
        'Content-Length': '147'
    }
    data_token = '此处填登录时抓取的Boby'
    rec_token = requests.post(url_token, headers=headers_token, data=data_token)
    at_text = rec_token.text
    at_json = json.loads(at_text)
    return at_json['access_token']

# 上报体温
def main_handler(event, context):
    dkurl = 'https://h5api.xiaoyuanjijiehao.com/api/staff/interface'
    data = '此处填上报时抓取的Body'
    at = gettoken()
    if at != '':
        res = requests.post(dkurl, headers={'accesstoken': at}, data=data)
