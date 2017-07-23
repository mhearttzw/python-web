from flask import request
from flask_restful import  Resource
import mysql.connector


class Collection(Resource):
    LogInfo = {'host': '182.254.230.24', 'user': 'fleeter', 'passwd': 'hust201417',
               'port': 3306, 'charset': 'utf8', 'database': 'fleeting'}

    collection_list = []
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

    def delete(self):
        userid = request.form['userid']
        videoid = request.form['videoid']
        params = ('user_id', 'video_id')
        query = "DELETE FROM fl_collection WHERE "
        self.cur.execute(query, (int(userid), int(videoid)))


    def post(self):
        self.collection_item = None
        userName = request.form['username']
        print(userName)
        query = "SELECT id FROM fl_user WHERE username = %s"
        self.cur.execute(query, (userName,))
        userid = self.cur.fetchone()[0]
        videoid = request.form['videoid']
        query = "SELECT * FROM fl_collection WHERE user_id = %s AND video_id = %s"
        self.cur.execute(query, (int(userid), int(videoid)))
        collection_item = self.cur.fetchall()
        print(collection_item)
        if len(collection_item) is not 0:
            query = "DELETE FROM fl_collection WHERE user_id = %s AND video_id =%s"
            self.cur.execute(query, (int(userid), int(videoid)))
            return 1 #返回删除视频收藏信号
        else:
            print("userid:" + str(userid) + "video: " + str(videoid))
            # params = ('user_id', 'video_id')
            query = "INSERT INTO fl_collection (user_id, video_id) " \
                    "VALUES ('%s', '%s')"
            self.cur.execute(query, (int(userid), int(videoid)))
            return 0 #返回成功信号

    def get(self, username):
        self.collection_list = []
        params = ('id', 'title', 'cover', 'description', 'url', 'size', 'type')
        query = "SELECT id FROM fl_user WHERE username = %s"
        self.cur.execute(query, (username,))
        userid = self.cur.fetchone()[0]
        print(userid)
        query = "SELECT id, title, cover, description, url, size, type " \
                "FROM fl_video as v, (SELECT video_id FROM fl_collection " \
                "WHERE user_id = %s) AS c WHERE v.id = c.video_id"
        self.cur.execute(query, (int(userid),))
        collection_list = self.cur.fetchall()
        for cnt in range(len(collection_list)):
            v = collection_list[cnt]
            video = {}
            for i in range(len(params)):
                video[params[i]] = v[i]
            self.collection_list.append(video)
        print(self.collection_list)
        return self.collection_list


if __name__ == '__main__':
    test = Collection().get("zzz")
    print(test)
