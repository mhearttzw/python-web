import subprocess
import json
import requests
import mysql.connector

database = "182.254.230.24"
req_url = "http://www.acfun.cn/rank.aspx?channelId=106&range=1&count=30&ext=1&date="
res1 = requests.get(req_url)
res = res1.json()
print(res[0]['url'])
#   type
type_video = "动画短片"

for i in range(len(res)):
    url_vedio = "http://www.acfun.cn" + res[i]['url']
    child = subprocess.Popen(["you-get", "--json", url_vedio], stdout= subprocess.PIPE)
    out = child.communicate()[0]
    temp = str(out, encoding="UTF-8")
    url = json.loads(temp)["streams"]["__default__"]["src"]
# 		subprocess.Popen.terminate()
    # >> > isinstance(['d', 'd'], str)
    # >> > isinstance(['d', 'd'], list)

    # time
    # ISOTIMEFORMAT = '%Y-%m-%d %X'
    # upload_time= time.strftime(ISOTIMEFORMAT, time.localtime())
    size = int(json.loads(temp)["streams"]["__default__"]["size"]/1024)
    # title
    title =  res[i]['title']
    description = res[i]['description']
    cover = res[i]['userImg']
    print(res[0])
    # a+= 1
    #################### 连接数据库 #################
    conn = mysql.connector.connect(host=database, user='fleeter', passwd='hust201417', port=3306, charset='utf8',
                                   database='fleeting')
    cur = conn.cursor()
    #                      conn.select_db('test')
    # cur.execute('create table video')
    temp = [str(title), str(cover), str(description), url, size, type_video]
    print(temp)
    add_values = (str(title), str(cover), str(description), str(url), str(size), str(type_video))
    print(add_values)
    add_names = ('INSERT INTO fl_video (title, cover, description, url, size, type) '
                 'VALUES (%s,%s,%s,%s,%s,%s)')
    cur.execute(add_names, add_values)
    # Make sure data is committed to the database
    conn.commit()

    cur.close()
    conn.close()

print("dfdg")
#print(a)


'''
child= subprocess.Popen(["you-get", "--json", "http://www.acfun.cn/v/ac2111115"], stdout= subprocess.PIPE)
out= child.communicate()[0]
temp= str(out, encoding="UTF-8")
result= json.loads(temp)["streams"]["__default__"]["src"]
#subprocess.Popen.terminate()
print(result[0])
#child.wait()
'''