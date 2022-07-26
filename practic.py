# -*- coding: utf-8 -*-
import random
import sys
import pyttsx3
import speech_recognition as sr
import json
from kak import *
from PyQt5 import QtCore, QtWebEngineWidgets

r = sr.Recognizer()
engine = pyttsx3.init()
mic = sr.Microphone(device_index=1)

voices = engine.getProperty('voices')
engine.setProperty('voice', 'ru')

file = open('base.json', 'r').read()  # Мы открываем для чтения и считываем данные

for voice in voices:
    if voice.name == 'Aleksandr':
        engine.setProperty('voice', voice.id)


def talk(word):
    engine.say(word)
    engine.runAndWait()


def record():
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.5)  # настройка посоторонних шумов
        print('Слушаю...')
        audio = r.listen(source)
        print('Услышала..')

    try:
        query = r.recognize_google(audio, language='ru-RU')
        text = query.lower()
        print('Вы сказали ', text)
        return text
    except sr.UnknownValueError:
        return record()
    except sr.RequestError:
        print('У меня доступа к сервера Googlе, для распознования вашей команды')
    except:
        print('Error404')


def hi():
    lst = ['привет', 'здравствуйте']
    talk(random.choice(lst))  # рандомным образом генерируем ответ


def quit():
    tsil = ['пока пока', 'всегда к вашим услугам']
    talk(random.choice(tsil))  # рандомным образом генерируем ответ
    exit(1)


def start():
    myquestions(record())


def AI(command):
    pars = json.loads(file)  # Загрузка данных в переменную
    if command in pars:
        dlina = len(pars[command])
        if dlina < 4:
            talk(random.choice(pars[command]))
        else:
            z = pars[command]  # передаем единственное значение
            print(len(z))
            talk(z)
    else:
        talk('Я не знаю как на это отвечать, научите меня пожалуйста')
        talk('Задайте вопрос')
        a = record()  # ключ
        talk('скажите как ответить')
        b = record()  # значение
        pars[a] = b  # ключ и значение (то чему научили)
        with open('base.json', 'w') as json_file:  # открываем файл для записи
            json.dump(pars, json_file, indent=2, sort_keys=True,
                      ensure_ascii=False)  # переменную, которую будем менять, новыми значениями и вывод будет ключ значение, сортировка и стандартная кодировка


def myquestions(command):
    if 'привет' in command or 'хай' in command:
        hi()  # обращаемся к функции hi
    elif 'пока' in command:
        quit()  # обращаемся к функции quit
    elif 'погода' in command:
        talk('Щас открою ')
        ui.textEdit.load(
            QtCore.QUrl('https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0&oq=%D0%BF%D0%BE%D0%B3'
                        '%D0%BE%D0%B4%D0%B0&aqs=chrome'
                        '..69i57j35i39j0i131i433i512j0i67l2j0i512j0i67l2j0i512j0i67i433i457.848j0j7&sourceid=chrome'
                        '&ie=UTF-8'))
    elif 'вконтакте' in command:
        talk('Щас открою ')
        ui.textEdit.load(QtCore.QUrl('https://vk.com/feed'))
    elif ('найти ' in command) or ('найди' in command):
        words = ('найди', 'найти', 'ищи', 'кто такой', 'что такое', 'о том')
        remove = ['пожалуйста', 'ладно', 'давай', 'сейчас']
        for i in words:
            command = command.replace(i, '')
            for j in remove:
                command = command.replace(j, '')
                command.strip()
        talk('Щас открою ')
        ui.textEdit.load(QtCore.QUrl(f'https://www.google.com/search?q={command}&oq={command}'f'81&aqs=chrome..69i57'
                             f'j46i131i433j0l5.2567j0j7&sourceid=chrome&ie=UTF-8'))
    else:
        AI(command)

# while True:
# start()


app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
MainWindow.resize(400, 300)

# web = QtWebEngineWidgets.QWebEngineView()
# web.load(QtCore.QUrl('https://google.com/'))
# web.show()

ui.pushButton.clicked.connect(start)
ui.pushButton_2.clicked.connect(quit)

sys.exit(app.exec())
