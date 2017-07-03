from flask_restful import reqparse, abort, Api, Resource
import mysql.connector
import json


class SortedList(Resource):
    LogInfo = {'host': '182.254.230.24', 'user': 'fleeter', 'passwd': 'hust201417',
               'port': 3306, 'charset': 'utf8', 'database': 'fleeting'}
    api_dict = {
        "anime": "动画短片",

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
        # json_list = json.dumps(self.video_list)

        # cur.execute("""SELECT title, cover, description, url, size, type FROM fl_video""")
        params = ('id', 'title', 'cover', 'description', 'url', 'size', 'type')
        ele = (self.api_dict[type],)
        query = " "
        self.cur.execute(query, ele)
        # v = cur.fetchone()
        # self.video_list = {}
        # for i in range(len(params)):
        #     self.video_list[params[i]] = v[i]

        video_list = self.cur.fetchall()
        for v in video_list:
            video = {}
            for i in range(len(params)):
                video[params[i]] = v[i]
            self.video_list.append(video)
        return self.video_list



if __name__ == '__main__':
    test = SortedList()
    print(test.get())