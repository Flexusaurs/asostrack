from flask import Flask, request
import requests
from bs4 import BeautifulSoup
import boto3
import telebot
import os

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('product_prices_table')

@app.route('/' + os.getenv('TELEGRAM_TOKEN'), methods=['POST'])
def receive_update():
    data = request.json
