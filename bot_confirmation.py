#Изменено

import random
import telebot
from re import sub
bot = telebot.TeleBot('6327302177:AAEPZSxkjxxocz0weJKBWFPfOegKaHNfMcQ')

a = random.randint(0, 100)

salads = {
    'Греческий салат - 250 РУБ.\n': 250,
    'Овощной салат - 200 РУБ.\n': 200,
    'Цезарь салат - 275 РУБ.\n': 275
}

shaurma = {
    'Шаверма Сырная - 270 РУБ.\n': 270,
    'Шаверма Классическая - 245 РУБ.\n': 245,
    'Шаверма Веган - 220 РУБ.\n': 220,
    'Шаверма Деревенская - 290 РУБ.\n': 290,
    'АУФфф - 540 РУБ.\n': 540,
    'Шаверма Кавказская - 360 РУБ.\n': 360,
    'Шаверма Мини - 230 РУБ.\n': 230,
    'Шаверма Экзотика - 280 РУБ.\n': 280,
}

fustfood = {
    'Картошка фри - 190 РУБ.\n': 190,
    'Наггетсы - 290 РУБ.\n': 290,
    'Крылья - 290 РУБ.\n': 290,
    'Стрипсы - 290 РУБ.\n': 290,
    'Сырные палочки - 380 РУБ.\n': 380,
    'Луковые кольца - 170 РУБ.\n': 170
    
}
dener = {
    'Дёнер(курица) - 330 РУБ.\n': 330,
    'Дёнер(свинина) - 350 РУБ.\n': 350,
}

kebabs = {
    'Ассорти - 1950 РУБ.\n': 1950,
    'Свиной шашлык - 400 РУБ.\n': 400,
    'Куриный шашлык - 340 РУБ.\n': 340,
    'Картошка - 230 РУБ.\n': 230,
    'Овощной шашлык - 270 РУБ.\n': 270, 
    'Кебаб(курица) - 320 РУБ.\n': 320,
    'Кебаб(говядина) - 360 РУБ.\n': 360,
}

kebabs_for_lavash = [
    'Свиной шашлык - 400 РУБ.\n',
    'Куриный шашлык - 340 РУБ.\n',
    'Кебаб(курица) - 320 РУБ.\n',
    'Кебаб(говядина) - 360 РУБ.\n',
]

pancakes = {
    'Банан-нутелла-орех - 270 РУБ.\n': 270,
    'Блинчик с курицей - 270 РУБ.\n': 270,
    'Блинчик ветчина - 260 РУБ.\n': 260,
    'Карбонат - 310 РУБ.\n': 310,  
}
drinks = {
    'Вода(без газа) - 90 РУБ.\n': 90,
    'Вода(с газом) - 90 РУБ.\n': 90,
    'Burn оригинальный - 180 РУБ.\n': 180,
    'Добрый кола 0,3 - 110 РУБ.\n': 110,
    'Добрый сок(мультифрукт) - 90 РУБ.\n': 90,
    'Добрый кола 0,5 - 130 РУБ.\n': 130,
    'Морс брусничный 0,3 - 90 РУБ.\n': 90,
    'Pulpy 0,5 - 140 РУБ.\n': 140,
    'Rich 0,5 - 140 РУБ.\n': 140,
    'Pulpy 1л - 180 РУБ.\n': 180,
    'Добрый кола 1л - 165 РУБ.\n': 165,
}
additions = {
    'Курица - 30 РУБ.\n': 30,
    'Свинина - 40 РУБ.\n': 40,
    'Лук жареный - 15 РУБ.\n': 15,
    'Сыр - 35 РУБ.\n': 35,
    'Гранат - 30 РУБ.\n': 30,
    'Халапеньо - 20 РУБ.\n': 20,
    'Картошка - 20 РУБ.\n': 20,
    'Маринованные огурцы - 20 РУБ.\n': 20,
    'Грибы шампиньоны -  40 РУБ.\n': 40,
}
additions_d = {
    'курица - 30 РУБ.\n': 30,
    'свинина - 40 РУБ.\n': 40,
    'лук жареный - 15 РУБ.\n': 15,
    'сыр - 35 РУБ.\n': 35,
    'гранат - 30 РУБ.\n': 30,
    'халапеньо - 20 РУБ.\n': 20,
    'картошка - 20 РУБ.\n': 20,
    'маринованные огурцы - 20 РУБ.\n': 20,
    'грибы шампиньоны -  40 РУБ.\n': 40,
}


