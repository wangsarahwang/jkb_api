#coding=utf-8
#coding=utf-8
import requests
import json
import get_token
import con_db
import urllib
import  time
import thread
con=1
global batch
batch=1

# def get_id_fre():
#     while True:
#         id_fre = con_db.get_frequecy()
#         for j in id_fre:
#             task_id = j[0]
#             fre = j[1]
#             detail_request_0(task_id, fre)
#             thread.start_new_thread(detail_request_0(), (task_id, fre,))
#             time.sleep(fre*60)


def detail_request_0(task_id,fre):
    while True:
        url = 'https://v6-api.jiankongbao.com/siteapi/data/sitetask/lasttimecheckinfos'
        token = get_token.token_request()
        print token
        header = {'token': token}
        print task_id
        data = {'task_id': task_id}
        data = urllib.urlencode(data)
        newurl = url + "?" + data
        result = requests.get(newurl, headers=header)
        d = json.loads(result.text)

        mon_points_num = d['cntGroupByResult']['total']
        #  mon_points_num=y.get("total")
        pass_points_num = d['cntGroupByResult']['1']
        fail_points_num = d['cntGroupByResult']['2']
        # con_db.insert_task_a(task_id, mon_points_num, pass_points_num, fail_points_num)

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
                                   result, resp_time, status_,batch)
        batch=batch+1
        time.sleep(fre*60)



def sign_cycle():

    global con,task11,task21,task31,task41,task51,task61,task71,task81,fre1,fre2,fre3,fre4,fre5,fre6,fre7,fre8
    con=1
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
        global con
        print fre1
        if con < 30:

            thread.start_new_thread(detail_request_0, (task11, fre1,))
            con = con + 1
            # time.sleep(fre1*60)
        elif con == 30:
            thread.start_new_thread(detail_request_1, (task11, fre1,))
            con = 1
            # time.sleep(fre1 * 60)

    def task2():
        global con,task2,fre2
        if con < 30:
            thread.start_new_thread(detail_request_0, (task21, fre2,))
            con = con + 1
            # time.sleep(fre2*60)

        elif con == 30:
            thread.start_new_thread(detail_request_1, (task21, fre2,))
            con = 1
            # time.sleep(fre2 * 60)

    def task3():
        global con,task3,fre3
        if con < 30:
            thread.start_new_thread(detail_request_0, (task31, fre3,))
            con = con + 1
        elif con == 30:
            thread.start_new_thread(detail_request_1, (task31, fre3,))
            con = 1

    def task4():
        global con,task4,fre4
        if con < 30:
            thread.start_new_thread(detail_request_0, (task41, fre4,))
            con = con + 1
        elif con == 30:
            thread.start_new_thread(detail_request_1, (task41, fre4,))
            con = 1

    def task5():
        global con,task5,fre5
        if con < 30:
            thread.start_new_thread(detail_request_0, (task51, fre5,))
            con = con + 1
        elif con == 30:
            thread.start_new_thread(detail_request_1, (task51, fre5,))
            con = 1

    def task6():
        global con,task6,fre6
        if con < 30:
            thread.start_new_thread(detail_request_0, (task61, fre6,))
            con = con + 1
        elif con == 30:
            thread.start_new_thread(detail_request_1, (task61, fre6,))
            con = 1

    def task7():
        global con,task7,fre7
        if con < 30:
            thread.start_new_thread(detail_request_0, (task71, fre7,))
            con = con + 1
        elif con == 30:
            thread.start_new_thread(detail_request_1, (task71, fre7,))
            con = 1

    def task8():
        global con,task8,fre8
        if con < 30:
            thread.start_new_thread(detail_request_0, (task81, fre8,))
            con = con + 1
        elif con == 30:
            thread.start_new_thread(detail_request_1, (task81, fre8,))
            con = 1

    def task9():
        print task1
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



def test():
    a=con_db.get_frequecy()
    for i in a:
        print i[0]
    print a




if __name__=='__main__':
    sign_cycle()




