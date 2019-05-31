# import pymssql
# server="1000"
# user="dulux"
# password="Fighting0624"
# db = pymssql.connect(host='127.0.0.1', port='1433', user='dulux', password='Fighting0624', database='jkb_api',
#                       charset='UTF-8')
# cur = db.cursor()
# sql = "INSERT INTO operator(isp_id,isp_name,en_name) VALUES('%s','%s','%s')"
# data=(90,1,1)
# # data=(id,name,e_name)
# cur.execute(sql,data)
# db.commit()
#coding=utf-8

# import pymssql
# conn = pymssql.connect(host='127.0.0.1',port='1433',user='dulux',password='Fighting0624',database='jkb_api', charset='UTF-8')
#
# cursor = conn.cursor()
#
# cursor.execute("""
# IF OBJECT_ID('persons', 'U') IS NOT NULL
#     DROP TABLE persons
# CREATE TABLE persons (
#     id INT NOT NULL,
#     name VARCHAR(100),
#     salesrep VARCHAR(100),
#     PRIMARY KEY(id)
# )
# """)
# cursor.executemany(
#     "INSERT INTO persons VALUES (%d, %s, %s)",
#     [(1, 'John Smith', 'John Doe'),
#      (2, 'Jane Doe', 'Joe Dog'),
#      (3, 'Mike T.', 'Sarah H.')])
#
# conn.commit()
#
#
# cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
# row = cursor.fetchone()
# while row:
#     print("ID=%d, Name=%s" % (row[0], row[1]))
#     row = cursor.fetchone()
#
#
# # for row in cursor:
# #     print("ID=%d, Name=%s" % (row[0], row[1]))
#
# conn.close()
str = '\xe8\xbe\xbd\xe5\xae\x81\xe5\xa4\xa7\xe8\xbf\x9e\xe8\x81\x94\xe9\x80\x9a'

print str.decode('utf-8')