users_adres = {}
user_number = {}
user_time = {}
msgs_id = {}
carts = {}
total_dict = {}
cost_of_delivery = 250


# Генерация меню для всех типов блюд. food - параметр указывающий на словарь блюд
def generate_menu(food):
    keyboard = telebot.types.InlineKeyboardMarkup()
    for i in food:
        keyboard.add(telebot.types.InlineKeyboardButton(f'{i}', callback_data=i))
    return keyboard

def remove(list):
    pattern = '[\n,.]'
    list = [sub(pattern, '', i) for i in list]
    return list

def has_letter(s):
    return any(char.isalpha() for char in s)


# Start
@bot.message_handler(commands=['start'])
def send_hello(msg):
    bot_msg = bot.send_message(msg.chat.id, 'ПриУет✌\n Я Телеграм-Bot "АУФфф", созданный для того, чтобы ты, мой дорогой, покушал с кайфом🤪\n Я готов принять хотелки твоего животика, и максимально быстро их реализовать в жизнь😉\nНомер телефона администратора: +79041163611 \n +79500928672 \n\nФункции:\n/make_an_order - Сделать заказ\n/show_menu - Посмотреть меню\n/clean_cart - Очистить корзину\n/start - Начать')
    msgs_id[msg.from_user.id] = bot_msg.message_id

    
    
    
# Make an order (reply keyboard)
@bot.message_handler(commands=['make_an_order'])
def make_order(msg):
    kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add('Салаты 🥗', 'Шаурма 🌯', 'Фастфуд 🍟', 'Денер 🥪', 'Шашлык 🍖', 'Блины 🥞', 'Напитки 🥤' )
    bot.send_message(msg.chat.id, 'Выберите тип блюда', reply_markup=kb)

# Show menu (просмотр меню)
@bot.message_handler(commands=['show_menu'])
def show(msg):
    bot.send_media_group(msg.chat.id,  [telebot.types.InputMediaPhoto(open('img/шавуха 1.jpg', 'rb')), telebot.types.InputMediaPhoto(open('img/шашлыки.jpeg', 'rb')), telebot.types.InputMediaPhoto(open('img/фастфуд.jpeg', 'rb')), telebot.types.InputMediaPhoto(open('img/салатики 1.jpg', 'rb')), telebot.types.InputMediaPhoto(open('img/ допы 1.jpg', 'rb'))])

# Выбрать салат
@bot.message_handler(func=lambda call: call.text == 'Салаты 🥗')
def choice_salad(msg):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Выбрать салат', callback_data='choice_salad'))
    bot_msg = bot.send_message(msg.chat.id, 'Выберите салат', reply_markup=keyboard)
    msgs_id[msg.from_user.id] = bot_msg.message_id

# Список салатов в формате inline keyboard
@bot.callback_query_handler(func=lambda call: call.data == 'choice_salad')
def add_salad(call):
    keyboard = generate_menu(salads)
    bot.edit_message_text('Салаты:', call.message.chat.id, msgs_id[call.from_user.id], reply_markup=keyboard)

# Добавление салата в корзину
@bot.callback_query_handler(func=lambda call: call.data in salads)
def add_salad_in_cart(call):
    if call.from_user.id in carts:
        carts[call.from_user.id].append(call.data)
        total_dict[call.from_user.id].append(salads[call.data])
    else:
        carts[call.from_user.id] = [call.data]
        total_dict[call.from_user.id] = [salads[call.data]]
    user_cart = carts[call.from_user.id]
    text = ('Блюдо добавлено ✅\nКорзина:\n' + ' {} '*len(user_cart)).format(*user_cart) 
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Добавить ещё ➕', callback_data='choice_salad'))
    keyboard.add(telebot.types.InlineKeyboardButton('Оформить заказ 💸', callback_data='place_order'))
    bot.edit_message_text(f'{text}\n{sum(total_dict[call.from_user.id])} руб', call.message.chat.id, msgs_id[call.from_user.id], reply_markup=keyboard)



