# компоненти бібліотеки для опису структури таблиці
from sqlalchemy import Column, DateTime, Integer, ForeignKey
# Імпортуємо модуль для зв'язування таблиць
from sqlalchemy.orm import relationship, backref

# імпортуємо модель продуктів для зв'язування моделей
from models.product import Products
from data_base.dbcore import Base



class Order(Base):
     """
     Клас для створення таблиці "Замовлення",
     заснований на декларативному стилі SQLAlchemy
     """
     # назва таблиці
     __tablename__ = 'orders'

     # поля таблиці
     id = Column (Integer, primary_key = True)
     quantity = Column(Integer)
     data = Column(DateTime)
     product_id = Column(Integer, ForeignKey('products.id'))
     user_id = Column(Integer)

     # для каскадного видалення даних із таблиці
     products = relationship(
         Products,
         backref=backref('orders',
                         uselist=True,
                         cascade='delete,all'))

     def __repr__(self):
         """
         Метод повертає формальне рядкове представлення вказаного об'єкта
         """
         return f"{self.quantity} {self.data}"