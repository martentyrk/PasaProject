from emailSendLogic import emailSender
from UI import userInterface
from webscraping import webscrape

webURL = input("Sisestage Amazoni lehe toote URL, mida soovite lisada hinnavaatlusesse: ")
userEmail = input("Sisestage enda emaili aadress: ")

prices = []
while True:
    productInfo = webscrape(webURL)
#Should be a save mechanic, appending all prices to list and checking the difference
#between the 2 last items

    if productInfo["price"] not in prices:
        prices.append(productInfo["price"])
        subject = ("Price checker notification!")

        #Checking below if there even exists a previous price
        if len(prices) >= 2:
            previousPrice = prices[-2]
            currentPrice = prices[-1]
            #Creating a body for the email message to present
            priceTitle = "You have added {0} to the price checker from PASA and the price has changed.".format(productInfo["title"])

            availability = "Product availability:{0}".format(productInfo["availability"])

            body = "The previous price for the product you wanted to check was {0} and the new price is {1}".format(previousPrice,currentPrice)
            ending = "All the best,\n PASA"
            #All info separated by category and added to textForBody
            textForBody = priceTitle,"\n",availability,"\n",body,"\n",ending
            emailSender(subject,textForBody,userEmail)