# Выбрвть шаурму
@bot.message_handler(func=lambda call: call.text == 'Шаурма 🌯')
def choice_shaurma(msg):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Выбрать шаурму', callback_data='choice_shaurma'))
    bot_msg = bot.send_message(msg.chat.id, 'Выберите шаурму', reply_markup=keyboard)
    msgs_id[msg.from_user.id] = bot_msg.message_id

# Список шаурмы в формате inline keyboard
@bot.callback_query_handler(func=lambda call: call.data == 'choice_shaurma')
def add_shaurma(call):
    keyboard = generate_menu(shaurma)
    bot.edit_message_text('Шаурма:', call.message.chat.id, msgs_id[call.from_user.id], reply_markup=keyboard)

    

# Добавление шаурмы в корзину
@bot.callback_query_handler(func=lambda call: call.data in shaurma)
def add_shaurma_in_cart(call):
    if call.from_user.id in carts:
        carts[call.from_user.id].append(call.data)
        total_dict[call.from_user.id].append(shaurma[call.data])
    else:
        carts[call.from_user.id] = [call.data]
        total_dict[call.from_user.id] = [shaurma[call.data]]
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Допы по кайфу 💪', callback_data='addit_yes'))
    keyboard.add(telebot.types.InlineKeyboardButton('Без допов 👎', callback_data='addit_no'))
    bot.send_message(call.message.chat.id, 'Хочешь допы по кайфу???', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'addit_yes')
