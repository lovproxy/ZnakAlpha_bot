import telebot
import sqlite3
import time
from telebot import types
#2.136 строка!!!!!!!
a,b,c,d,e,f,g,otv,gor,po,rsa = str(),str(),str(),str(),str(),str(),str(),str(),str(),str(),str()
i = 0
ank = []
op = 1
ttt = ('М','Ж')
ss = 0
@bot.message_handler(content_types=['text'])
def gettext(message):
    if message.text=='/start':
        keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button0 = telebot.types.KeyboardButton(text="/anketa")
        button2 = telebot.types.KeyboardButton(text="/search")
        button3 = telebot.types.KeyboardButton(text="/lower")
        button5 = telebot.types.KeyboardButton(text="/help")
        keyboard1.add(button0, button2,button3,button5)
        bot.send_message(message.from_user.id,'Доброго времени суток!Этот бот создан для поиска вторых половинок в вашем городе!Чтобы заполнить информацию о себе, введите команду /anketa.Для того,чтобы начать поиск,введите команду /search',reply_markup=keyboard1)
        global a
        a = message.from_user.username
        a = '@' + a
    elif message.text=='/anketa':
        a = message.from_user.username
        a = '@' + a
        mnogo(message)
    elif message.text=='/search':
        anket(message)
    elif message.text=='/lower':
        a = message.from_user.username
        a = '@' + a
        global ss
        ss = 1
        est(message)
    elif message.text=='/delete':
        a = message.from_user.username
        a = '@' + a
        bot.send_message(message.from_user.id, 'Вы захотели удалить свою анкету.Подтвеждаете данное действие?')
        bot.register_next_step_handler(message, dele)
    elif message.text=='/help':
        bot.send_message(message.from_user.id,'Чтобы заполнить информацию о себе, введите команду /anketa.\nДля того,чтобы начать поиск,введите команду /search.\nДля изменения своей анкеты,введите \n/lower.\n Чтобы удалить свою анкету введите \n/delete.\nТакже вы можете посмотреть свою анкету,введя команду /myank.')
    elif message.text=='/myank':
        yes(message)
    else:
        bot.send_message(message.from_user.id, 'Ваша команда не принадлежит перечню доступных мне команд.Введите /help для ознакомления со списков всех команд!')
@bot.message_handler(content_typer=['text'])
def anketa(message):
    global b,op
    b = message.text
    bot.send_message(message.from_user.id, 'Введите вашу фамилию:')
    op = 2
    bot.register_next_step_handler(message, prov)
def fam(message):
    global c,op
    c = message.text
    bot.send_message(message.from_user.id, 'Введите ваше отчество:')
    op = 3
    bot.register_next_step_handler(message, prov)
def otch(message):
    global d,op
    d = message.text
    bot.send_message(message.from_user.id, 'Введите ваш возраст:')
    op = 4
    bot.register_next_step_handler(message, prov)
def age(message):
    global e,op
    e = message.text
    bot.send_message(message.from_user.id, 'Введите ваш город,где вы находитесь в данный момент:')
    op = 5
    bot.register_next_step_handler(message, prov)
def gorod(message):
    global f,op
    f = message.text
    keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button0 = telebot.types.KeyboardButton(text="М")
    button1 = telebot.types.KeyboardButton(text="Ж")
    keyboard2.add(button0, button1)
    bot.send_message(message.from_user.id, 'Введите ваш пол(М или Ж):',reply_markup=keyboard2)
    op = 6
    bot.register_next_step_handler(message, prov)


def pol(message):
    keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button0 = telebot.types.KeyboardButton(text="/anketa")
    button1 = telebot.types.KeyboardButton(text="/myank")
    button2 = telebot.types.KeyboardButton(text="/search")
    button3 = telebot.types.KeyboardButton(text="/lower")
    button4 = telebot.types.KeyboardButton(text="/delete")
    button5 = telebot.types.KeyboardButton(text="/help")
    keyboard1.add(button0, button1,button2, button3,button4, button5)
    if 'М'==message.text or 'Ж'==message.text:
        global g
        g = message.text
        if ss==0:
            cursor.execute('INSERT INTO Users (id, imya, fam, otch, age, gorod, pol) VALUES (?, ?, ?, ?, ?, ?, ?)', (a, b, c, d, e, f, g))
            bot.send_message(message.from_user.id,'Отлично!Ваша анкета заполнена.Теперь вы можете начать поиск своей второй половинки.Если вы хотите поменять информацию о себе,то введите команду /lower.',reply_markup=keyboard1)
        else:
            aaa = cursor.execute('SELECT * FROM Users WHERE id= ?',(a,)).fetchall()
            if len(aaa)>0:
                cursor.execute('UPDATE Users SET imya=?,fam=?,otch=?,age=?,gorod=? WHERE id = ?',(b,c,d,e,f,a))
                bot.send_message(message.from_user.id,'Отлично!Ваша анкета была перезаписана.Теперь вы можете продолжить поиск своей второй половинки введя команду /search.',reply_markup=keyboard1)
    elif '/' in message.text:
        gettext(message)
    else:
        bot.send_message(message.from_user.id,'Ай-ай-ай...Введите корректный пол(М или Ж)!')
        bot.register_next_step_handler(message,pol)
    connection.commit()
