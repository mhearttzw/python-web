import subprocess
import json
import requests
import mysql.connector

# Connect the database
database = "182.254.230.24"
conn = mysql.connector.connect(host=database, user='fleeter', passwd='hust201417', port=3306, charset='utf8',
                               database='fleeting')
cur = conn.cursor()

# Choose type TODO: Add more types and urls
video_type_url = {"娱乐": "http://www.acfun.cn/rank.aspx?channelId=60&range=1&count=30&ext=1&date=",
                  "动画短片": "http://www.acfun.cn/rank.aspx?channelId=106&range=3&count=30&ext=1&date=",
                  "音乐": "http://www.acfun.cn/rank.aspx?channelId=137&range=1&count=30&ext=1&date="
                  }
# Insert video information into the database
for type_video in video_type_url:
    # Get response
    req_url = video_type_url[type_video]
    res1 = requests.get(req_url)
    res = res1.json()
    for i in range(len(res)):
        print(type_video, ": ", i)

        url_video = "http://www.acfun.cn" + res[i]['url']
        child = subprocess.Popen(["you-get", "--json", url_video], stdout=subprocess.PIPE)
        out = child.communicate()[0]
        temp = str(out, encoding="UTF-8")
        try:
            url = json.loads(temp)["streams"]["__default__"]["src"]
        except:
            continue

        size = int(json.loads(temp)["streams"]["__default__"]["size"] / 1024/1024)
        title = res[i]['title']
        description = res[i]['description']
        cover = res[i]['titleImg']
        temp = [str(title), str(cover), str(description), str(url[0]), str(size), type_video]
        add_values = (str(title), str(cover), str(description), str(url[0]), str(size), str(type_video))

        add_names = ('INSERT INTO fl_video (title, cover, description, url, size, type) '
                     'VALUES (%s,%s,%s,%s,%s,%s)')
        cur.execute(add_names, add_values)
# Make sure data is committed to the database
conn.commit()
cur.close()
conn.close()

# Unused information
'''
subprocess.Popen.terminate()
>> > isinstance(['d', 'd'], str)
>> > isinstance(['d', 'd'], list)
time
ISOTIMEFORMAT = '%Y-%m-%d %X'
upload_time= time.strftime(ISOTIMEFORMAT, time.localtime())
'''
