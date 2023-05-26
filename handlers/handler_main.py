# імпортуємо клас HandlerCommands обробка команд
from handlers.handler_com import HandlerCommands
# імпортуємо клас HandlerAllText обробка натискання на кнопки та інші повідомлення
from handlers.handler_all_text import HandlerAllText
# імпортуємо клас HandlerInlineQuery обробка натискання на кнопки інлайн
from handlers.handler_inline_query import HandlerInlineQuery


class HandlerMain:
     """
     Клас компонувальник
     """
     def __init__(self, bot):
         # отримуємо нашого бота
         self.bot = bot
         # тут буде ініціалізація обробників
         self.handler_commands = HandlerCommands(self.bot)
         self.handler_all_text = HandlerAllText(self.bot)
         self.handler_inline_query = HandlerInlineQuery(self.bot)

     def handle(self):
         # тут буде запуск обробників
         self.handler_commands.handle()
         self.handler_all_text.handle()
         self.handler_inline_query.handle()