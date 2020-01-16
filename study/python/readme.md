一 说明：
1 scratch.py为抓取B站分类“动画”下按视频热度排序、原创、且发布时间为最新两个月的列表数据
2 author.py为抓取up主的粉丝数量
以上均有API

二 需要安装
1 python版本3.5
2 pymysql模块

pip安装问题，需要做镜像处理：
阿里云 [mirrors.aliyun.com/pypi/simple…](https://mirrors.aliyun.com/pypi/simple/)
中国科技大学 [pypi.mirrors.ustc.edu.cn/simple/](https://pypi.mirrors.ustc.edu.cn/simple/)
豆瓣(douban) [pypi.douban.com/simple/](https://pypi.douban.com/simple/)
清华大学 [pypi.tuna.tsinghua.edu.cn/simple/](https://pypi.tuna.tsinghua.edu.cn/simple/)
中国科学技术大学 [pypi.mirrors.ustc.edu.cn/simple/](http://pypi.mirrors.ustc.edu.cn/simple/)

经过实践，阿里云的可以
命令操作为：
pip install beautifulsoup4 -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
pip install -i https://mirrors.aliyun.com/pypi/simple/ pymysql

BILIBILI API
https://www.bilibili.com/read/cv3430609/
https://zhuanlan.zhihu.com/p/24581605