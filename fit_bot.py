from random import choice
 
import telebot
from telebot import types
import webbrowser
 
token = '579:AAEGRFSL2fcp7wq3yo19E'
 
bot = telebot.TeleBot(token)
 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('C:\python\olya.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
        # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Тренировки для развития гибкости")
    item2 = types.KeyboardButton("😊 Укрепление мышц и похудение")
    item3 = types.KeyboardButton("😊 Тренировки для плоского живота")
    item4 = types.KeyboardButton("😊 Гибкая спина и осанка")
    item5 = types.KeyboardButton("😊 Зарядка или разминка")
    item6 = types.KeyboardButton("😊 Вечерние релакс тренировки")
    item7 = types.KeyboardButton("😊 Гибкость ног / шпагаты")
 
    markup.add(item1, item2, item3, item4, item5, item6, item7)
 
    bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот Ольги Илющихиной. Я могу вам прислать тренировку или полезную статью. Для этого выбирайте раздел в меню ниже".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Тренировки для развития гибкости':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Динамическая растяжка", url="https://www.youtube.com/watch?v=f70zfPjFxu0")
            item2 = types.InlineKeyboardButton("Мобилизация суставов", url="https://www.youtube.com/watch?v=3KHB1aBbrPY")
            item3 = types.InlineKeyboardButton("Упражнения для гибкой спины", url="https://www.youtube.com/watch?v=JzvHAtOdfRc")
            item4 = types.InlineKeyboardButton("🔥АКТИВНАЯ ГИБКОСТЬ НОГ🔥", url="https://www.youtube.com/watch?v=FQPnZoZ1hjg")
            item5 = types.InlineKeyboardButton("👍РАСТЯЖКА ДЛЯ НАЧИНАЮЩИХ🧡", url="https://www.youtube.com/watch?v=MIFCKXBzx38")
            item6 = types.InlineKeyboardButton("РАСТЯЖКА НА КАЖДЫЙ ДЕНЬ", url="https://www.youtube.com/watch?v=uMrne5kPlo4")
            item7 = types.InlineKeyboardButton("ГИБКИЕ И СИЛЬНЫЕ НОГИ", url="https://www.youtube.com/watch?v=T0FzzcUTZTk")
            item8 = types.InlineKeyboardButton("ДЛЯ ГИБКОСТИ НОГ", url="https://www.youtube.com/watch?v=8fDsXwCzMYo")
            item9 = types.InlineKeyboardButton("Как научиться делать складку", url="https://www.youtube.com/watch?v=AYa5szE4qKY")
            item10 = types.InlineKeyboardButton("МЯГКАЯ РАСТЯЖКА на все тело", url="https://www.youtube.com/watch?v=I6bZahgy2f4")
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
 
            bot.send_message(message.chat.id, 'Выберите видео из предложенных ниже.', reply_markup=markup)
       
        elif message.text == '😊 Укрепление мышц и похудение':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("ЭФФЕКТИВНОЕ ПОХУДЕНИЕ🔥", url="https://www.youtube.com/watch?v=SEK9B4mqQ3I")
            item2 = types.InlineKeyboardButton("Комплекс упражнений для тонуса мышц", url="https://www.youtube.com/watch?v=jVU7T8Cyoic")
            item3 = types.InlineKeyboardButton("КАК УКРЕПИТЬ СПИНУ👍", url="https://www.youtube.com/watch?v=JP6GwZ7DyWg")
            item4 = types.InlineKeyboardButton("ТРЕНИРОВКА ДЛЯ CТРОЙНОСТИ🔥", url="https://www.youtube.com/watch?v=8cOECR_ljMI")
            item5 = types.InlineKeyboardButton("👯КАК УБРАТЬ ЖИВОТ И БОКА 🧘🏻‍♀️", url="https://www.youtube.com/watch?v=XuFACDoEios")
            item6 = types.InlineKeyboardButton("Красивые ягодицы дома", url="https://www.youtube.com/watch?v=HWTBeaKP400")
            item7 = types.InlineKeyboardButton("Укрепляем РУКИ, СПИНУ и ПРЕСС", url="https://www.youtube.com/watch?v=znh5Nu86yE0")
            item8 = types.InlineKeyboardButton("Упражнения для похудения", url="https://www.youtube.com/watch?v=sNHZNzKzYHA")
            item9 = types.InlineKeyboardButton("Лучшие упражнения на пресс", url="https://www.youtube.com/watch?v=oooL5kvTA8Y")
           
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
 
            bot.send_message(message.chat.id, 'Выберите видео из предложенных ниже.', reply_markup=markup)
        elif message.text == '😊 Тренировки для плоского живота':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("👯КАК УБРАТЬ ЖИВОТ И БОКА 🧘🏻‍♀️", url="https://www.youtube.com/watch?v=XuFACDoEios")
            item2 = types.InlineKeyboardButton("Упражнение для пресса", url="https://www.youtube.com/watch?v=5EUOXBCedRs")
            item3 = types.InlineKeyboardButton("Упражнения для похудения", url="https://www.youtube.com/watch?v=sNHZNzKzYHA")
            item4 = types.InlineKeyboardButton("упражнения для пресса спины", url="https://www.youtube.com/watch?v=Aza1F_NeeXQ")
            item5 = types.InlineKeyboardButton("Упражнения для женского здоровья", url="https://www.youtube.com/watch?v=sl05UccO-4k")
 
            markup.add(item1, item2, item3, item4, item5)
 
            bot.send_message(message.chat.id, 'Выберите видео из предложенных ниже.', reply_markup=markup)
        elif message.text == '😊 Гибкая спина и осанка':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Здоровая спина", url="https://www.youtube.com/watch?v=Qtnw9kdGMWo")
            item2 = types.InlineKeyboardButton("Как избавиться от сутулости", url="https://www.youtube.com/watch?v=ij3jI5Lag4g")
            item3 = types.InlineKeyboardButton("Упражнения для гибкой спины🐆", url="https://www.youtube.com/watch?v=JzvHAtOdfRc")
            item4 = types.InlineKeyboardButton("КАК УКРЕПИТЬ СПИНУ👍", url="https://www.youtube.com/watch?v=JP6GwZ7DyWg")
            item5 = types.InlineKeyboardButton("🧘🏻‍♀️ПИЛАТЕС ДЛЯ СПИНЫ🌷", url="https://www.youtube.com/watch?v=_X_O0YDtR5k")
            item6 = types.InlineKeyboardButton("Как избавиться от боли в спине", url="https://www.youtube.com/watch?v=FJ9BbZ0GGaE")
            item7 = types.InlineKeyboardButton("Снимаем напряжение с шеи", url="https://www.youtube.com/watch?v=2utf3QxYC1g")
            item8 = types.InlineKeyboardButton("Улучшаем подвижность позвоночника", url="https://www.youtube.com/watch?v=p5_oB-0Ils0")
            item9 = types.InlineKeyboardButton("Офисная разминка", url="https://www.youtube.com/watch?v=kQr6fWJOiAY")
            item10 = types.InlineKeyboardButton("Упражнения для расслабления", url="https://www.youtube.com/watch?v=hYcYH80HbWQ")
            item11 = types.InlineKeyboardButton("УПРАЖНЕНИЯ ДЛЯ ГИБКОЙ СПИНЫ", url="https://www.youtube.com/watch?v=XcofGG73Il0")
            item12 = types.InlineKeyboardButton("Учимся делать мостик", url="https://www.youtube.com/watch?v=TWLXQkf0-yQ")
            item13 = types.InlineKeyboardButton("Упражнения для осанки дома", url="https://www.youtube.com/watch?v=Ga2BbAXwX3Y")
            item14 = types.InlineKeyboardButton("Лучшие упражнения для СПИНЫ", url="https://www.youtube.com/watch?v=gH7pwKtwP08")
            item15 = types.InlineKeyboardButton("Эффективные упражнения для спины", url="https://www.youtube.com/watch?v=Aza1F_NeeXQ")
 
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15)
 
            bot.send_message(message.chat.id, 'Выберите видео из предложенных ниже.', reply_markup=markup)
        elif message.text == '😊 Зарядка или разминка':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Зарядка для бодрости", url="https://www.youtube.com/watch?v=iymvyC9zF-4")
            item2 = types.InlineKeyboardButton("☕️Утренняя зарядка⚡️", url="https://www.youtube.com/watch?v=JYQXAjzddvc")
            item3 = types.InlineKeyboardButton("Мобилизация суставов", url="https://www.youtube.com/watch?v=uMrne5kPlo4")
            item4 = types.InlineKeyboardButton("Зарядка 13 минут", url="https://www.youtube.com/watch?v=zlxg8OFFlyk")
            item5 = types.InlineKeyboardButton("Простая быстрая разминка⚡️", url="https://www.youtube.com/watch?v=hZYx4n_zy_M")
            item6 = types.InlineKeyboardButton("Бодрая зарядка на каждый день", url="https://www.youtube.com/watch?v=1yPL-KZeZPU")
 
            markup.add(item1, item2, item3, item4, item5, item6)
 
            bot.send_message(message.chat.id, 'Выберите видео из предложенных ниже.', reply_markup=markup)
        elif message.text == '😊 Вечерние релакс тренировки':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Избавляемся от стресса", url="https://www.youtube.com/watch?v=G6XO8C5DzDE")
            item2 = types.InlineKeyboardButton("Снимаем напряжение с шеи", url="https://www.youtube.com/watch?v=2utf3QxYC1g")
            item3 = types.InlineKeyboardButton("Упражнения для расслабления", url="https://www.youtube.com/watch?v=hYcYH80HbWQ")
            item4 = types.InlineKeyboardButton("МЯГКАЯ РАСТЯЖКА на все тело", url="https://www.youtube.com/watch?v=I6bZahgy2f4")
            item5 = types.InlineKeyboardButton("Растяжка для расслабления", url="https://www.youtube.com/watch?v=7HqS11Q6cCU")
            item6 = types.InlineKeyboardButton("Лучшая вечерняя тренировка", url="https://www.youtube.com/watch?v=WSFBTgoxL6E")
 
            markup.add(item1, item2, item3, item4, item5, item6)
 
            bot.send_message(message.chat.id, 'Выберите видео из предложенных ниже.', reply_markup=markup)            
        elif message.text == '😊 Гибкость ног / шпагаты':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("10 минут ПОПЕРЕЧНЫЙ ШПАГАТ", url="https://www.youtube.com/watch?v=XcOvjgiH1D8")
            item2 = types.InlineKeyboardButton("Тренировка для гибкости ног🤸🏻‍♂️", url="https://www.youtube.com/watch?v=QAUwtK6bgm0")
            item3 = types.InlineKeyboardButton("Растяжка ног | Продольный шпагат", url="https://www.youtube.com/watch?v=RjU_JdqIhu8")
 
            markup.add(item1, item2, item3)
 
            bot.send_message(message.chat.id, 'Выберите видео из предложенных ниже.', reply_markup=markup)                    
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')  

bot.polling(none_stop=True)
