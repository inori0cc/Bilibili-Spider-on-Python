"""---------------------------by me-----------------------------"""
import pandas as pd
from sqlalchemy import create_engine

sql = 'select * from zhuanlan_youxi'
conn = create_engine('mysql+pymysql://root:12345678@localhost:3306/bilibili')
pdata = pd.read_sql(sql,conn)
reasons= pdata['category']

reasons.value_counts()

import matplotlib.pyplot as plt
labels = '手机游戏', '单机游戏', '网络游戏', '电子竞技', '桌游棋牌'
sizes = [371, 278, 194, 102, 56]
explode = (0.2, 0.1, 0.1, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("游戏专栏中游戏种类分布")
plt.show()
"""---------------------------by me-----------------------------"""