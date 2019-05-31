#coding=utf-8
import time
import pymssql
#所有对数据库的操作

db= pymssql.connect(host='127.0.0.1',port='1433',user='dulux',password='Fighting0624',database='jkb_api', charset='UTF-8')

#插入运营商
def instert_operation(id1,name1,e_name1):
    id = id1
    name = name1
    e_name = e_name1
    cur = db.cursor()
    sql = "INSERT INTO operator(isp_id,isp_name,en_name) VALUES('%s','%s','%s')"
    data=(id,name,e_name)
    cur.execute(sql%data)
    db.commit()

    #插入地区
def instert_location(code,name,e_name):
    code=code
    name=name
    e_name=e_name
    cur=db.cursor()
    sql="Insert into location values ('%s','%s','%s')"
    data=(code,name,e_name)
    cur.execute(sql%data)
    db.commit()
#插入监控点
def insert_point(mo_id,mo_name,isp_id,lo_code):
    mo_id=mo_id
    mo_name=mo_name
    isp_id=isp_id
    lo_code=lo_code
    cur=db.cursor()
    sql="INSERT INTO monitor_point VALUES('%s','%s','%s','%s')"
    data=(mo_id,mo_name,isp_id,lo_code)
    cur.execute(sql%data)
    db.commit()

#插入监控列表
def insert_task(t_id,t_name,t_sum,t_type,t_create_time,frequency,t_status,group_id,last_resp_result,threshold_result,last_check_time):

    cur = db.cursor()
    sql = "INSERT INTO task(task_id,task_name,task_summary,task_type,task_create_time,frequency,task_status,group_id,last_resp_result,threshold_result,last_check_time) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    data = (
        t_id, t_name, t_sum, t_type, t_create_time, frequency, t_status, group_id, last_resp_result, threshold_result,
        last_check_time)
    cur.execute(sql % data)
    db.commit()

def is_task(task_id):
    cur=db.cursor()
    cur.execute("select count(*) from task where task_id='%s'"%task_id)
    return  cur.fetchone()

def update_task(t_id,t_name,t_sum,t_type,t_create_time,frequency,t_status,group_id,last_resp_result,threshold_result,last_check_time):
    cur=db.cursor()
    sql="update task set task_name='%s',task_summary='%s',task_type='%s',task_create_time='%s',frequency='%s',task_status='%s',group_id='%s',last_resp_result='%s',threshold_result='%s',last_check_time='%s' where task_id='%s'"

    data=(t_name,t_sum,t_type,t_create_time,frequency,t_status,group_id,last_resp_result,threshold_result,last_check_time,t_id)
    cur.execute(sql % data)
    db.commit()

#插入监控记录
def insert_detail_0(task_id, monitor_id, monitor_name, location_name, isp_name, isp_id, monitorIp, result, resp_time,
        status_,insert_time,sign,batch):

    db0= pymssql.connect(host='127.0.0.1', port='1433', user='dulux', password='Fighting0624', database='jkb_api',
                         charset='UTF-8')
    cur = db0.cursor()
    sql = "INSERT INTO details (task_id, monitor_id, monitor_name, location_name, isp_name, isp_id, monitorIp, result, resp_time,status_,insert_time,sign,batch)VALUES(%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
    data = (
        task_id, monitor_id, monitor_name, location_name, isp_name, isp_id, monitorIp, result, resp_time,
        status_, insert_time, sign,batch)
    cur.execute(sql%data)

    db0.commit()
    cur.close()
    db0.close()



#插入task表里的后四个字段
def insert_task_a(task_id,mon_points_num,pass_points_num,fail_points_num):
     db = pymssql.connect(host='127.0.0.1', port='1433', user='dulux', password='Fighting0624', database='jkb_api',
                          charset='UTF-8')
     cur=db.cursor()
     sql="update task set mon_points_num='%s',pass_points_num='%s',fail_points_num='%s' ,point_update_time='%s' where task_id='%s'"
     data=(mon_points_num,pass_points_num,fail_points_num,int(time.time()),task_id)
     cur.execute(sql%data)
     db.commit()


#在数据库拿到url
def get_url(url_name):

    db1= pymssql.connect(host='127.0.0.1',port='1433',user='dulux',password='Fighting0624',database='jkb_api', charset='UTF-8')
    name=url_name
    cur=db1.cursor()
    cur.execute("select url FROM url where URL_name='%s'"% name)
    result=cur.fetchone()
    return  result

#查询task_id和频次
def get_frequecy():
    cur=db.cursor()
    cur.execute("select task_id,frequency FROM schedule_ ")
    result=cur.fetchall()
    return result

def get_batch(task_id):

    db = pymssql.connect(host='127.0.0.1', port='1433', user='dulux', password='Fighting0624', database='jkb_api',
                         charset='UTF-8')
    cur = db.cursor()
    cur.execute("select batch FROM schedule_ where task_id='%s'"%task_id)
    result = cur.fetchall()
    return result

def update_batch(task_id,batch):
    db= pymssql.connect(host='127.0.0.1',port='1433',user='dulux',password='Fighting0624',database='jkb_api', charset='UTF-8')
    cur=db.cursor()
    sql = "update schedule_ set batch='%s' where task_id='%s'"
    data = (batch,task_id)
    cur.execute(sql % data)
    db.commit()

def get_con(task_id):

    db= pymssql.connect(host='127.0.0.1',port='1433',user='dulux',password='Fighting0624',database='jkb_api', charset='UTF-8')
    cur = db.cursor()
    cur.execute("select con FROM schedule_ where task_id='%s'"%task_id)
    result = cur.fetchall()
    return result

def update_con(task_id,con):

    db = pymssql.connect(host='127.0.0.1', port='1433', user='dulux', password='Fighting0624', database='jkb_api',
                         charset='UTF-8')
    cur=db.cursor()
    sql = "update schedule_ set con='%s' where task_id='%s'"
    data = (con,task_id)
    cur.execute(sql % data)
    db.commit()





# if __name__=='__main__':
   # print get_frequecy()