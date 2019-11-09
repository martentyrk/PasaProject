from emailSendLogic import emailSender
from UI import userInterface
from webscraping import webscrape

webURL = input("Sisestage Amazoni lehe toote URL, mida soovite lisada hinnavaatlusesse: ")
userEmail = input("Sisestage enda emaili aadress: ")

prices = []

while True:
    currentPrice = webscrape(webURL)

#Should be a save mechanic, appending all prices to list and checking the difference
#between the 2 last items

    if currentPrice not in prices:
        prices.append(webscrape(webURL))
        subject = ("Price checker notification!")
#Checking if there even exists a previous price
        if len(prices) >= 2:
            previousPrice = prices[-2]
            currentPrice = prices[-1]
            body = "The previous price for the product you wanted to check was {0} and the new price is {1}".format(previousPrice,currentPrice)
            emailSender(subject,body,userEmail)



