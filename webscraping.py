import requests
import bs4
import time
import html5lib


# translator for amazon.de availability
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
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}
    existenceChecker = requests.get(URL)

    page = requests.get(URL, headers=headers)
    print(page)
    time.sleep(2)
    soup = bs4.BeautifulSoup(page.content, "html5lib")


    #comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    time.sleep(5)
    # added time.sleep so that we would not be recognized as robots

    productTitle = soup.find(id="productTitle").get_text().strip()


    productAvailability = soup.find(id="availability").get_text().strip()
    # getting product title and availability status
    # trying different id tags because different products have different ids depending on sale
    try:
        productPrice = soup.find(id="priceblock_ourprice").get_text()
    except:
        try:
            productPrice = soup.find(id="priceblock_dealprice").get_text()

        except:
            return ("Sisestatud URL millel puudub hind.")
    # adding all the needed info to productInfo
    productAvailability = germanTranslator(productAvailability)
    productInfo["availability"] = productAvailability
    productInfo["price"] = productPrice
    productInfo["title"] = productTitle
    return productInfo
