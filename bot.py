import telebot
import random
from telebot import types
import os
import time
import csv

vakmestprog = int(25) # количество вакантых мест в программировании
vakmest3d = int(25) # количество вакантых мест в 3д моделировании
vakmestel = int(25) # количество вакантых мест в электроннике
vakmestrob = int(25) # количество вакантых мест в робототехнике

spisokprog = r"C:\Users\Admin\Desktop\семихатовский хакатон\списки\списки программирование.txt" # путь на txt с списком на программирование
spisok3d = r"C:\Users\Admin\Desktop\семихатовский хакатон\списки\списки 3D моделирование.txt" # путь на txt с списком на 3D моделирование
spisokel = r"C:\Users\Admin\Desktop\семихатовский хакатон\списки\списки электронника.txt" # путь на txt с списком на электронника
spisokrob = r"C:\Users\Admin\Desktop\семихатовский хакатон\списки\списки робототехника.txt" # путь на txt с списком на робототехника
fotosog = r"C:\Users\Admin\Desktop\семихатовский хакатон\списки\photo" #путь на папку с согласиями

tokenlink = r"C:\Users\Admin\Desktop\семихатовский хакатон\token.txt" #путь на токен бота


# Создаем бота
with open(tokenlink, 'r') as f:
    token = f.read()
bot = telebot.TeleBot(token)
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        #Начальные кнопки 
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("📆Актуальные курсы")
        item2=types.KeyboardButton("💼Загрузка документов")
        item3=types.KeyboardButton("🏢Информация об организации")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(m.chat.id, 'Здравствуйте. Это Телеграмм бот, для взаимодействия с Лабораторией робототехники и 3D моделирования Космопорт.\n \nИспользуя бота Вы можете:\nполучать актуальную информацию о курсах,\nзагружать необходимые документы своего ребёнка, записываться на заинтересующие вас курсы.\n \nДля продолжения нажмите на одну из кнопок 👇',  reply_markup=markup)
