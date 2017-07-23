import mysql.connector

database = "182.254.230.24"

conn = mysql.connector.connect(host=database, user='fleeter', passwd='hust201417', port=3306, charset='utf8',
                               database='fleeting')
cur = conn.cursor()

add_names = 'SELECT * from fl_video '
cur.execute(add_names)
data = cur.fetchone()
for v in data:
    print(v)

cur.close()
conn.close()