def yes(call): 
    keyboard = generate_menu(additions)
    bot.send_message(call.message.chat.id, 'Допы:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data in additions)
def add_add(call):
    carts[call.from_user.id][-1] += f' + {call.data}'
    total_dict[call.from_user.id].append(additions[call.data])
    user_cart = carts[call.from_user.id]
    text = ('Блюдо добавлено ✅\nКорзина:\n' + ' {} '*len(user_cart)).format(*user_cart) 
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Добавить ещё ➕', callback_data='choice_shaurma'))
    keyboard.add(telebot.types.InlineKeyboardButton('Оформить заказ 💸', callback_data='place_order'))
    bot_msg = bot.send_message(call.message.chat.id, f'{text}\n{sum(total_dict[call.from_user.id])} руб', reply_markup=keyboard)
    msgs_id[call.from_user.id] = bot_msg.message_id

@bot.callback_query_handler(func=lambda call: call.data == 'addit_no')
def no(call):
    user_cart = carts[call.from_user.id]
    text = ('Блюдо добавлено ✅\nКорзина:\n' + ' {} '*len(user_cart)).format(*user_cart) 
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Добавить ещё ➕', callback_data='choice_shaurma'))
    keyboard.add(telebot.types.InlineKeyboardButton('Оформить заказ 💸', callback_data='place_order'))
    bot_msg = bot.send_message(call.message.chat.id, f'{text}\n{sum(total_dict[call.from_user.id])} руб', reply_markup=keyboard)
    msgs_id[call.from_user.id] = bot_msg.message_id




# Выбрвть dener
@bot.message_handler(func=lambda call: call.text == 'Денер 🥪')
def choice__dener(msg):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Выбрать блюдо', callback_data='a'))
    bot_msg = bot.send_message(msg.chat.id, 'Выберите блюдо', reply_markup=keyboard)
    msgs_id[msg.from_user.id] = bot_msg.message_id

# Список dener в формате inline keyboard
@bot.callback_query_handler(func=lambda call: call.data == 'a')
def add_dener(call):
    keyboard = generate_menu(dener)
    bot.edit_message_text('Денеры:', call.message.chat.id, msgs_id[call.from_user.id], reply_markup=keyboard)

# Добавление денера в корзину
@bot.callback_query_handler(func=lambda call: call.data in dener)
def add_dener_in_cart(call):
    if call.from_user.id in carts:
        carts[call.from_user.id].append(call.data)
        total_dict[call.from_user.id].append(dener[call.data])
    else:
        carts[call.from_user.id] = [call.data]
        total_dict[call.from_user.id] = [dener[call.data]]
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Допы по кайфу 💪', callback_data='d_addit_yes'))
    keyboard.add(telebot.types.InlineKeyboardButton('Без допов 👎', callback_data='d_addit_no'))
    bot.send_message(call.message.chat.id, 'Хочешь допы по кайфу???', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'd_addit_yes')
def dnr_yes(call): 
    keyboard = generate_menu(additions_d)
    bot.send_message(call.message.chat.id, 'Допы:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data in additions_d)
def add_add(call):
    carts[call.from_user.id][-1] += f' + {call.data}'
    total_dict[call.from_user.id].append(additions_d[call.data])
    user_cart = carts[call.from_user.id]
    text = ('Блюдо добавлено ✅\nКорзина:\n' + ' {} '*len(user_cart)).format(*user_cart) 
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Добавить ещё ➕', callback_data='a'))
    keyboard.add(telebot.types.InlineKeyboardButton('Оформить заказ 💸', callback_data='place_order'))
    bot_msg = bot.send_message(call.message.chat.id, f'{text}\n{sum(total_dict[call.from_user.id])} руб', reply_markup=keyboard)
    msgs_id[call.from_user.id] = bot_msg.message_id

@bot.callback_query_handler(func=lambda call: call.data == 'd_addit_no')
def dnr_no(call):
    user_cart = carts[call.from_user.id]
    text = ('Блюдо добавлено ✅\nКорзина:\n' + ' {} '*len(user_cart)).format(*user_cart) 
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Добавить ещё ➕', callback_data='a'))
    keyboard.add(telebot.types.InlineKeyboardButton('Оформить заказ 💸', callback_data='place_order'))
    bot_msg = bot.send_message(call.message.chat.id, f'{text}\n{sum(total_dict[call.from_user.id])} руб', reply_markup=keyboard)
    msgs_id[call.from_user.id] = bot_msg.message_id



# Выбрвть фастфуд
@bot.message_handler(func=lambda call: call.text == 'Фастфуд 🍟')
def choice_fustfood(msg):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Выбрать блюдо', callback_data='choice_fustfood'))
    bot_msg = bot.send_message(msg.chat.id, 'Выберите блюдо', reply_markup=keyboard)
    msgs_id[msg.from_user.id] = bot_msg.message_id

# Список фастфуда в формате inline keyboard
@bot.callback_query_handler(func=lambda call: call.data == 'choice_fustfood')
def add_fustfood(call):
    keyboard = generate_menu(fustfood)
    bot.edit_message_text('Фастфуд:', call.message.chat.id, msgs_id[call.from_user.id], reply_markup=keyboard)

# Добавление фастфуда в корзину
@bot.callback_query_handler(func=lambda call: call.data in fustfood)
def add_fustfood_in_cart(call):
    if call.from_user.id in carts:
        carts[call.from_user.id].append(call.data)
        total_dict[call.from_user.id].append(fustfood[call.data])
    else:
        carts[call.from_user.id] = [call.data]
        total_dict[call.from_user.id] = [fustfood[call.data]]
    user_cart = carts[call.from_user.id]
    text = ('Блюдо добавлено ✅\nКорзина:\n' + ' {} '*len(user_cart)).format(*user_cart) 
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Добавить ещё ➕', callback_data='choice_fustfood'))
    keyboard.add(telebot.types.InlineKeyboardButton('Оформить заказ 💸', callback_data='place_order'))
    bot.edit_message_text(f'{text}\n{sum(total_dict[call.from_user.id])} руб', call.message.chat.id, msgs_id[call.from_user.id], reply_markup=keyboard)



# Выбрвть шашлык
@bot.message_handler(func=lambda call: call.text == 'Шашлык 🍖')
def choice_kebabs(msg):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Выбрать блюдо', callback_data='choice_kebabs'))
    bot_msg = bot.send_message(msg.chat.id, 'Выберите блюдо', reply_markup=keyboard)
    msgs_id[msg.from_user.id] = bot_msg.message_id

# Список шашлык в формате inline keyboard
@bot.callback_query_handler(func=lambda call: call.data == 'choice_kebabs')
def add_kebabs(call):
    keyboard = generate_menu(kebabs)
    bot.edit_message_text('Шашлык:', call.message.chat.id, msgs_id[call.from_user.id], reply_markup=keyboard)

# Добавление шашлык в корзину
@bot.callback_query_handler(func=lambda call: call.data in kebabs)
def add_kebabs_in_cart(call):
    if call.from_user.id in carts:
        carts[call.from_user.id].append(call.data)
        total_dict[call.from_user.id].append(kebabs[call.data])
    else:
        carts[call.from_user.id] = [call.data]
        total_dict[call.from_user.id] = [kebabs[call.data]]
    
    if call.data in kebabs_for_lavash:
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton('Да 💪', callback_data='lavash_yes'))
        keyboard.add(telebot.types.InlineKeyboardButton('Нет 👎', callback_data='lavash_no'))
        bot.send_message(call.message.chat.id, 'Завернуть в лавашик???', reply_markup=keyboard)
    else:
        user_cart = carts[call.from_user.id]
        text = ('Блюдо добавлено ✅\nКорзина:\n' + ' {} '*len(user_cart)).format(*user_cart) 
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton('Добавить ещё ➕', callback_data='choice_kebabs'))
        keyboard.add(telebot.types.InlineKeyboardButton('Оформить заказ 💸', callback_data='place_order'))
        bot.edit_message_text(f'{text}\n{sum(total_dict[call.from_user.id])} руб', call.message.chat.id, msgs_id[call.from_user.id], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'lavash_yes')
