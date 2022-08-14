"""---------------------------by me-----------------------------"""
import pandas as pd
from sqlalchemy import create_engine

sql = 'select * from banned'
conn = create_engine('mysql+pymysql://root:12345678@localhost:3306/bilibili')
pdata = pd.read_sql(sql,conn)
reasons= pdata['banned_reason']

reasons.value_counts()

import matplotlib.pyplot as plt
labels = '发布引战言论', '发布人身攻击言论', '发布垃圾广告信息', '发布色情信息', '刷屏', '发布赌博诈骗信息', '发布传播不实信息','其它'
sizes = [200, 140, 84, 29, 33, 13, 10, 51]
explode = (0.2, 0.1, 0, 0,0,0,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("封禁原因分布")
plt.show()
"""---------------------------by me-----------------------------"""