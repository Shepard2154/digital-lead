import os
import json
import requests

import telebot
from dotenv import load_dotenv
from loguru import logger


load_dotenv(".env")

bot = telebot.TeleBot(os.getenv("MY_KEY"))
BACKEND = os.getenv("BACKEND_URL")
users_last_message_address_id = dict()


def catch_backend_off(func):
    ''' 
    Декоратор для определения ошибок доступа к беку.
    Использовать ДО декоратора catch_user.
    '''
    def decor(message):
        try: 
            func(message)
        except Exception as e:
            bot.reply_to(message, 'Извините, на этом сервер все...')
            logger.error(e)
    return decor


def catch_user(func):
    ''' 
    Декоратор для определения пользователя.
    Handler должен принимать message, user. 
    Использовать ПОСЛЕ декоратора telebot'а
    '''
    def decor(message):
        from_user = message.from_user
        user = {
            'id': from_user.id,
            'firstname': from_user.first_name,
            'lastname': from_user.last_name
        }
        return func(message, user)
    return decor


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Добрый день! Бот по приему жалоб готов вам помочь!")

@bot.message_handler(func=lambda message: True)
@catch_backend_off
@catch_user
def send_welcome(message, user):
    ''' Принимаем текстовые сообщения '''
    r = requests.post(
        f'{BACKEND}message/create/',
        json = {
            'text': message.text,
            'author_id': user,
            'addr': {}
    })
    response = json.loads(r.content)
    cl = response.get("event_class")
    users_last_message_address_id[user.get('id')] = response.get("address")
    if cl == "D": cl = "Дтп"
    elif cl == "F": cl = "Пожар"
    elif cl == "WS": cl = "Нарушение водоснабжения"
    elif cl == "T": cl = "Мусор"
    elif cl == "L": cl = "Сбой электросети"
    elif cl == "LR": cl = "Загрязнение водоемов"
    elif cl == "R": cl = "Дороги"
    bot.reply_to(message, f'Ваше сообщение класса: {cl}\nПринято!\n\nПожалуйста, напишите адрес или прикрепите геопозицию!')


@bot.message_handler(content_types=['location'])
@catch_backend_off
@catch_user
def location_processing(message, user):
    ''' Принимаем геолокацию '''
    location = message.location
    r = requests.put(
        f'{BACKEND}message/address/{users_last_message_address_id.get(user.get("id"))}/',
        json = {
            'latitude': location.latitude,
            'longtitude': location.longitude
    })
    bot.reply_to(message, 'Ваше заявление принято, оператор свяжется с вами в ближайшее время')
    

@bot.message_handler(content_types=['venue'])
@catch_backend_off
@catch_user
def venue_processing(message, user):
    ''' Принимаем место '''
    place = message.venue
    address = place.address
    location = place.location
    r = requests.put(
        f'{BACKEND}message/address/{users_last_message_address_id.get(user.get("id"))}/',
        json = {
            'latitude': location.latitude,
            'longtitude': location.longitude,
            'text': address
    })
    bot.reply_to(message, 'Ваше заявление принято, оператор свяжется с вами в ближайшее время')


@bot.message_handler(content_types=['photo'])
@catch_backend_off
@catch_user
def photo_processing(message, user):
    ''' Принимаем фото '''
    fileID = message.photo[-1].file_id
    file = bot.get_file(fileID)
    to_send = bot.download_file(file.file_path)
    headers = {
        'cache-control': "no-cache",
        'Content-Disposition': 'attachment; filename=example.txt'
    }
    file = {
        'file': to_send
    }
    r = requests.post(f'{BACKEND}message/photo/', headers=headers, files=file)
    response = json.loads(r.content)
    cl = response.get("event_class")
    users_last_message_address_id[user.get('id')] = response.get("address")
    if cl == "D": cl = "Дтп"
    elif cl == "F": cl = "Пожар"
    elif cl == "WS": cl = "Нарушение водоснабжения"
    elif cl == "T": cl = "Мусор"
    elif cl == "L": cl = "Сбой электросети"
    elif cl == "LR": cl = "Загрязнение водоемов"
    elif cl == "R": cl = "Дороги"
    bot.reply_to(message, f'Ваше сообщение класса: {cl}\nПринято!\n\nПожалуйста, напишите адрес или прикрепите геопозицию!')


bot.polling()