def warm_up_kebab(call):
    carts[call.from_user.id][-1] += ' + лаваш - 25 руб\n'
    total_dict[call.from_user.id].append(25)
    user_cart = carts[call.from_user.id]
    text = ('Блюдо добавлено ✅\nКорзина:\n' + ' {} '*len(user_cart)).format(*user_cart) 
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Добавить ещё ➕', callback_data='choice_kebabs'))
    keyboard.add(telebot.types.InlineKeyboardButton('Оформить заказ 💸', callback_data='place_order'))
    bot_msg = bot.send_message(call.message.chat.id, f'{text}\n{sum(total_dict[call.from_user.id])} руб', reply_markup=keyboard)
    msgs_id[call.from_user.id] = bot_msg.message_id


@bot.callback_query_handler(func=lambda call: call.data == 'lavash_no')
def no(call):
    user_cart = carts[call.from_user.id]
    text = ('Блюдо добавлено ✅\nКорзина:\n' + ' {} '*len(user_cart)).format(*user_cart) 
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Добавить ещё ➕', callback_data='choice_kebabs'))
    keyboard.add(telebot.types.InlineKeyboardButton('Оформить заказ 💸', callback_data='place_order'))
    bot_msg = bot.send_message(call.message.chat.id, f'{text}\n{sum(total_dict[call.from_user.id])} руб', reply_markup=keyboard)
    msgs_id[call.from_user.id] = bot_msg.message_id



#Добавление блинов
@bot.message_handler(func=lambda call: call.text == 'Блины 🥞')
def choice_pancakes(msg):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Выбрать блюдо', callback_data='choice_pancakes'))
    bot_msg = bot.send_message(msg.chat.id, 'Выберите блюдо', reply_markup=keyboard)
    msgs_id[msg.from_user.id] = bot_msg.message_id
 
# Список блинов в формате inline keyboard 
@bot.callback_query_handler(func=lambda call: call.data == 'choice_pancakes') 
def add_pancakes(call): 
    keyboard = generate_menu(pancakes) 
    bot.edit_message_text('Блины:', call.message.chat.id, msgs_id[call.from_user.id], reply_markup=keyboard)
 
