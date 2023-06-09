#імпортуємо спеціальні типи телеграм бота для створення елементів інтерфейсу
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, \
     ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
# імпортуємо налаштування та утиліти
from settings import config
# Імпортуємо клас-менеджер для роботи з бібліотекою
from data_base.dbalchemy import DBManager


class Keyboards:
     """
     Клас Keyboards призначений для створення та розмітки інтерфейсу бота
     """
     # ініціалізація розмітки

     def __init__(self):
         self.markup = None
         # ініціалізуємо менеджер для роботи з БД
         self.BD = DBManager()

     def set_btn(self, name, step=0, quantity=0):
         """
         Створює та повертає кнопку за вхідними параметрами
         """

         if name == "AMOUNT_ORDERS":
             config.KEYBOARD["AMOUNT_ORDERS"] = "{} {} {}".format(step + 1,
                                                                  'з', str(
                     self.BD.count_rows_order()))

         if name == "AMOUNT_PRODUCT":
             config.KEYBOARD["AMOUNT_PRODUCT"] = "{}".format(quantity)

         return KeyboardButton(config.KEYBOARD[name])

     def start_menu(self):
         """
         Створює розмітку кнопок в основному меню та повертає розмітку
         """
         self.markup = ReplyKeyboardMarkup(True, True)
         itm_btn_1 = self.set_btn('CHOOSE_GOODS')
         itm_btn_2 = self.set_btn('INFO')
         itm_btn_3 = self.set_btn('SETTINGS')
         # Розташування кнопок у меню
         self.markup.row(itm_btn_1)
         self.markup.row(itm_btn_2, itm_btn_3)
         return self.markup

     def info_menu(self):
         """
         Створює розмітку кнопок у меню 'Про магазин'
         """
         self.markup = ReplyKeyboardMarkup(True, True)
         itm_btn_1 = self.set_btn('<<')
         # Розташування кнопок у меню
         self.markup.row(itm_btn_1)
         return self.markup

     def settings_menu(self):
         """
         Створює розмітку кнопок у меню 'Налаштування'
         """
         self.markup = ReplyKeyboardMarkup(True, True)
         itm_btn_1 = self.set_btn('<<')
         # Розташування кнопок у меню
         self.markup.row(itm_btn_1)
         return self.markup

     @staticmethod
     def remove_menu():
         """
         Видаляє кнопки
         """
         return ReplyKeyboardRemove()

     def category_menu(self):
         """
         Створює розмітку кнопок у меню категорій товару та повертає розмітку
         """
         self.markup = ReplyKeyboardMarkup(True, True, row_width=1)
         self.markup.add(self.set_btn('SEMIPRODUCT'))
         self.markup.add(self.set_btn('GROCERY'))
         self.markup.add(self.set_btn('ICE_CREAM'))
         self.markup.row(self.set_btn('<<'), self.set_btn('ORDER'))
         return self.markup

     @staticmethod
     def set_inline_btn(name):
         """
         Створює та повертає інлайн кнопку за вхідними параметрами
         """
         return InlineKeyboardButton(str(name),
                                     callback_data=str(name.id))

     def set_select_category(self, category):
         """
         Створює розмітку інлайн-кнопок
         обраної категорії товару та повертає розмітку
         """
         self.markup = InlineKeyboardMarkup(row_width=1)
         # завантажуємо в назву інлайн кнопок дані
         # з БД у відповідність до категорії товару
         for itm in self.BD.select_all_products_category(category):
             self.markup.add(self.set_inline_btn(itm))

         return self.markup

     def orders_menu(self, step, quantity):
         """
         Створює розмітку кнопок у замовленні товару та повертає розмітку
         """

         self.markup = ReplyKeyboardMarkup(True, True)
         itm_btn_1 = self.set_btn('X', step, quantity)
         itm_btn_2 = self.set_btn('DOUWN', step, quantity)
         itm_btn_3 = self.set_btn('AMOUNT_PRODUCT', step, quantity)
         itm_btn_4 = self.set_btn('UP', step, quantity)

         itm_btn_5 = self.set_btn('BACK_STEP', step, quantity)
         itm_btn_6 = self.set_btn('AMOUNT_ORDERS', step, quantity)
         itm_btn_7 = self.set_btn('NEXT_STEP', step, quantity)
         itm_btn_8 = self.set_btn('APPLAY', step, quantity)
         itm_btn_9 = self.set_btn('<<', step, quantity)
         # Розташування кнопок у меню
         self.markup.row(itm_btn_1, itm_btn_2, itm_btn_3, itm_btn_4)
         self.markup.row(itm_btn_5, itm_btn_6, itm_btn_7)
         self.markup.row(itm_btn_9, itm_btn_8)

         return self.markup