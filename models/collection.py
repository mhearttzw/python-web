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

    # def post(self, username):



    def get(self, username):
        self.collection_list = []
        params = ('id', 'title', 'cover', 'description', 'url', 'size', 'type')
        query = "SELECT id, title, cover, description, url, size, type " \
                "FROM fl_video as v, (SELECT video_id FROM fl_collection " \
                "WHERE user_id = %s) AS c WHERE v.id = c.video_id"
        self.cur.execute(query, (username,))
        collection_list = self.cur.fetchall()
        for cnt in range(len(collection_list)):
            v = collection_list[cnt]
            video = {}
            for i in range(len(params)):
                video[params[i]] = v[i]
            self.collection_list.append(video)
        return self.collection_list


if __name__ == '__main__':
    test = Collection().collection_list
    print(test)
