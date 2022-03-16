import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
import csv
def soup(url):
    thepage=urllib.request.urlopen(url)
    soupdata=BeautifulSoup(thepage,"html.parser")
    thepage.close()
    return soupdata
def get_details(url):
 soup1=soup(url)
 edata=""
 details1=""
 for i in soup1.findAll("div",{"id" : "ppd"}):
   for j in i.findAll("div",{ "id" : "centerCol"}):
        for k in j.findAll("div",{"id":"title_feature_div"}):
            for l in k.findAll("span",{"id":"productTitle"}):
             title=l.text.replace(",","..")
        for r1 in j.findAll("div",{"id":"featurebullets_feature_div"}):
            for r2 in r1.findAll("ul", {"class": "a-unordered-list a-vertical a-spacing-mini"}):
                for s1 in r2.findAll("span",{"class":"a-list-item"}):
                  detaile=s1.text.replace("\n","")
                  details1+=detaile
        for r3 in j.findAll("div",{"id":"apex_desktop"}):
          for r4 in r3.findAll("span",{"class":"a-offscreen"}):
                        price=r4.text.replace(",","")
   for a in i.findAll("div",{"id":"leftCol"}):
     for b in a.findAll('div',{"id":"imgTagWrapperId"}):
        for c in b.findAll("img")  :
           img=(c['src'])

 data=title+","+img+","+price+","+details1
 edata=edata+"\n"+data
 print(edata)
 header="Product Title,Product Image URL,Price of the Product,Product Details"
 file=open(os.path.expanduser("sample.csv"),"wb")
 file.write(bytes (header,encoding="ascii", errors="ignore"))
 file.write(bytes (edata, encoding="ascii", errors="ignore"))
url=["https://www.amazon.com/Neon-City-Godzilla-Funko-1015/dp/B08ZCV5434"]
for i in url:
    get_details(i)