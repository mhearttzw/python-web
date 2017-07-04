from flask_restful import reqparse, abort, Api, Resource
import mysql.connector
import json
from orm.fl_video import User


class RecommendList(Resource, User):
    LogInfo = {'host': '182.254.230.24', 'user': 'fleeter', 'passwd': 'hust201417',
               'port': 3306, 'charset': 'utf8', 'database': 'fleeting'}
<<<<<<< HEAD
    # 返回数据以json格式呈现
    video_list = {}
=======
    video_list = []
    conn = None
    cur = None
>>>>>>> ed659813b343d1a79616bcb0756ffe154ea8edb8

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
<<<<<<< HEAD

        cur.close()
        conn.commit()
        conn.close()
        # self.video_list = video_info

    # def get(self, User):
    #     video_obj = User.query.all()
    #     for i in range(len(video_obj)):
    #         User.video_list.append({
    #             "title1": video_obj[i].title,
    #             "cover": video_obj[i].cover,
    #             "description": video_obj[i].description,
    #             "info": video_obj[i].info,
    #             "url": video_obj[i].url,
    #             "upload_time": video_obj[i].upload_time,
    #             "size": video_obj[i].size,
    #             "duration": video_obj[i].duration,
    #             "type": video_obj[i].type
    #         })
    #     return self.video_list

    def get(self):
        # json_list = json.dumps(self.video_list)
=======
>>>>>>> ed659813b343d1a79616bcb0756ffe154ea8edb8
        return self.video_list


if __name__ == '__main__':
    test = RecommendList().video_list
    print(test)
