#coding=utf-8
import requests
import json
import get_token
import con_db

def point_request():
    url='https://v6-api.jiankongbao.com/siteapi/tasks/monitors'
    token = get_token.token_request()
    header = {'token': token}
    result = requests.post(url, headers=header)
    # print result.text
    d = json.loads(result.text)
    for item in d['data']:
       # res=json.load(item)
       lo_code=item.get("location_code")
       mo_id=item.get("monitor_id")
       mo_name=item.get("monitor_name")
       isp_id=item.get("isp_id")
       #print en_name
       con_db.insert_point(mo_id,mo_name,isp_id,lo_code)



if __name__=='__main__':
    point_request()