import telebot
from telebot import types
from parsing import main_parsing

# массив ссылок на вакансии
links = []
# был ли запрос и не пуст ли массив ссылок
was_req = False
# была ли дана команда /find
is_find = False

# Создаем экземпляр бота
bot = telebot.TeleBot('5898546763:AAFHVF2EW9hm2D0AkrePJiACGRV6LOf2OJg')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет. Этот бот может помочь с поиском работы, для более подробной информации наберите /help')


# Функция, обрабатывающая команду /help
@bot.message_handler(commands=["help"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'После команды /find бот ищет самую '
    'высокооплачиваемую вакансию на hh.ru. Следует написать /find, а '
    'потом нужную профессию. ')


# Функция, обрабатывающая команду /find
@bot.message_handler(commands=["find"])
def start(m, res=False):
    global is_find
    is_find = True
    bot.send_message(m.chat.id, 'Теперь введите нужную профессию:')


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    global links
    global was_req
    global is_find


    # обработка не предусмотренных команд
    if not is_find and not was_req:
        if not was_req:
            bot.send_message(message.chat.id, 'Вы можете ознакомится с функционалом '
            'бота с помощью команды /help')
        else:
            bot.send_message(message.chat.id, 'Вводите новую профессию после '
            'команды /find')

        return


    # если массив ссылок не пуст, работает при нажатии кнопки
    if was_req and message.text == "Следующая вакансия":
        try:
            # пробуем удалить 1 элемент и вывести следующий
            links.pop(0)
            bot.send_message(message.chat.id, links[0])
        except:
            # если это невозможно пишем, что вакансий больше нет
            bot.send_message(message.chat.id, 'Больше вакансий по данному запросу не найдено')
        
    else:

        bot.send_message(message.chat.id, 'Ожидайте...')

        # парсим hh.ru
        links = main_parsing(str(message.text))

        # если массив длины 0, то вакансий нет
        if len(links) == 0:
            bot.send_message(message.chat.id, 'Вакансий с известной зарплатой не найдено')

        # вывод первой вакансии
        else:
            bot.send_message(message.chat.id, links[0])
            was_req = True

        # если вакансии успешно найдены делаем кнопку
        if was_req:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item = types.KeyboardButton("Следующая вакансия")
            markup.add(item)

    # запроса /find не было --> говорим об этом
    is_find = False

# Запускаем бота
bot.infinity_polling()