#Получение сообщений
@bot.message_handler(content_types=["text"])
def handle_text(message):
    #Актуальные курсы
    if message.text.strip() == '📆Актуальные курсы' :
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True) 
        item4=types.KeyboardButton("👨‍💻Программирование") 
        item5=types.KeyboardButton("🗽3D моделирование") 
        item6=types.KeyboardButton("🕹Электроника") 
        item7=types.KeyboardButton("⚙️Робототехника") 
        item8=types.KeyboardButton("⬅️ Назад") 
        markup.add(item4) 
        markup.add(item5) 
        markup.add(item6) 
        markup.add(item7) 
        markup.add(item8) 
        bot.send_message(message.chat.id, '👨‍💻Программирование — курсы по обучению программирования на языке Python\n \n🗽3D моделирование — курсы по обучению 3D моделированию в программе Blender\n \n🕹Электроника — курсы по работе с электроникой и микроконтроллером Arduino\n \n⚙️Робототехника — курсы по созданию роботов на микроконтроллере Arduino\n \n⬅️Назад — вернуться в главное меню  ',  reply_markup=markup)
    # Если выбрали программирование
    if message.text.strip() == "👨‍💻Программирование":
          markup=types.ReplyKeyboardMarkup(resize_keyboard=True)  
          item20=types.KeyboardButton("👨‍💻 Записаться")
          item21=types.KeyboardButton("⬅️ Назад") 
          markup.add(item20) 
          markup.add(item21) 
          bot.send_message(message.chat.id, 'Занятия по программированию на языке Python. Группа №1.\nВремя проведения: пятница, 11:30-13:00.\nМесто проведения: Луначарского 136, Станция технического творчества Космопорт, Большой зал.\n \nДля записи нажмите кнопку "Записаться"',  reply_markup=markup)
            
    if message.text.strip() == '👨‍💻 Записаться':
            def save_link(message):
                my_link = message.text
                bot.send_message(message.chat.id, 'Отлично. Загрузите необходимые документы во вкладке "Загрузка документов".')
                dict1 = my_link
                str1 = str(dict1)
                with open(spisokprog, mode="a") as file:
    # Записываем содержимое переменной в файл и добавляем символ новой строки (\n)
                   file.write(str1 + "\n")
                
                with open(spisokprog, 'r') as file:
                   lines = file.readlines()
                   vakmestcountprog = vakmestprog - len(lines)
                   print(vakmestcountprog)
                   if vakmestcountprog < 1:
                           bot.send_message(message.chat.id, 'По направлению достигнуто максимальное кол-во обучающихся учащихся. Вы записаны в резерв.')
                    
                print(my_link)
               
                 
                                                 
            print("Новый лог от",message.from_user.username)
            print("--------------------------------------------------------------")
            print(message.text) 
            sent = bot.send_message(message.chat.id, "Введите ФИО ребёнка:")
            bot.register_next_step_handler(sent, save_link)
           
            
            
            
            
    if message.text.strip() == "🗽3D моделирование":
          markup=types.ReplyKeyboardMarkup(resize_keyboard=True)  
          item20=types.KeyboardButton("🗽 Записаться")
          item21=types.KeyboardButton("⬅️ Назад") 
          markup.add(item20) 
          markup.add(item21) 
          bot.send_message(message.chat.id, 'Занятия по 3D моделированию. Группа №1\nВремя проведения: среда, 15:30-17:30.\nМесто проведения: Луначарского 136, Станция технического творчества Космопорт, Большой зал.\n \nДля записи нажмите кнопку "Записаться"',  reply_markup=markup)
            
    if message.text.strip() == '🗽 Записаться': 
            def save_link(message):
                my_link = message.text
                bot.send_message(message.chat.id, 'Отлично. Загрузите необходимые документы во вкладке "Загрузка документов".')
                dict1 = my_link
                str1 = str(dict1)
                with open(spisok3d, mode="a") as file:
    # Записываем содержимое переменной в файл и добавляем символ новой строки (\n)
                   file.write(str1 + "\n")
                
                with open(spisok3d, 'r') as file:
                   lines = file.readlines()
                   vakmestcount3d = vakmest3d - len(lines)
                   print(vakmestcount3d)
                   if vakmestcount3d < 1:
                           bot.send_message(message.chat.id, 'По направлению достигнуто максимальное кол-во обучающихся учащихся. Вы записаны в резерв.')
                print(my_link)
                      
                                                 
            print("Новый лог от",message.from_user.username)
            print("--------------------------------------------------------------")
            print(message.text) 
            sent = bot.send_message(message.chat.id, "Введите ФИО ребёнка:")
            bot.register_next_step_handler(sent, save_link)
            
    #Если выбрали Электроника
    if message.text.strip() == "🕹Электроника":
          markup=types.ReplyKeyboardMarkup(resize_keyboard=True)  
          item20=types.KeyboardButton("🕹 Записаться")
          item21=types.KeyboardButton("⬅️ Назад") 
          markup.add(item20) 
          markup.add(item21) 
          bot.send_message(message.chat.id, 'Занятия по работе с электроникой. Группа №1.\nВремя проведения: четверг, 15:30-17:30.\nМесто проведения: Луначарского 136, Станция технического творчества Космопорт, Паялка.\n \nДля записи нажмите кнопку "Записаться"',  reply_markup=markup)
            
    if message.text.strip() == '🕹 Записаться': 
            def save_link(message):
                my_link = message.text
                bot.send_message(message.chat.id, 'Отлично. Загрузите необходимые документы во вкладке "Загрузка документов".')
                dict1 = my_link
                str1 = str(dict1)
                with open(spisokel, mode="a") as file:
    # Записываем содержимое переменной в файл и добавляем символ новой строки (\n)
                   file.write(str1 + "\n")
                
                with open(spisokel, 'r') as file:
                   lines = file.readlines()
                   vakmestcountel = vakmestel - len(lines)
                   print(vakmestcountel)
                   if vakmestcountel < 1:
                           bot.send_message(message.chat.id, 'По направлению достигнуто максимальное кол-во обучающихся учащихся. Вы записаны в резерв.')                   
                print(my_link)
                      
                                                 
            print("Новый лог от",message.from_user.username)
            print("--------------------------------------------------------------")
            print(message.text) 
            sent = bot.send_message(message.chat.id, "Введите ФИО ребёнка:")
            bot.register_next_step_handler(sent, save_link)
            
    #Если выбрали Робототехника
    if message.text.strip() == "⚙️Робототехника":
          markup=types.ReplyKeyboardMarkup(resize_keyboard=True)  
          item20=types.KeyboardButton("⚙ Записаться")
          item21=types.KeyboardButton("⬅️ Назад") 
          markup.add(item20) 
          markup.add(item21) 
          bot.send_message(message.chat.id, 'Занятия по работе с микроконтроллером Arduino. Группа №1.\nВремя проведения: пятница, 09:30-11:00.\nМесто проведения: Луначарского 136, Станция технического творчества Космопорт, Большой зал.\n \nДля записи нажмите кнопку "Записаться"',  reply_markup=markup)
            
    if message.text.strip() == '⚙ Записаться': 
            def save_link(message):
                my_link = message.text
                bot.send_message(message.chat.id, 'Отлично. Загрузите необходимые документы во вкладке "Загрузка документов".')
                dict1 = my_link
                str1 = str(dict1)
                with open(spisokrob, mode="a") as file:
    # Записываем содержимое переменной в файл и добавляем символ новой строки (\n)
                   file.write(str1 + "\n")
                
                with open(spisokrob, 'r') as file:
                   lines = file.readlines()
                   vakmestcounrob = vakmestrob - len(lines)
                   print(vakmestcounrob)
                   if vakmestcountrob < 1:
                           bot.send_message(message.chat.id, 'По направлению достигнуто максимальное кол-во обучающихся учащихся. Вы записаны в резерв.')                   
                print(my_link)
                      
                                                 
            print("Новый лог от",message.from_user.username)
            print("--------------------------------------------------------------")
            print(message.text) 
            sent = bot.send_message(message.chat.id, "Введите ФИО ребёнка:")
            bot.register_next_step_handler(sent, save_link)
            
            
    if message.text.strip() == '💼Загрузка документов':
            markup=types.ReplyKeyboardRemove()
    #Загрузка доков
    if message.text.strip() == '💼Загрузка документов':
            
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True) 
             

            def save_link1(message):
                bot.send_message(message.chat.id, "Ниже загрузите согласия на зачисление и обработку персональных данных.")
                
                
                @bot.message_handler(content_types=['photo'])
                def handle_docs_document(message):
                    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
                    downloaded_file = bot.download_file(file_info.file_path)
                    src = fotosog + message.photo[1].file_id
                    
                    with open(src, 'wb') as new_file:
                      new_file.write(downloaded_file)
                      
                      
                      bot.reply_to(message, "Фото добавлено")
                      
                      item9=types.KeyboardButton("Робототехника") 
                      markup.add(item9)
                      
                      new_file.close()
                      
                                                 
            print("Новый лог от",message.from_user.username)
            print("--------------------------------------------------------------")
            print(message.text) 
            sent = bot.send_message(message.chat.id, "Введите ФИО обучающегося")
            bot.register_next_step_handler(sent, save_link1)

                
    #Информация об организации
    if message.text.strip() == '🏢Информация об организации':
            answer = 'Станция технического творчества Космопорт - это социальный проект АО "НПО автоматики" - одного из крупнейших предприятий России в области разработки и изготовления систем управления и радиоэлектронной аппаратуры для ракетно - космической техники.\n \nАдрес: г.Екатеринбург, ул. Луначарского 136\nСвязь: (343)355-93-88'
            bot.send_message(message.chat.id, answer)
            
    #кнопка назад
    if message.text.strip() == "⬅️ Назад": 
          markup=types.ReplyKeyboardMarkup(resize_keyboard=True)  
          item1=types.KeyboardButton("📆Актуальные курсы")
          item2=types.KeyboardButton("💼Загрузка документов")
          item3=types.KeyboardButton("🏢Информация об организации")
          markup.add(item1)
          markup.add(item2)
          markup.add(item3)    
          bot.send_message(message.chat.id, 'Для продолжения нажмите на одну из кнопок 👇',  reply_markup=markup)
          

            
# Запускаем бота
bot.polling(none_stop=True, interval=0)