from bs4 import BeautifulSoup
import urllib.request

url_top_level_domain = "http://m.kukudm.com"
url_bleach_home_page = "http://m.kukudm.com/comiclist/6/"
UA_iphone_6p= "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4"

url_req = urllib.request.Request(url_bleach_home_page)
url_req.add_header("User-Agent",UA_iphone_6p)

html_home_page = urllib.request.urlopen(url_req)

bs = BeautifulSoup(html_home_page,"html.parser")

#lst = bs.find("div",{"class":"classopen"}).children
lst = bs.find("div",{"class":"classopen"}).find_all("li")

print(type(lst))
for c in lst:
    print("Episode url is %s%s" % (url_top_level_domain , c.find("a").get("href")), " , title is: %s" %  c.find("a").string)












