import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = "https://www.zomato.com/bangalore/voosh-thalis-bowls-1-bellandur-bangalore/order"

page = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(page.content, 'html.parser')

names = []
prices = []
descriptions = []
mustTryTag = []

foods = soup.find_all('div', class_="sc-1s0saks-17 bGrnCu")
for food in foods:
    name = food.find('h4').get_text()
    price = food.find('span').get_text()[1:]
    price = int(price)
    description = food.find('p').get_text()
    try:
        mustTry = food.find('div', class_="sc-2gamf4-0 cRxPpO").get_text()
    except:
        mustTry = None

    names.append(name)
    prices.append(price)
    descriptions.append(description)
    mustTryTag.append(mustTry)

data = pd.DataFrame({
    "NAME": names,
    "PRICE": prices,
    "DESCRIPTION": descriptions,
    "MUST_TRY_TAG": mustTryTag
})

data.to_csv('foods_data.csv')
    

    