def est(message):
    cursor.execute('SELECT * FROM Users WHERE id= ?', (a,))
    aaa = cursor.fetchall()
    if len(aaa) == 0:
        bot.send_message(message.from_user.id,'Ваша первоначальная анкета не была обнаружена.Воспользуйтесь командой /anketa для создания своей анкеты!')
    else:
        bot.send_message(message.from_user.id,
                         'Вы захотели изменить данные о себе.Заполните анкету о себе заново.Введите ваше имя:')
        bot.register_next_step_handler(message, prov)
def dele(message):
    if message.text=='Да' or message.text=='Yes'or message.text=='Da':
        cursor.execute('SELECT * FROM Users WHERE id= ?', (a,))
        aaa = cursor.fetchall()
        if len(aaa) > 0:
            cursor.execute("DELETE FROM Users WHERE id = ?",(a,))
            connection.commit()
            bot.send_message(message.from_user.id,'Ваша анкета была удалена!')
        else:
            bot.send_message(message.from_user.id, 'Ваших анкет не обнаружено!Чтобы создать новую,введите команду /anketa')
    elif message.text=='No' or message.text=='Net' or message.text=='Нет':
        bot.send_message(message.from_user.id,'Удаление отменено.Можете поискать себе вторую половинку командой /search!')
    else:
        prover(message)
def mnogo(message):
    cursor.execute('SELECT * FROM Users WHERE id= ?', (a,))
    aaa = cursor.fetchall()
    global op
    if len(aaa) < 1:
        bot.send_message(message.from_user.id, 'Пожалуйста,вводите свои данные на русском языке!')
        bot.send_message(message.from_user.id, 'Введите ваше имя:')
        op = 1
        bot.register_next_step_handler(message, prov)
    else:
        bot.send_message(message.from_user.id, 'У вас уже создана анкета!Если вы хотите её изменить,введите /lower.')
def search(message):
    cursor.execute('SELECT * FROM Users WHERE gorod=? AND pol=?',(gor,rsa))
    global ank
    ank = cursor.fetchall()
    if len(ank)>0:
        aaaaa = '<b>Связь с собеседником</b>:' + '\n' + str(ank[i][0]) + '\n' + '<b>Имя</b>:' + '\n' + str(
            ank[i][1]) + '\n' + '<b>Фамилия</b>:' + '\n' + str(ank[i][2]) + '\n' + '<b>Отчество</b>:' + '\n' + str(
            ank[i][3]) + '\n' + '<b>Возраст</b>:' + '\n' + str(ank[i][4])
        markup = types.InlineKeyboardMarkup()
        f = 'https://t.me/'+str(ank[i][0][1:])
        k1 = types.InlineKeyboardButton(text=ank[i][0], url=f)
        markup.add(k1)
        bot.send_message(message.from_user.id,aaaaa, reply_markup = markup, parse_mode='HTML')
        time.sleep(5)
        bot.send_message(message.from_user.id, 'Продолжить поиск?')
        bot.register_next_step_handler(message, prodol)
    else:
        bot.send_message(message.from_user.id, 'В твоём городе нету людей,которые бы пользовались нашей программой...Искать людей из других городов?')
        bot.register_next_step_handler(message, nety)

def prodol(message):
    if message.text=='Да' or message.text=='Da' or message.text=='Yes':
        global i
        if i+2 <len(ank):
            i += 1
            search(message)
        else:
            i = 0
            bot.send_message(message.from_user.id,'Вы посмотрели все анкеты,которые были созданы пользователями.Хотите посмотреть анкеты в других городах?')
            bot.register_next_step_handler(message, nety)
    elif message.text=='No' or message.text=='Net' or message.text=='Нет':
        bot.send_message(message.from_user.id, 'Хорошего дня!')
    else:
        bot.register_next_step_handler(message, kor2)
