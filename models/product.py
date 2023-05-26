# компоненти бібліотеки для опису структури таблиці
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
# Імпортуємо модуль для зв'язування таблиць
from sqlalchemy.orm import relationship, backref

# Імпортуємо модель Категорія для зв'язування моделей
from models.category import Category
from data_base.dbcore import Base


class Products(Base):
     """
     Клас для створення таблиці "Товар",
     заснований на декларативному стилі SQLAlchemy
     """
     # назва таблиці
     __tablename__ = 'products'

     # поля таблиці
     id = Column (Integer, primary_key = True)
     name = Column (String, index = True)
     title = Column(String)
     price = Column(Float)
     quantity = Column(Integer)
     is_active = Column(Boolean)
     category_id = Column(Integer, ForeignKey('category.id'))
     # для каскадного видалення даних із таблиці
     category = relationship(
         Category,
         backref=backref('products',
                         uselist=True,
                         cascade='delete,all'))

     def __repr__(self):
         """
         Метод повертає формальне рядкове представлення вказаного об'єкта
         """
         return f"{self.name} {self.title} {self.price}"