import cookielib
import urllib2

url = "http://www.baidu.com"

#first
print "fisrt: directly request by url"
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

# second
print "second: use request and set user-agent by Request"
request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

# third
print "third: use Handler to adapt different enviroment."
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
print response3.read()