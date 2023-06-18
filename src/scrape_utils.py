import requests
from bs4 import BeautifulSoup
import json
from dotenv import load_dotenv
import os
from datetime import datetime
import time

def scrape(link: str, currency = "ILS"):
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser").find("script", type="application/ld+json")
    product_data = json.loads(soup.string)
    print(product_data["name"], product_data["color"], product_data["productID"])
    #price_endpoint = f"https://www.asos.com/api/product/catalogue/v3/stockprice?productIds={product_data['productID']}&store=ROW&currency={currency}"
    price_api = f"https://api.asos.com/product/catalogue/v3/stockprice?productIds={product_data['productID']}&store=ROW&currency={str(currency)}"
    print(requests.get(price_api, headers=headers).json()[0]["productPrice"]["current"]["text"], requests.get(price_api, headers=headers).json()[0]["discountPercentage"])
#link = "https://www.asos.com/tommy-jeans/tommy-jeans-chest-luxe-logo-t-shirt-in-black/prd/204291070?colourWayId=204291073&cid=50580"

if __name__ == "__main__":
    scrape("https://www.asos.com/reclaimed-vintage/reclaimed-vintage-swim-shorts-in-short-length-in-blue-paisely-print/prd/204266239?colourWayId=204266240&cid=13210", currency="ILS")
    