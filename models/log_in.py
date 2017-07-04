

from flask import request
from flask_restful import reqparse, abort, Api, Resource
import mysql.connector
import json


class SortedList(Resource):
    LogInfo = {'host': '182.254.230.24', 'user': 'fleeter', 'passwd': 'hust201417',
               'port': 3306, 'charset': 'utf8', 'database': 'fleeting'}
    api_dict = {
        "anime": "动画短片",

    }
    response = {
        "isRegisted": 1
    }
    video_list = []
    conn = None

    def __init__(self):
        self.conn = mysql.connector.connect(host=self.LogInfo['host'], user=self.LogInfo['user'],
                                            passwd=self.LogInfo['passwd'],
                                            port=self.LogInfo['port'], charset=self.LogInfo['charset'],
                                            database=self.LogInfo['database'])
        self.cur = self.conn.cursor(buffered=True)

    def __del__(self):
        self.cur.close()
        self.conn.commit()
        self.conn.close()
        # self.video_list = video_info

    def get(self, type):
        if type == '/register':
            query = "SELECT username FROM fl_user"
            self.cur.execute(query)
            haveregisted = self.cur.fetchall()
            # 判断是否已被注册
            if len(haveregisted) is not 0:
                self.response["isRegisted"] = 0
                return self.response
            userName = request.form['username']
            passWord = request.form['password']
            insert = "INSERT INTO fl_user(username, password) VALUES (%s, %s)"
            self.cur.execute(insert, (userName, passWord))
            self.response["isRegisted"] = 1
            return self.response
        elif type == '/user':
            query = "SELECT username FROM fl_user"
            self.cur.execute(query)
            haveregisted = self.cur.fetchall()
            passWord = request.form['password']
            if len(haveregisted) is not 0:
                query = "SELECT password FROM fl_user WHERE username= %s"
                self.cur.execute(query, (passWord,))
                passWordRight = self.cur.fetchall()
                if len(passWordRight) is not 0:
                    return '登录成功'
                else:
                    return '1' #密码错误
            else:
                return '0' #用户名未注册




if __name__ == '__main__':
    test = SortedList()
    print(test.get())