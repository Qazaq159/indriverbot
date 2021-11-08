import asyncio
import requests
from aiogram import Bot, types

API_TOKEN = '2021796476:AAHFBze12f2JJs_NcCYF3A68n_OQPXeK3Mo'
CHANNEL_ID = '408100714' # это должен быть int, например -1006666666666

def sendd(API_TOKEN):
    url = f' https://api.telegram.org/bot{API_TOKEN}/getUpdates'
    response = requests.get(url)
    return response.json()

response = sendd(API_TOKEN)
print(response)