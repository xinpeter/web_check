import urllib.request,time,pytest

class Test_url:
    def test_url(self):
        c_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            data = urloolib.request.urlopen("http://www.leyou999.com")
            print("%s 网站正常3" % c_time)
            assert True
        except Exception as e:
            print(e)
            assert False

