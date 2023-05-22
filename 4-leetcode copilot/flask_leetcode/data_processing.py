"""
  数据处理的通用类
  @Author : Chen Yang
"""
import pandas as pd
import socket
import pymysql 

from datetime import datetime
# 得到当前的时间，比如 2023-04-02 11:32
def get_current_time():
    now = str(datetime.now())[0:16]
    return now

# 得到当前的时间，比如 2023-04-02 11:32
def get_current_date():
    now = str(datetime.now())[0:10]
    return now
    
# 创建&返回session
def get_db_session(db='chatgpt'):
	conn = pymysql.connect(host='localhost', port=3306, user='用户名', passwd='密码', db=db)
	cur = conn.cursor()
	# 取消mysql查询缓存
	sql = "SET autocommit=1;"
	cur.execute(sql)
	return conn, cur

if __name__ == '__main__':
	print(get_ip_address())