import requests
import bs4

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


    soup = bs4.BeautifulSoup(page.content, "html5lib")

    # added time.sleep so that we would not be recognized as robots

#Amazoni kohta webscrape
    if "amazon" in URL:
        try:
            productTitle = soup.find(id="productTitle").get_text().strip()
        except:
            try:
                productTitle = soup.find(id="productTitle").get_text().strip()
            except:
                productTitle = " "

        try:
            productAvailability = soup.find(id="productAvailability").get_text.strip()
        except:
            try:
                productAvailability = soup.find("p", class_="a-spacing-micro a-color-secondary a-text-bold").text.strip()
            except:
                productAvailability = ""

        # getting product productTitle and productAvailability status
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

        return(productInfo)

#Ebay scanner
    if "ebay" in URL:
        #getting the productTitle and removing a small part from it.
        try:
            h1 = soup.find("h1", id="itemTitle").find("span").get_text()
            productTitle = soup.find("h1", id="itemTitle").get_text()
            if h1 in productTitle:
                productTitle = productTitle.replace(h1,"")
                productInfo["title"] = productTitle
            else:
                productInfo["title"] = productTitle
        except:
            productInfo["title"] = " "

        #getting item productPrice
        try:
            productPrice = soup.find("span", id="prcIsum").text
            productInfo["price"] = productPrice
        except:
            try:
                productPrice = soup.find("span", id="mm-saleDscPrc").text
                productInfo["price"] = productPrice

            except:
                productInfo["price"] = " "

        #getting the productAvailability
        try:
            productAvailability = soup.find("span", id="qtySubTxt").get_text().strip()
            productInfo["availability"] = productAvailability
        except:
            productInfo["availability"] = " "

        return(productInfo)

    else:
        return("Please use an amazon or ebay website")

