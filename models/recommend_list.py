from flask_restful import reqparse, abort, Api, Resource
import mysql.connector
import json


class RecommendList(Resource):
    LogInfo = {'host': '182.254.230.24', 'user': 'fleeter', 'passwd': 'hust201417',
               'port': 3306, 'charset': 'utf8', 'database': 'fleeting'}
    video_list = []
    conn = None
    cur = None

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

    def get(self):
        self.video_list = []
        params = ('id', 'title', 'cover', 'description', 'url', 'size', 'type')
        self.cur.execute("""SELECT id, title, cover, description, url, size, type FROM fl_video""")

        video_list = self.cur.fetchall()
        for cnt in range(len(video_list)):
            v = video_list[cnt]
            video = {}
            for i in range(len(params)):
                video[params[i]] = v[i]
            self.video_list.append(video)
        return self.video_list


if __name__ == '__main__':
    test = RecommendList().video_list
    print(test)
