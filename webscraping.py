import requests
import bs4
import time

#translator for amazon.de availability
def germanTranslator(word):
    if word == "Auf lager.":
        word = "In stock."
    elif word == "Derzeit nicht verfügbar.":
        word = "Currently unavailable"
    elif word == "In Kürze verfügbar":
        word = "Available soon"
    return word


def webscrape(URL):
    productInfo = {}
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15"}
    existenceChecker = requests.get(URL)
    if existenceChecker.status_code == 200:
        page = requests.get(URL,headers=headers)

        time.sleep(2)
        soup = bs4.BeautifulSoup(page.content, "html.parser")
        time.sleep(5)
        #added time.sleep so that we would not be recognized as robots
        productTitle = soup.find(id="productTitle").get_text().strip()
        productAvailability = soup.find(id="availability").get_text().strip()
        #getting product title and availability status
        #trying different id tags because different products have different ids depending on sale
        try:
            productPrice = soup.find(id="priceblock_ourprice").get_text()
        except:

            try:
                productPrice = soup.find(id="priceblock_dealprice").get_text()

            except:
                return("Sisestatud URL millel puudub hind.")

        #adding all the needed info to productInfo
        productAvailability = germanTranslator(productAvailability)
        productInfo["availability"] = productAvailability
        productInfo["price"] = productPrice
        productInfo["title"] = productTitle
        return productInfo

    else: return "Sellist URLi ei eksisteeri"