def nety(message):
    #Остановка тут!!!!!!!!!!!!!!!!!!!!!!!
    if message.text=='Да' or message.text=='Da' or message.text=='Yes':
        global ank
        global i
        cursor.execute('SELECT * FROM Users Where pol=?',(rsa,))
        ank=cursor.fetchall()
        if len(ank)>0:
            if i <len(ank):
                aaaaa = '<b>Связь с собеседником</b>:' + '\n' + str(ank[i][0]) + '\n' + '<b>Имя</b>:' + '\n' + str(
            ank[i][1]) + '\n' + '<b>Фамилия</b>:' + '\n' + str(ank[i][2]) + '\n' + '<b>Отчество</b>:' + '\n' + str(
            ank[i][3]) + '\n' + '<b>Возраст</b>:' + '\n' + str(ank[i][4])+'\n'+'<b>Город</b>:'+'\n'+str(ank[i][5])
                markup = types.InlineKeyboardMarkup()
                f = 'https://t.me/' + str(ank[i][0][1:])
                k1 = types.InlineKeyboardButton(text=ank[i][0], url=f)
                markup.add(k1)
                bot.send_message(message.from_user.id, aaaaa, reply_markup=markup, parse_mode='HTML')
                time.sleep(5)
                bot.send_message(message.from_user.id, 'Продолжить поиск?')
                i+=1
                bot.register_next_step_handler(message, nety)
            else:
                i = 0
                bot.send_message(message.from_user.id, 'Вы просмотрели все анкеты,которые были зарегистрированы пользователями.Хорошего дня!')
        else:
            bot.send_message(message.from_user.id, 'К сожалению в данный момент не существует анкет,которые можно было бы показать.Возвращайтесь позже!')
    elif message.text == 'No' or message.text == 'Net' or message.text == 'Нет':
        bot.send_message(message.from_user.id, 'Хорошего дня!')
    else:
        kor1(message)
def kor1(message):
    if '/' in message.text:
        gettext(message)
    else:
        bot.send_message(message.from_user.id, 'Введите корректный ответ!')
        bot.register_next_step_handler(message,nety)
def kor2(message):
    if '/' in message.text:
        gettext(message)
    else:
        bot.send_message(message.from_user.id, 'Введите корректный ответ!')
        prodol(message)
def anket(message):
    a = message.from_user.username
    a = '@' + a
    cursor.execute('SELECT * FROM Users WHERE id=?', (a,))
    global hhh, po,gor
    hhh = cursor.fetchall()
    if len(hhh)>0:
        gor = hhh[0][5]
        po = hhh[0][6]
        if po == ttt[0]:
            global rsa
            rsa = 'Ж'
        else:
            rsa = 'М'
        search(message)
    else:
        bot.send_message(message.from_user.id,'Введите город,в котором хотите начать поиск:')
        bot.register_next_step_handler(message,qqq)
def qqq(message):
    global gor
    gor = message.text
    bot.send_message(message.from_user.id, 'Введите ваш пол:')
    bot.register_next_step_handler(message, pooo)
def pooo(message):
    global rsa
    if message.text=='М':
        rsa = 'Ж'
    else:
        rsa = 'М'
    search(message)
def prover(message):
    if '/' in message.text:
        gettext(message)
    else:
        bot.send_message(message.from_user.id,
                         'Введёный вами ответ не является корректным.Повторите попытку,пожалуйста!')
        bot.register_next_step_handler(message, dele)
def yes(message):
    cursor.execute('SELECT * FROM Users WHERE id= ?', (a,))
    ank = cursor.fetchall()
    if len(ank)>0:
        aaaaa = '<b>Связь с собеседником</b>:' + '\n' + str(ank[0][0]) + '\n' + '<b>Имя</b>:' + '\n' + str(
        ank[0][1]) + '\n' + '<b>Фамилия</b>:' + '\n' + str(ank[0][2]) + '\n' + '<b>Отчество</b>:' + '\n' + str(
        ank[0][3]) + '\n' + '<b>Возраст</b>:' + '\n' + str(ank[0][4]) + '\n' + '<b>Город</b>:' + '\n' + str(
        ank[0][5]) + '\n' + '<b>Пол</b>:' + '\n' + str(ank[0][6])
        markup = types.InlineKeyboardMarkup()
        bot.send_message(message.from_user.id, aaaaa, reply_markup=markup, parse_mode='HTML')
    else:
        bot.send_message(message.from_user.id,'Ваша анкета не была зарегистрирована.Вы можете это сделать,введя команду /anketa')
def prov(message):
    if '/' in message.text:
        gettext(message)
    else:
        match op:
            case 1:
                anketa(message)
            case 2:
                fam(message)
            case 3:
                otch(message)
            case 4:
                age(message)
            case 5:
                gorod(message)
            case 6:
                pol(message)
bot.polling(none_stop=True, interval=0)
