import requests
from bs4 import BeautifulSoup
import boto3
import env 
from datetime import datetime
import time
import telegram from telegram

dynamodb = boto3.resource('')
table = ()

headers = {
    'authority': 'www.asos.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'user-agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4159.2 Safari/537.36',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': link,
    'accept-language': 'en-US,en;q=0.9'
}


 