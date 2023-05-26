from os import path
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_base.dbcore import Base

from settings import config
from models.product import Products
from models.order import Order
from settings import utility


class Singleton(type):
    """
    Патерн Singleton надає механізм створення одного
    і лише одного об'єкта класу,
    та надання до нього глобальної точки доступу.
    """
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class DBManager(metaclass=Singleton):
    """ 
    Клас менеджер для работи із БД 
    """

    def __init__(self):
        """
        Ініціалізація сесії та підключення до БД
        """
        self.engine = create_engine(config.DATABASE)
        session = sessionmaker(bind=self.engine)
        self._session = session()
        if not path.isfile(config.DATABASE):
            Base.metadata.create_all(self.engine)

    def select_all_products_category(self, category):
        """
        Повертає всі товари категорії
        """
        result = self._session.query(Products).filter_by(
            category_id=category).all()

        self.close()
        return result

    def close(self):
        """ Закриває сесію """
        self._session.close()

    # Робота із замовленням
    def _add_orders(self, quantity, product_id, user_id,):
        """
        Метод заповнення замовлення
        """
        # отримуємо список усіх product_id
        all_id_product = self.select_all_product_id()
        # якщо дані є у списку, оновлюємо таблиці замовлення та продуктів
        if product_id in all_id_product:
            quantity_order = self.select_order_quantity(product_id)
            quantity_order += 1
            self.update_order_value(product_id, 'quantity', quantity_order)

            quantity_product = self.select_single_product_quantity(product_id)
            quantity_product -= 1
            self.update_product_value(product_id, 'quantity', quantity_product)
            return
        # якщо даних немає, створюємо новий об'єкт замовлення
        else:
            order = Order(quantity=quantity, product_id=product_id,
                          user_id=user_id, data=datetime.now())
            quantity_product = self.select_single_product_quantity(product_id)
            quantity_product -= 1
            self.update_product_value(product_id, 'quantity', quantity_product)

        self._session.add(order)
        self._session.commit()
        self.close()

    def select_all_product_id(self):
        """
        Повертає всі id товару у замовленні
        """
        result = self._session.query(Order.product_id).all()
        self.close()
        # конвертуємо результат вибірки на вигляд [1,3,5...]
        return utility._convert(result)

    def select_order_quantity(self, product_id):
        """
        Повертає кількість товару на замовлення
        """
        result = self._session.query(Order.quantity).filter_by(
            product_id=product_id).one()
        self.close()
        return result.quantity

    def select_single_product_quantity(self, rownum):
        """
        Повертає кількість товару на складі
        відповідно до номеру товару - rownum
        Цей номер визначається під час вибору товару в інтерфейсі.
        """
        result = self._session.query(
            Products.quantity).filter_by(id=rownum).one()
        self.close()
        return result.quantity

    def update_product_value(self, rownum, name, value):
        """
        Оновлює кількість товару на складі
        відповідно до номеру товару - rownum
        """
        self._session.query(Products).filter_by(
            id=rownum).update({name: value})
        self._session.commit()
        self.close()

    def update_order_value(self, product_id, name, value):
        """
        Оновлює кількість товару на складі
        відповідно до номеру товару - rownum
        """
        self._session.query(Order).filter_by(
            product_id=product_id).update({name: value})
        self._session.commit()
        self.close()

    def select_single_product_name(self, rownum):
        """
        Повертає назву товару
        відповідно до номеру товару - rownum
        """
        result = self._session.query(Products.name).filter_by(id=rownum).one()
        self.close()
        return result.name

    def select_single_product_title(self, rownum):
        """
        Повертає торгову марку товару
        відповідно до номеру товару - rownum
        """
        result = self._session.query(Products.title).filter_by(id=rownum).one()
        self.close()
        return result.title

    def select_single_product_price(self, rownum):
        """
        Повертає ціну товару
        відповідно до номеру товару - rownum
        """
        result = self._session.query(Products.price).filter_by(id=rownum).one()
        self.close()
        return result.price

    def count_rows_order(self):
        """
        Повертає кількість позицій у замовленні
        """
        result = self._session.query(Order).count()
        self.close()
        return result

    def select_order_quantity(self, product_id):
        """
        Повертає кількість товару із замовлення
        відповідно до номеру товару - rownum
        """
        result = self._session.query(Order.quantity).filter_by(
            product_id=product_id).one()
        self.close()
        return result.quantity

    def delete_order(self, product_id):
        """
        Видаляє товар із замовлення
        """
        self._session.query(Order).filter_by(product_id=product_id).delete()
        self._session.commit()
        self.close()

    def delete_all_order(self):
        """
        Видаляє дані всього замовлення
        """
        all_id_orders = self.select_all_order_id()

        for itm in all_id_orders:
            self._session.query(Order).filter_by(id=itm).delete()
            self._session.commit()
        self.close()

    def select_all_order_id(self):
        """
        Повертає всі id замовлення
        """
        result = self._session.query(Order.id).all()
        self.close()
        return utility._convert(result)