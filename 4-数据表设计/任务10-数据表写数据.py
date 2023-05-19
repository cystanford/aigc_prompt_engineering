import pandas as pd
from sqlalchemy import create_engine

# 读取Excel文件
df = pd.read_excel('LeetCode试题列表.xlsx')

# 将acceptance字段转化为float类型
df['acceptance'] = df['acceptance'].str.strip('%').astype(float) / 100
#print('df=', df)

# 连接MySQL数据库
#engine = create_engine('mysql+pymysql://<用户名>:<密码>@<主机名>:<端口>/<数据库名>')
engine = create_engine('mysql+pymysql://wucai:wucai1234!@rm-uf6z891lon6dxuqblqo.mysql.rds.aliyuncs.com:3306/chatgpt')

# 将数据写入到MySQL数据表
df.to_sql('problem_list', engine, if_exists='replace', index=False)
