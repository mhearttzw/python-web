from flask_restful import reqparse, abort, Api, Resource
import mysql.connector
import json


class RecommendList(Resource):
    LogInfo = {'host': '182.254.230.24', 'user': 'fleeter', 'passwd': 'hust201417',
               'port': 3306, 'charset': 'utf8', 'database': 'fleeting'}
    video_list = []

    def __init__(self):
        conn = mysql.connector.connect(host=self.LogInfo['host'], user=self.LogInfo['user'],
                                       passwd=self.LogInfo['passwd'],
                                       port=self.LogInfo['port'], charset=self.LogInfo['charset'],
                                       database=self.LogInfo['database'])
        cur = conn.cursor(buffered=True)

        # cur.execute("""SELECT title, cover, description, url, size, type FROM fl_video""")
        params = ('id', 'title', 'cover', 'description', 'url', 'size', 'type')
        cur.execute("""SELECT id, title, cover, description, url, size, type FROM fl_video""")

        # v = cur.fetchone()
        # self.video_list = {}
        # for i in range(len(params)):
        #     self.video_list[params[i]] = v[i]

        video_list = cur.fetchall()
        for v in video_list:
            video = {}
            for i in range(len(params)):
                video[params[i]] = v[i]
            self.video_list.append(video)

        cur.close()
        conn.commit()
        conn.close()
        # self.video_list = video_info

    def get(self):
        # json_list = json.dumps(self.video_list)
        return self.video_list


if __name__ == '__main__':
    test = RecommendList()
    print(test.get())
