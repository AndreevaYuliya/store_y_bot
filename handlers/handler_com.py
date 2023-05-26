# імпортуємо клас батько
from handlers.handler import Handler


class HandlerCommands(Handler):
     """
     Клас обробляє вхідні команди /start та /help тощо.
     """
     def __init__(self, bot):
         super().__init__(bot)

     def pressed_btn_start(self, message):
         """
         обробляє вхідні /start команди
         """
         self.bot.send_message(message.chat.id,
                               f'{message.from_user.first_name},'
                               f' привіт! Чекаю на подальші завдання.',
                               reply_markup=self.keybords.start_menu())

     def handle(self):
         # обробник (декоратор) повідомлень,
         # який обробляє вхідні команди /start.
         @self.bot.message_handler(commands=['start'])
         def handle(message):
             print(type(message))
             if message.text == '/start':
                 self.pressed_btn_start(message)