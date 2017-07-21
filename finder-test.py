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

# GETTING THE PRODUCT LIST ON CURRYS

print "|--- ON CURRYS ---|"
for prodList in soupC.find("ul", class_="product-listing").find_all("li"):

    # # IMAGEM
    # for prodImg in soupC.find("div", class_="product-image").find("a"):
    #     print prodImg

    # TITULO
    for prodTitle in prodList.soupC.find("div", class_="product-details").find("a"):
        prodTitle = prodTitle.replace('  ','').replace('\n', '')
        print "|- " + prodTitle

    # # LINK
    # for prodLink in soupC.find("div", class_="product-details").find("a"):
    #     type(prodLink.attrs)
    #     print prodLink.attrs['href']

    # # PRICE
    # for prodPrice in soupC.find("div", class_="product-pricing").find("span", class_="productFamilyPriceValue"):
    #     prodPrice = prodPrice.replace(',', 'a').replace('.', 'a')
    #     prodPrice = sub('[^a-zA-Z0-9_-]', '', prodPrice)
    #     prodPrice = prodPrice.replace('a', ',').replace('a', '.')
    #     print "|- " + prodPrice + " euros"
