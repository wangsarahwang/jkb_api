#coding=utf-8
import requests
import json
import get_token
import urllib
import con_db

def get_locations():
    url = 'https://v6-api.jiankongbao.com/siteapi/tasks/locations'
    token = get_token.token_request()
    header = {'token': token}
    data={'level':'0'}
    data = urllib.urlencode(data)
    newurl = url + "?" + data
    result = requests.get(newurl, headers=header)
 #   print result.text
    d = json.loads(result.text)
    for item in d['data']:
       # res=json.load(item)
       lo_code=item.get("location_code")
       lo_name=item.get("location_name")
       en_name=item.get("en_name")
       #print en_name
       con_db.instert_location(lo_code,lo_name,en_name)


if __name__=='__main__':
    get_locations()