# Добавление блина в корзину 
@bot.callback_query_handler(func=lambda call: call.data in pancakes) 
def add_pancakes_in_cart(call): 
    if call.from_user.id in carts: 
        carts[call.from_user.id].append(call.data) 
        total_dict[call.from_user.id].append(pancakes[call.data]) 
    else: 
        carts[call.from_user.id] = [call.data] 
        total_dict[call.from_user.id] = [pancakes[call.data]] 
    user_cart = carts[call.from_user.id] 
    text = ('Блюдо добавлено ✅\nКорзина:\n' + ' {} '*len(user_cart)).format(*user_cart)  
    keyboard = telebot.types.InlineKeyboardMarkup() 
    keyboard.add(telebot.types.InlineKeyboardButton('Добавить ещё ➕', callback_data='choice_pancakes')) 
    keyboard.add(telebot.types.InlineKeyboardButton('Оформить заказ 💸', callback_data='place_order')) 
    bot.edit_message_text(f'{text}\n{sum(total_dict[call.from_user.id])} руб', call.message.chat.id, msgs_id[call.from_user.id], reply_markup=keyboard)



 # Выбрвть напиток 
@bot.message_handler(func=lambda call: call.text == 'Напитки 🥤') 
def choice_drink(msg): 
    keyboard = telebot.types.InlineKeyboardMarkup() 
    keyboard.add(telebot.types.InlineKeyboardButton('Выбрать блюдо', callback_data='choice_drink')) 
    bot_msg = bot.send_message(msg.chat.id, 'Выберите блюдо', reply_markup=keyboard) 
    msgs_id[msg.from_user.id] = bot_msg.message_id 
 
# Список напитка в формате inline keyboard 
@bot.callback_query_handler(func=lambda call: call.data == 'choice_drink') 
def add_drink(call): 
    keyboard = generate_menu(drinks) 
    bot.edit_message_text('Напитки:', call.message.chat.id, msgs_id[call.from_user.id], reply_markup=keyboard) 
 
# Добавление напитка в корзину 
@bot.callback_query_handler(func=lambda call: call.data in drinks) 
def add_drink_in_cart(call): 
    if call.from_user.id in carts: 
        carts[call.from_user.id].append(call.data) 
        total_dict[call.from_user.id].append(drinks[call.data]) 
    else: 
        carts[call.from_user.id] = [call.data] 
        total_dict[call.from_user.id] = [drinks[call.data]] 
    user_cart = carts[call.from_user.id] 
    text = ('Блюдо добавлено ✅\nКорзина:\n' + ' {} '*len(user_cart)).format(*user_cart)  
    keyboard = telebot.types.InlineKeyboardMarkup() 
    keyboard.add(telebot.types.InlineKeyboardButton('Добавить ещё ➕', callback_data='choice_drink')) 
    keyboard.add(telebot.types.InlineKeyboardButton('Оформить заказ 💸', callback_data='place_order')) 
    bot.edit_message_text(f'{text}\n{sum(total_dict[call.from_user.id])} руб', call.message.chat.id, msgs_id[call.from_user.id], reply_markup=keyboard)



@bot.message_handler(commands=['gif'])
def send_пасхалка(msg):
    bot.send_animation(msg.chat.id, 'https://media1.tenor.com/m/LTcVMiH7lyUAAAAd/burrito.gif')


# Очистка корзины
@bot.message_handler(commands=['clean_cart'])
def clean(msg):
    try:
        del carts[msg.from_user.id]
        del total_dict[msg.from_user.id]
        bot.send_message(msg.chat.id, 'Корзина пуста🗑')
    except KeyError:
        bot.send_message(msg.chat.id, 'Корзина пуста🗑')



@bot.callback_query_handler(func=lambda call: call.data == 'place_order')
def pl_or(call):
        bot.send_message(call.message.chat.id, 'Укажите номер телефона☎\n\nПример: 89998887766')



