import time
def getHeader():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    }
    return headers

def getUrl(page, cateId):
    url = 'https://s.search.bilibili.com/cate/search?'
    params = {
        # 'callback': 'jqueryCallback_bili_6172376022260306',
        'main_ver': 'v3',
        'search_type': 'video',
        'view_type': 'hot_rank',
        'order': 'click',
        'copy_right': '1',
        'cate_id': str(cateId),
        'page': '1',
        'pagesize': '20',
        'jsonp': 'jsonp',
        'time_from': '20191114',
        'time_to': '20200114',
        '_': '1578904199459'
    }
    params['page'] = str(page)

    query = ''
    for key in params:
        query = query+key+'='+params[key]+'&'
    return url+query

def getFields():
    fields = [
        'senddate',
        'rank_offset',
        'tag',
        'duration',
        'comic_id',
        'rank_score',
        'badgepay',
        'pubdate',
        'title',
        'review',
        'mid',
        'is_union_video',
        'rank_index',
        'type',
        'arcrank',
        'play',
        'pic',
        'description',
        'video_review',
        'is_pay',
        'favorites',
        'arcurl',
        'author',
        'cate_id'
    ]
    return fields