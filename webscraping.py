import requests
import bs4

def webscrape(webURL):
    URL = webURL
    page = requests.get(URL, headers = {"User-Agent":"Undefined"})
    soup = bs4.BeautifulSoup(page.content,"html.parser")
    try:
        priceInfo = soup.find(id="priceblock_saleprice").get_text()
    except:
        try: priceInfo = soup.find(id="priceblock_ourprice").get_text()
        except:
            print("Olete sisestanud vale URLi, proovige uuesti")
    return (priceInfo)
