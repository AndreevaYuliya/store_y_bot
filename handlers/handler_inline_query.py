# імпортуємо клас батько
from handlers.handler import Handler
# імпортуємо повідомлення користувачу
from settings.message import MESSAGES


class HandlerInlineQuery(Handler):
     """
     Клас обробляє вхідні текстові
     повідомлення від натискання на інлайн кнопки
     """

     def __init__(self, bot):
         super().__init__(bot)

     def pressed_btn_product(self, call, code):
         """
         обробляє вхідні запити на натискання кнопок товару inline
         """
         # створюється запис у БД за фактом замовлення
         self.BD._add_orders(1, code, 1)

         self.bot.answer_callback_query(
             call.id,
             MESSAGES['product_order'].format(
                 self.BD.select_single_product_name(code),
                 self.BD.select_single_product_title(code),
                 self.BD.select_single_product_price(code),
                 self.BD.select_single_product_quantity(code)),
             show_alert = True)

     def handle(self):
         # Обробник (декоратор) запитів від натискання на кнопки товару.
         @self.bot.callback_query_handler(func=lambda call: True)
         def callback_inline(call):
             code = call.data
             if code.isdigit():
                 code = int(code)

             self.pressed_btn_product(call, code)