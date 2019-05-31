#coding=utf-8

import urllib
import requests
import json
import con_db

#获取token，访问URl需要在数据库拿
def token_request():
    url_=con_db.get_url('get_token')
    url=url_[0]
    # url = 'https://v6-api.jiankongbao.com/userapi/common/apitoken'
    data_ = {"client_secret": "3da3e8b072951c474f0e3aaa69294b63bc91b1be", "client_id": "152370", "user_pwd": "67bf7dda7a1d1855b34d8678a0284f33", "user_email": "sarah.wang@akzonobel.com"}
    data=urllib.urlencode(data_)
    newurl=url+"?"+data
    result=requests.get(newurl)
    d=json.loads(result.text)
    x=d.get("token")
    return x





#if __name__ == '__main__':
 #   token_request()