@bot.callback_query_handler(func=lambda call: call.data == 'correct_number')
def plac_or(call):
        bot.send_message(call.message.chat.id, 'Укажите время получения заказа\n\nПример: 22:10')



@bot.callback_query_handler(func=lambda call: call.data == 'deliver_order')
def plc_order(call):
    bot.send_message(call.message.chat.id, 'Укажите адрес доставки🏡')

@bot.message_handler(content_types=['text'])
def p(msg):
    if has_letter(msg.text):
            keyboard = telebot.types.InlineKeyboardMarkup()
            keyboard.add(telebot.types.InlineKeyboardButton('Адрес верный ✅', callback_data='final_delivery_confirm'))
            keyboard.add(telebot.types.InlineKeyboardButton('Ввести адрес заново 🔄', callback_data='deliver_order'))
            users_adres[msg.from_user.id] = msg.text
            bot_msg = bot.send_message(msg.chat.id, f'Адрес введён верно?\n{msg.text}', reply_markup=keyboard)
            msgs_id[msg.from_user.id] = bot_msg.text

    elif ':' in msg.text:
            keyboard = telebot.types.InlineKeyboardMarkup()
            keyboard.add(telebot.types.InlineKeyboardButton('Да ✅', callback_data='correct_time'))
            keyboard.add(telebot.types.InlineKeyboardButton('Ввести время заново 🔄', callback_data='correct_number'))
            user_time[msg.from_user.id] = msg.text
            bot_msg = bot.send_message(msg.chat.id, f'Время верное?\n{msg.text}', reply_markup=keyboard)
            msgs_id[msg.from_user.id] = bot_msg.text

    else:
            if len(msg.text) == 11:
                keyboard = telebot.types.InlineKeyboardMarkup()
                keyboard.add(telebot.types.InlineKeyboardButton('Номер верный ✅', callback_data='correct_number'))
                keyboard.add(telebot.types.InlineKeyboardButton('Ввести номер заново 🔄', callback_data='place_order'))
                user_number[msg.from_user.id] = msg.text
                bot_msg = bot.send_message(msg.chat.id, f'Номер телефона введён верно?\n{msg.text}', reply_markup=keyboard)
                msgs_id[msg.from_user.id] = bot_msg.text
            else:
                bot.send_message(msg.chat.id, 'Номер телефона введён некорректно')

