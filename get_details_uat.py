#coding=utf-8
import requests
import json
import get_token
import con_db
import urllib
import time
import thread
import threading




def detail_request_0(task_id,):

    batch0=con_db.get_batch(task_id)
    con0=con_db.get_con(task_id)
    batch=batch0[0][0]
    con=con0[0][0]
    # print batch

    url1 = con_db.get_url('getdetail')
    url = url1[0]
    # url = 'https://v6-api.jiankongbao.com/siteapi/data/sitetask/lasttimecheckinfos'
    token = get_token.token_request()
    # print token
    header = {'token': token}
    # print task_id
    data = {'task_id': task_id}
    data = urllib.urlencode(data)
    newurl = url + "?" + data
    result = requests.get(newurl, headers=header)
    d = json.loads(result.text)


    # print d["msg"]
    now = int(time.time())

    mon_points_num = d['cntGroupByResult']['total']
    #  mon_points_num=y.get("total")
    pass_points_num = d['cntGroupByResult']['1']
    fail_points_num = d['cntGroupByResult']['2']
    con_db.insert_task_a(task_id, mon_points_num, pass_points_num, fail_points_num)
    if con < 30:
        for i in d['data']:
            monitor_id = i.get("monitor_id")
            monitor_name = i.get("monitor_name")
            location_name = i.get("location_name")
            isp_name = i.get("isp_name")
            isp_id = i.get("isp_id")
            monitorIp = i.get("monitorIp")
            result = i.get("result")
            resp_time = i.get("resp_time")
            status_ = i.get("status")
            con_db.insert_detail_0(task_id, monitor_id, monitor_name, location_name, isp_name, isp_id, monitorIp,
                                   result, resp_time, status_, now, 0, batch)

        con = con + 1
    elif con == 30:
        for i in d['data']:
            monitor_id = i.get("monitor_id")
            monitor_name = i.get("monitor_name")
            location_name = i.get("location_name")
            isp_name = i.get("isp_name")
            isp_id = i.get("isp_id")
            monitorIp = i.get("monitorIp")
            result = i.get("result")
            resp_time = i.get("resp_time")
            status_ = i.get("status")
            con_db.insert_detail_0(task_id, monitor_id, monitor_name, location_name, isp_name, isp_id, monitorIp,
                                   result, resp_time, status_, now, 1, batch)
            con=1


    batch = batch + 1

    con_db.update_batch(task_id,batch)
    con_db.update_con(task_id,con)






def sign_cycle():

    global task11,task21,task31,task41,task51,task61,task71,task81,fre1,fre2,fre3,fre4,fre5,fre6,fre7,fre8
    id_fre = con_db.get_frequecy()
    task11=id_fre[0][0]
    fre1=id_fre[0][1]
    task21 = id_fre[1][0]
    fre2 = id_fre[1][1]
    task31 = id_fre[2][0]
    fre3= id_fre[2][1]
    task41 = id_fre[3][0]
    fre4= id_fre[3][1]
    task51= id_fre[4][0]
    fre5= id_fre[4][1]
    task61= id_fre[5][0]
    fre6= id_fre[5][1]
    task71= id_fre[6][0]
    fre7 = id_fre[6][1]
    task81 = id_fre[7][0]
    fre8 = id_fre[7][1]
    # print task3
    def task1():
        def task1_1():
            thread.start_new_thread(detail_request_0, (task11,))
            timer = threading.Timer(fre1 * 60, task1_1)
            timer.start()
        task1_1()



    def task2():
        thread.start_new_thread(detail_request_0, (task21,))
        timer = threading.Timer(fre2* 60, task2)
        timer.start()

    def task3():
        thread.start_new_thread(detail_request_0, (task31,))
        timer = threading.Timer(fre3* 60, task3)
        timer.start()

    def task4():
        thread.start_new_thread(detail_request_0, (task41,))
        timer = threading.Timer(fre4* 60, task4)
        timer.start()

    def task5():
        thread.start_new_thread(detail_request_0, (task51,))
        timer = threading.Timer(fre5* 60, task5)
        timer.start()

    def task6():
        thread.start_new_thread(detail_request_0, (task61,))
        timer = threading.Timer(fre6* 60, task6)
        timer.start()

    def task7():
        thread.start_new_thread(detail_request_0, (task71,))
        timer = threading.Timer(fre7 * 60, task7)
        timer.start()

    def task8():
        thread.start_new_thread(detail_request_0, (task81,))
        timer = threading.Timer(fre8 * 60, task8)
        timer.start()
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    while 1:
        pass

# if __name__=='__main__':
#     sign_cycle()
#




