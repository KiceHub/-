# 校园集结号体温上报
基于python2.7，需要抓包，并配合云函数每天定时上报

思路：请求登录获取accesstoken，然后上报。

需要抓包url：

(登录时抓取)https://auth.xiaoyuanjijiehao.com/oauth2/token

(上报时抓取)https://h5api.xiaoyuanjijiehao.com/api/staff/interface

推荐抓包软件HttpCanary，记得安装ssl证书
