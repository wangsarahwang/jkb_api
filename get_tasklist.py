#coding=utf-8
import requests
import json
import get_token
import con_db

def point_request():
    url='https://v6-api.jiankongbao.com/siteapi/tasks/list'
    token = get_token.token_request()
    header = {'token': token}
    result = requests.post(url, headers=header)
    # print result.text
    d = json.loads(result.text)
    # print d
    for item in d['data']:
       # res=json.load(item)
       t_id=item.get("task_id")
       t_name=item.get("task_name")
       t_sum=item.get("task_summary")
       t_type=item.get("task_type")
       t_create_time=item.get("task_create_time")
       frequency=item.get("frequency")
       t_status=item.get("task_status")
       group_id=item.get("group_id")
       last_resp_result=item.get("last_resp_result")
       threshold_result=item.get("threshold_result")
       last_check_time=item.get("last_check_time")
       if con_db.is_task(t_id)==0:
           con_db.insert_task(t_id,t_name,t_sum,t_type,t_create_time,frequency,t_status,group_id,last_resp_result,threshold_result,last_check_time)
       else:
           con_db.update_task(t_id,t_name,t_sum,t_type,t_create_time,frequency,t_status,group_id,last_resp_result,threshold_result,last_check_time)







if __name__=='__main__':
    point_request()