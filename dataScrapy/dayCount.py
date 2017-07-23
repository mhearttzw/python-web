import subprocess
# 因为这里是同级引用所以报错可以忽视
from dataScrapy.__file_handle import *
import os, time, decimal
import json
import requests
import mysql.connector



# Connect the database
database = "116.90.85.73"

result = ''

final_result = ''


# 统计结果并输出到文件中
def statics(api_id):
    for index in range(7):

        conn = mysql.connector.connect(host=database, user='root', passwd='6uLYFX2J', port=33336, charset='utf8',
                                       database='platformAPI')
        cur = conn.cursor()

        # 结果集查询
        sql = "SELECT result FROM api_log WHERE status=0 AND api_id= %s AND day(NOW())-day(created_time)= %s AND month(created_time)=month(Now()) and year(created_time)=year(Now());"
        cur.execute(sql, (api_id, index))
        data = cur.fetchall()

        # 结果集数量
        sql1 = "SELECT COUNT(result) FROM api_log WHERE api_id=%s AND day(NOW())-day(created_time)= %s AND month(created_time)=month(Now()) and year(created_time)=year(Now());"
        cur.execute(sql1, (api_id, index))
        count = cur.fetchall()[0][0]

        # 耗时的统计
        sql2 = "SELECT   MAX(consumed_time), ROUND(AVG(consumed_time), 2) FROM api_log WHERE api_id=%s AND day(NOW())-day(created_time)= %s AND month(created_time)=month(Now()) and year(created_time)=year(Now());"
        cur.execute(sql2, (api_id, index))
        time_statics = cur.fetchall()
        max_time = time_statics[0][0]
        avg_time = time_statics[0][1]

        conn.commit()
        cur.close()
        conn.close()

        isUseful = 0
        for row in data:  # data是一个列表，一次循环一行，row代表一行，row以元祖的形式显示
            result = json.loads(row[0])['data']['match']  # loads将str转化为dict格式
            if result:
                isUseful += 1

        if count == 0:
            write_file(count, 0, 0, 0, 0, index, api_id)
        else:
            # round改为使用decimal模块
            rate = round(isUseful / count, 5)

            # print(count)
            # print('成功匹配量：' + str(isUseful))
            # print(rate)
            # print(str(avg_time) + '\n')

            write_file(count, isUseful, rate, max_time, avg_time, index, api_id)


# 统计结果并保存到变量中
def save_final_html(api_id):
    result_html = ''
    # 查询近一周的数据
    for index in range(7):

        conn = mysql.connector.connect(host=database, user='root', passwd='6uLYFX2J', port=33336, charset='utf8',
                                       database='platformAPI')
        cur = conn.cursor()

        # 结果集查询
        sql = "SELECT result FROM api_log WHERE status=0 AND api_id= %s AND day(NOW())-day(created_time)= %s AND month(created_time)=month(Now()) and year(created_time)=year(Now());"
        cur.execute(sql, (api_id, index))
        data = cur.fetchall()

        # 结果集数量
        sql1 = "SELECT COUNT(result) FROM api_log WHERE api_id=%s AND day(NOW())-day(created_time)= %s AND month(created_time)=month(Now()) and year(created_time)=year(Now());"
        cur.execute(sql1, (api_id, index))
        count = cur.fetchall()[0][0]

        # 耗时的统计
        sql2 = "SELECT   MAX(consumed_time), ROUND(AVG(consumed_time), 2) FROM api_log WHERE api_id=%s AND day(NOW())-day(created_time)= %s AND month(created_time)=month(Now()) and year(created_time)=year(Now());"
        cur.execute(sql2, (api_id, index))
        time_statics = cur.fetchall()
        max_time = time_statics[0][0]
        avg_time = time_statics[0][1]

        conn.commit()
        cur.close()
        conn.close()

        isUseful = 0
        for row in data:  # data是一个列表，一次循环一行，row代表一行，row以元祖的形式显示
            result = json.loads(row[0])['data']['match']  # loads将str转化为dict格式
            if result:
                isUseful += 1

        if count == 0:
            result_html += str(save_html(count, 0, 0, 0, 0, index, api_id))
            print("result:" +result_html)
        else:
            # round改为使用decimal模块
            rate = round(isUseful / count, 5)

            print(count)
            print('成功匹配量：' + str(isUseful))
            print(rate)
            print('平均时间:' +str(avg_time))

            tmp  = str(save_html(count, isUseful, rate, max_time, avg_time, index, api_id))
            print("result_tmp:" + tmp)
            result_html += tmp
    # 返回html结果
    return result_html


# statics(18)
# statics(26)




