# Імпортуємо функцію створення об'єкта бота
from telebot import TeleBot
# імпортуємо основні налаштування проекту
from settings import config
# Імпортуємо головний клас-обробник бота
from handlers.handler_main import HandlerMain


class TelBot:
     """
     Основний клас телеграм бота (сервер), в основі якого
     використовується бібліотека pyTelegramBotAPI
     """
     __version__ = config.VERSION
     __author__ = config.AUTHOR

     def __init__(self):
         """
         Ініціалізація бота
         """
         # отримуємо токен
         self.token = config.TOKEN
         # ініціалізуємо бот на основі зареєстрованого токена
         self.bot = TeleBot(self.token)
         # ініціалізуємо обробник подій
         self.handler = HandlerMain(self.bot)

     def start(self):
         """
         Метод призначений для старту оброблювача подій
         """
         self.handler.handle()

     def run_bot(self):
         """
         Метод запускає основні події сервера
         """
         # обробник подій
         self.start()
         # служить для запуску бота (робота в режимі нон-стоп)
         self.bot.polling(none_stop=True)


if __name__ == '__main__':
     bot = TelBot()
     bot.run_bot()