@bot.callback_query_handler(func=lambda call: call.data == 'correct_time')
def pick_or_deliv(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Доставка🛵', callback_data='deliver_order'))
    keyboard.add(telebot.types.InlineKeyboardButton('Самовывоз👣', callback_data='pickup_confirm'))
    bot.send_message(call.message.chat.id, 'Как хотите получить заказ?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'final_delivery_confirm')
def confirmation_delivery(call):
    output_cart = "\n".join(i for i in remove(carts[call.from_user.id]))
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Подтвердить', callback_data='final_delivery'))
    keyboard.add(telebot.types.InlineKeyboardButton('Изменить способ получения', callback_data='correct_time_for_del'))
    bot.send_message(call.message.chat.id, f'Ваш заказ:\n\n{output_cart}\n\nСумма - {sum(total_dict[call.from_user.id])} руб.\n\nОчистить корзину - /clean_cart', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'correct_time_for_del')
def pick_or_deliv(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Доставка🛵', callback_data='final_delivery'))
    keyboard.add(telebot.types.InlineKeyboardButton('Самовывоз👣', callback_data='pickup_confirm'))
    bot.send_message(call.message.chat.id, 'Как хотите получить заказ?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'final_delivery')
def send_order_deliver(call): 
    output_cart = "\n".join(i for i in remove(carts[call.from_user.id]))
    bot.send_message(call.message.chat.id, f'адресок - {users_adres[call.from_user.id]}\n\nВаш заказ принят✔\nС вас {sum(total_dict[call.from_user.id])} руб\n(Cумма доставки рассчитывается по тарифам службы такси, оплата при получении заказа водителю)\n\nРеквизиты для оплаты заказа💳:\n5559 4941 1913 5704 - Альфабанк\n+7(950)092-86-72 - Альфабанк\nПолучатель - Марянян Василий Межлумович\n\nОжидайте звонка администратора, в течении 10 минут!📞')
    # bot.send_message(1177901865 , f'Способ получения - доставка\nНомер телефона - {user_number[call.from_user.id]}\nАдрес доставки - {users_adres[call.from_user.id]}\n\n{output_cart}\n\nСумма - {sum(total_dict[call.from_user.id])} руб.\n\nВремя - {user_time[call.from_user.id]}')
    # bot.send_message(6549580182 , f'Способ получения - доставка\nНомер телефона - {user_number[call.from_user.id]}\nАдрес доставки - {users_adres[call.from_user.id]}\n\n{output_cart}\n\nСумма - {sum(total_dict[call.from_user.id])} руб.\n\nВремя - {user_time[call.from_user.id]}')
    # bot.send_message(7106453907 , f'Способ получения - доставка\nНомер телефона - {user_number[call.from_user.id]}\nАдрес доставки - {users_adres[call.from_user.id]}\n\n{output_cart}\n\nСумма - {sum(total_dict[call.from_user.id])} руб.\n\nВремя - {user_time[call.from_user.id]}')
    # bot.send_message(879086748, f'Способ получения - доставка\nНомер телефона - {user_number[call.from_user.id]}\nАдрес доставки - {users_adres[call.from_user.id]}\n\n{output_cart}\n\nСумма - {sum(total_dict[call.from_user.id])} руб.\n\nВремя - {user_time[call.from_user.id]}')

    del carts[call.from_user.id]
    del total_dict[call.from_user.id]



@bot.callback_query_handler(func=lambda call: call.data == 'pickup_confirm')
def confirmation_delivery(call):
    output_cart = "\n".join(i for i in remove(carts[call.from_user.id]))
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Подтвердить', callback_data='pickup'))
    keyboard.add(telebot.types.InlineKeyboardButton('Изменить способ получения', callback_data='correct_time'))
    bot.send_message(call.message.chat.id, f'Ваш заказ:\n\n{output_cart}\n\nСумма - {sum(total_dict[call.from_user.id])} руб.\n\nОчистить корзину - /clean_cart', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'pickup')
def send_order_pickup(call):
    output_cart = "\n".join(i for i in remove(carts[call.from_user.id]))
    bot.send_message(call.message.chat.id, f'Ваш заказ принят✔\nС вас {int(sum(total_dict[call.from_user.id]))} руб\n\nОплата переводом! 💸\nРеквизиты для оплаты заказа💳:\n5559 4941 1913 5704 - Альфабанк\n+7(950)092-86-72 - Альфабанк\nПолучатель - Марянян Василий Межлумович\n\nОжидайте звонка администратора, в течении 10 минут!📞')
    # bot.send_message(1177901865 , f'Способ получения - самовывоз\nНомер телефона - {user_number[call.from_user.id]}\nСумма - {int(sum(total_dict[call.from_user.id]))} руб.\n\n{output_cart}\n\nВремя - {user_time[call.from_user.id]}')
    # bot.send_message(6549580182 , f'Способ получения - самовывоз\nНомер телефона - {user_number[call.from_user.id]}\nСумма - {int(sum(total_dict[call.from_user.id]))} руб.\n\n{output_cart}\n\nВремя - {user_time[call.from_user.id]}')
    # bot.send_message(7106453907 , f'Способ получения - самовывоз\nНомер телефона - {user_number[call.from_user.id]}\nСумма - {int(sum(total_dict[call.from_user.id]))} руб.\n\n{output_cart}\n\nВремя - {user_time[call.from_user.id]}')
    # bot.send_message(879086748 , f'Способ получения - самовывоз\nНомер телефона - {user_number[call.from_user.id]}\nСумма - {int(sum(total_dict[call.from_user.id]))} руб.\n\n{output_cart}\n\nВремя - {user_time[call.from_user.id]}')

    carts.pop(call.from_user.id)
    total_dict.pop(call.from_user.id)


if __name__ == '__main__':
    bot.infinity_polling() 