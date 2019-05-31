#coding=utf-8

import  urllib
import requests
import json
import get_token
import con_db
url='https://v6-api.jiankongbao.com/siteapi/tasks/isps'


def isp_request():
    token=get_token.token_request()
    header = {'token':token}
    result = requests.get(url,headers=header)
    print result.text
    d = json.loads(result.text)
    for item in d['data']:
       # res=json.load(item)
       isp_id=item.get("isp_id")
       isp_name=item.get("isp_name")
       en_name=item.get("en_name")
       print en_name
       con_db.instert_operation(isp_id,isp_name,en_name)



    #print d["data"][0]









if __name__=='__main__':
    isp_request(url)