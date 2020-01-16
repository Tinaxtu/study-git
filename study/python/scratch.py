import urllib.request
import time
import pymysql
import math
import header
import json
import time

headers   = header.getHeader()
fieldList = header.getFields()
fields    = ','.join(fieldList)
binds     = '%s,'*len(fieldList) # 参数占位
log       = open('./error.log', 'a+') # 日志记录
binds     = binds[0:-1]
# 24-动画(MAD.AMV) 27-动画(综合) 168-国创(国产原创相关)
cates     = [24, 27, 168] 

db = pymysql.connect('127.0.0.1', 'root', '123456', 'test')
cursor = db.cursor()

for cateId in cates:
    curPage = 1
    count   = 0
    while True:
        url = header.getUrl(curPage, cateId)
        req = urllib.request.Request(url=url, headers=headers)

        try:
            rep   = urllib.request.urlopen(req, timeout=5)
            html  = rep.read().decode('UTF-8')
            datas = json.loads(html)

            if( curPage==1 ):
                totalPage = datas['numPages'] # 后续可能会变
            lists = datas['result']

            for item in lists:
                count = count+1
                item['badgepay'] = 0 if(item['badgepay']==False) else 1 # python无三元操作
                sqlInsert = "INSERT INTO comicVideo("+fields+")VALUES("+binds+")"
                posts = (
                    item['senddate'], item['rank_offset'], item['tag'], item['duration'], item['id'], item['rank_score'], 
                    item['badgepay'], item['pubdate'], item['title'], item['review'], item['mid'], item['is_union_video'], item['rank_index'], 
                    item['type'], item['arcrank'], item['play'], item['pic'], item['description'], item['video_review'], item['is_pay'], 
                    item['favorites'], item['arcurl'], item['author'], cateId) # 元组形式

                try:
                    cursor.execute(sqlInsert, posts)
                    db.commit()
                    msg = str(totalPage)+" "+str(curPage)+" "+str(count)+" comic ID "+str(item['id'])+" success\n"
                    print(msg)
                    log.write(msg)
                except:
                    db.rollback()
                    msg = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+" "+str(totalPage)+" "+str(curPage)+" "+str(count)+" comic ID "+str(item['id'])+" failed\n"
                    log.write(msg)
            curPage = curPage+1
        except urllib.error.URLError as e:
            errorMsg = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+" page "+str(curPage)+" request error\n"
            log.write(errorMsg)
        
        time.sleep(0.1) # 时间间隔
        if( curPage>totalPage ):
            log.write("curPage:"+str(curPage)+",totalPage:"+str(totalPage))
            log.write("over "+str(cateId)+'\n'+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+'\n')
            break
print("success")

