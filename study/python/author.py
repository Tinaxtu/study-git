import urllib.request
import pymysql
import math
import json
import header
import time

# DB
db = pymysql.connect('127.0.0.1', 'root', '123456', 'test')
cursor = db.cursor()

# page number
sqlCount = "SELECT count(*) FROM author"
cursor.execute(sqlCount)
result  = cursor.fetchone()
numPage = math.ceil(result[0]/20)

# request header
headers = header.getHeader()

# log
log = open('./author.log', 'a+')

for i in range(0, numPage):
    sqlSelect = "SELECT * FROM author LIMIT "+str(i*20)+","+str(20)
    cursor.execute(sqlSelect)
    resLists = cursor.fetchall()
    
    for item in resLists:
        mid = str(item[1])
        url = 'http://api.bilibili.com/x/relation/stat?vmid='+mid+'&jsonp=jsonp'
        req = urllib.request.Request(url=url, headers=headers)
        try:
            rep   = urllib.request.urlopen(req, timeout=5)
            html  = rep.read().decode('UTF-8')
            datas = json.loads(html)
            follower = datas['data']['follower']

            sqlUpdate = "UPDATE author SET follower=%s WHERE id=%s"
            params    = (follower, item[0])
            cursor.execute(sqlUpdate, params)
            db.commit()

            msg = mid+" "+item[2]+" get follower: " + str(follower)
            print(msg)
        except:
            msg = mid+" author mid get failed\n"
            print(msg)
            log.write(msg)
    time.sleep(0.2)
print("success all")


# INSERT INTO author(mid,name)SELECT DISTINCT(mid),author FROM comicVideo;
