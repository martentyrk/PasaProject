import requests
import bs4

URL = "https://www.amazon.de/Bloodborne-Game-Year-PlayStation-4/dp/B016ZU4FIQ/ref=sr_1_3?ie=UTF8&qid=1519566642&sr=8-3&keywords=bloodborne+ps4"
page = requests.get(URL,headers={"User-Agent":"Defined"})
soup = bs4.BeautifulSoup(page.content, "html.parser")
price = soup.find(id="priceblock_ourprice").get_text()
print(price)

