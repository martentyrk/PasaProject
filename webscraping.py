import requests
import bs4

URL = "https://www.amazon.co.uk/dp/B07XRC3BBG/ref=dp_cerb_1"
page = requests.get(URL, headers = {"User-Agent":"Undefined"})
soup = bs4.BeautifulSoup(page.content,"html.parser")
priceInfo = soup.find(id="priceblock_saleprice").get_text()
print(priceInfo)