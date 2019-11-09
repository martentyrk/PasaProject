import requests
import bs4
import time
def webscrape(URL):
    productInfo = {}
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15"}

    page = requests.get(URL,headers=headers)

    time.sleep(2)
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    time.sleep(5)
    productTitle = soup.find(id="productTitle").get_text()
    try:
        productPrice = soup.find(id="priceblock_ourprice").get_text()
    except:
        try: productPrice = soup.find(id="priceblock_dealprice").get_text()

        except: return("Sisestatud vale hind")
    productInfo["price"] = productPrice
    productInfo["title"] = productTitle.strip()
    return productInfo