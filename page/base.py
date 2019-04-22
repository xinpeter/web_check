import urllib.request,time

c_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
try:
    urllib.request.urlopen("http://www.leyou999.com")

    print("%s 网站正常3" %c_time)
except Exception as e:
    print(e)