# імпортуємо відповідь користувачу
from settings.message import MESSAGES
from settings import config, utility
# імпортуємо клас батько
from handlers.handler import Handler


class HandlerAllText(Handler):
     """
     Клас обробляє вхідні текстові повідомлення від натискання кнопок
     """

     def __init__(self, bot):
         super().__init__(bot)
         # крок у замовленні
         self.step = 0

     def pressed_btn_category(self, message):
         """
         Обробка події натискання на кнопку 'Вибрати товар'. А точніше
         це вибір категорії товарів
         """
         self.bot.send_message(message.chat.id, "Каталог категорій товару",
                               reply_markup=self.keybords.remove_menu())
         self.bot.send_message(message.chat.id, "Зробіть свій вибір",
                               reply_markup=self.keybords.category_menu())

     def pressed_btn_info(self, message):
         """
         Обробка події натискання на кнопку 'Про магазин'
         """
         self.bot.send_message(message.chat.id, MESSAGES['trading_store'],
                               parse_mode="HTML",
                               reply_markup=self.keybords.info_menu())

     def pressed_btn_settings(self, message):
         """
         Обробка події натискання на кнопку 'Налаштування'
         """
         self.bot.send_message(message.chat.id, MESSAGES['settings'],
                               parse_mode="HTML",
                               reply_markup=self.keybords.settings_menu())

     def pressed_btn_back(self, message):
         """
         Обробка події натискання на кнопку 'Назад'
         """
         self.bot.send_message(message.chat.id, "Ви повернулися назад",
                               reply_markup=self.keybords.start_menu())

     def pressed_btn_product(self, message, product):
         """
         Обробка події натискання на кнопку 'Вибрати товар'. А точніше
         це вибір товару з категорії
         """
         self.bot.send_message(message.chat.id, 'Категорія' +
                               config.KEYBOARD[product],
                               reply_markup=self.keybords.set_select_category(
                                   config.CATEGORY[product]))
         self.bot.send_message(message.chat.id, "Ок",
                               reply_markup=self.keybords.category_menu())

     def pressed_btn_order(self, message):
         """
         Обробляє вхідні текстові повідомлення від натискання кнопки 'Замовлення'.
         """
         # обнулюємо дані кроку
         self.step = 0
         # отримуємо список усіх товарів у замовленні
         count = self.BD.select_all_product_id()
         # отримуємо кількість у кожній позиції товару у замовленні
         quantity = self.BD.select_order_quantity(count[self.step])

         # надсилаємо відповідь користувачу
         self.send_message_order(count[self.step], quantity, message)

     def send_message_order(self, product_id, quantity, message):
         """
         Надсилає відповідь користувачу під час виконання різних дій
         """
         self.bot.send_message(message.chat.id,MESSAGES['order_number'].format(
             self.step+1), parse_mode="HTML")
         self.bot.send_message(message.chat.id,
                               MESSAGES['order'].
                               format(self.BD.select_single_product_name(
                                   product_id),
                                      self.BD.select_single_product_title(
                                          product_id),
                                      self.BD.select_single_product_price(
                                          product_id),
                                      self.BD.select_order_quantity(
                                          product_id)),
                               parse_mode="HTML",
                               reply_markup=self.keybords.orders_menu(
                                   self.step, quantity))

     def pressed_btn_up(self, message):
         """
         Обробка натискання кнопки збільшення
         кількості певного товару у замовленні
         """
         # отримуємо список усіх товарів у замовленні
         count = self.BD.select_all_product_id()
         # отримуємо кількість конкретної позиції у замовленні
         quantity_order = self.BD.select_order_quantity(count[self.step])
         # отримуємо кількість конкретної позиції в пролуктах
         quantity_product = self.BD.select_single_product_quantity(
             count[self.step])
         # якщо товар є
         if quantity_product > 0:
             quantity_order += 1
             quantity_product -= 1
             # вносимо зміни до БД orders
             self.BD.update_order_value(count[self.step],
                                        'quantity', quantity_order)
             # вносимо зміни до БД product
             self.BD.update_product_value(count[self.step],
                                          'quantity', quantity_product)
         # надсилаємо відповідь користувачу
         self.send_message_order(count[self.step], quantity_order, message)

     def pressed_btn_douwn(self, message):
         """
         Обробка натискання кнопки зменшення
         кількості певного товару у замовленні
         """
         # отримуємо список усіх товарів у замовленні
         count = self.BD.select_all_product_id()
         # отримуємо кількість конкретної позиції у замовленні
         quantity_order = self.BD.select_order_quantity(count[self.step])
         # отримуємо кількість конкретної позиції в пролуктах
         quantity_product = self.BD.select_single_product_quantity(
             count[self.step])
         # якщо товар у замовленні є
         if quantity_order > 0:
             quantity_order -= 1
             quantity_product += 1
             # вносимо зміни до БД orders
             self.BD.update_order_value(count[self.step],
                                        'quantity', quantity_order)
             # вносимо зміни до БД product
             self.BD.update_product_value(count[self.step],
                                          'quantity', quantity_product)
         # надсилаємо відповідь користувачу
         self.send_message_order(count[self.step], quantity_order, message)

     def pressed_btn_x(self, message):
         """
         Обробка натискання кнопки видалення
         товарної позиції замовлення
         """
         # отримуємо список усіх product_id замовлення
         count = self.BD.select_all_product_id()
         # якщо список не порожній
         if count.__len__() > 0:
             # отримуємо кількість конкретної позиції у замовленні
             quantity_order = self.BD.select_order_quantity(count[self.step])
             # отримуємо кількість товару до конкретної
             # позиції замовлення для повернення в product
             quantity_product = self.BD.select_single_product_quantity(
                 count[self.step])
             quantity_product += quantity_order
             # вносимо зміни до БД orders
             self.BD.delete_order(count[self.step])
             # вносимо зміни до БД product
             self.BD.update_product_value(count[self.step],
                                          'quantity', quantity_product)
             # зменшуємо крок
             self.step -= 1

         count = self.BD.select_all_product_id()
         # якщо список не порожній
         if count.__len__() > 0:

             quantity_order = self.BD.select_order_quantity(count[self.step])
             # надсилаємо користувачеві повідомлення
             self.send_message_order(count[self.step], quantity_order, message)

         else:
             # якщо товару немає у замовленні відправляємо повідомлення
             self.bot.send_message(message.chat.id, MESSAGES['no_orders'],
                                   parse_mode="HTML",
                                   reply_markup=self.keybords.category_menu())

     def pressed_btn_back_step(self, message):
         """
         Обробка натискання кнопки переміщення
         до більш ранніх товарних позицій замовлення
         """
         # зменшуємо крок поки крок не буде рівний "0"
         if self.step > 0:
             self.step -= 1
         # отримуємо список усіх товарів у замовленні
         count = self.BD.select_all_product_id()
         quantity = self.BD.select_order_quantity(count[self.step])

         # надсилаємо відповідь користувачу
         self.send_message_order(count[self.step], quantity, message)

     def pressed_btn_next_step(self, message):
         """
         Обробка натискання кнопки переміщення
         до пізніших товарних позицій замовлення
         """
         # збільшуємо крок доки крок не буде рівний кількості рядків
         # полів замовлення з розрахунком ціни поділу починаючи з "0"
         if self.step < self.BD.count_rows_order() - 1:
             self.step += 1
         # отримуємо список усіх товарів у замовленні
         count = self.BD.select_all_product_id()
         # отримуємо еоличество конкретного товару у відповідність до кроку вибірки
         quantity = self.BD.select_order_quantity(count[self.step])

         # надсилаємо відповідь користувачу
         self.send_message_order(count[self.step], quantity, message)

     def pressed_btn_apllay(self, message):
         """
         обробляє вхідні текстові повідомлення
         від натискання на кнопку 'Оформити замовлення'.
         """
         # надсилаємо відповідь користувачу
         self.bot.send_message(message.chat.id,
                               MESSAGES['applay'].format(
                                   utility.get_total_coas(self.BD),

                                   utility.get_total_quantity(self.BD)),
                               parse_mode="HTML",
                               reply_markup=self.keybords.category_menu())
         # відчищаємо дані із замовлення
         self.BD.delete_all_order()

     def handle(self):
         # обробник (декоратор) повідомлень,
         # який обробляє вхідні текстові повідомлення від натискання кнопок.
         @self.bot.message_handler(func=lambda message: True)
         def handle(message):
             # ********** меню ********** #

             if message.text == config.KEYBOARD['CHOOSE_GOODS']:
                 self.pressed_btn_category(message)

             if message.text == config.KEYBOARD['INFO']:
                 self.pressed_btn_info(message)

             if message.text == config.KEYBOARD['SETTINGS']:
                 self.pressed_btn_settings(message)

             if message.text == config.KEYBOARD['<<']:
                 self.pressed_btn_back(message)

             if message.text == config.KEYBOARD['ORDER']:
                 # якщо є замовлення
                 if self.BD.count_rows_order() > 0:
                     self.pressed_btn_order(message)
                 else:
                     self.bot.send_message(message.chat.id,
                                           MESSAGES['no_orders'],
                                           parse_mode="HTML",
                                           reply_markup=self.keybords.
                                           category_menu())

             # ********** меню (категорії товару, ПФ, Бакалія, Морозиво)******
             if message.text == config.KEYBOARD['SEMIPRODUCT']:
                 self.pressed_btn_product(message, 'SEMIPRODUCT')

             if message.text == config.KEYBOARD['GROCERY']:
                 self.pressed_btn_product(message, 'GROCERY')

             if message.text == config.KEYBOARD['ICE_CREAM']:
                 self.pressed_btn_product(message, 'ICE_CREAM')

             # ********** меню (Замовлення)**********

             if message.text == config.KEYBOARD['UP']:
                 self.pressed_btn_up(message)

             if message.text == config.KEYBOARD['DOUWN']:
                 self.pressed_btn_douwn(message)

             if message.text == config.KEYBOARD['X']:
                 self.pressed_btn_x(message)

             if message.text == config.KEYBOARD['BACK_STEP']:
                 self.pressed_btn_back_step(message)

             if message.text == config.KEYBOARD['NEXT_STEP']:
                 self.pressed_btn_next_step(message)

             if message.text == config.KEYBOARD['APPLAY']:
                 self.pressed_btn_apllay(message)
             # інші натискання та введення даних користувачем
             else:
                 self.bot.send_message(message.chat.id, message.text)