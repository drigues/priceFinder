from bs4 import BeautifulSoup
import requests
# SYS.EXIT
import sys
# REPACE CHARACTERES
from re import sub


print "|---------------------------------------------------|"
print "|--- Find the best deal between CURRYS and ARGOS ---|"
print "|---------------------------------------------------|"
keyWorld = raw_input("|- Search for an eletronic product: ")
print "|---------------------------------------------------|"
print "|"
kw1 = keyWorld
kw2 = keyWorld

if keyWorld == "exit":
    sys.exit()

if ' ' in keyWorld:
    kw1 = keyWorld.replace(' ','-')
    kw2 = keyWorld.replace(' ','+')

urlCurrys = "http://www.currys.ie/action/searchsite/" + kw1
urlArgos = "http://www.argos.ie/webapp/wcs/stores/servlet/Search?storeId=10152&catalogId=14551&langId=111&searchTerms="+ kw2

onCurrys = requests.get(urlCurrys)
onArgos = requests.get(urlArgos)

dataCurrys = onCurrys.text
soupC = BeautifulSoup(dataCurrys, "html.parser")
dataArgos = onArgos.text
soupA = BeautifulSoup(dataArgos, "html.parser")

# GETTING THE PRODUCT NAME ON CURRYS

i = 0
nameProdList = []
print "|--- ON CURRYS ---|"
for nameList in soupC.find_all("div", class_="product-details"):
    for nameItem in nameList.find("a"):
        nameItem = nameItem.replace('  ','').replace('\n', '')
        nameProdList[i] = nameItem
        print i
        i += 1
        print i

j = 0
priceProdList = []
for priceList in soupC.find_all("div", class_="product-pricing"):
    for priceFull in priceList.find_all("div", class_="Topleft"):
        for priceC in priceFull.find("span"):
            priceC = priceC.replace(',', 'a').replace('.', 'a')
            priceC = sub('[^a-zA-Z0-9_-]', '', priceC)
            priceC = priceC.replace('a', ',').replace('a', '.')
            priceProdList[j] = priceC

for idx, item in enumerate(nameProdList):
    print item[idx]
    print item
    print idx
    print nameProdList

print "|"

# GETTING THE PRODUCT PRICE

for name in soupA.find_all(id="listerrhs").find_all("h4", class_="description").find_all("a"):
    name = name.replace('.','')
    print "|--- ON ARGOS ---|"
    print "|- " + name

for priceA in soupA.find_all_all("li", class_="pricing").find_all("li", class_="price"):
    priceA = priceA.replace(',', 'a').replace('.', 'a')
    priceA = sub('[^a-zA-Z0-9_-]', '', priceA)
    priceA = priceA.replace('a', ',').replace('a', '.')
    print "|- Price: "+priceA+" euros"

print "|"

# GETTING THE CHEAPEST

if priceA > priceC:
    print "|- THE BEST PRICE IS ON CURRYS!!"
else:
    print "|- THE BEST PRICE IS ON ARGOS!!"

print "|"
