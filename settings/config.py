import os
# Імпортуємо модуль emoji для відображення емоджі
from emoji import emojize

# токен видається під час реєстрації програми
TOKEN = '6048229698:AAGFABM9-fR-hWgT8CiemfrPuxwvvyGWVQc'
# назва БД
NAME_DB = 'products.db'
# версія програми
VERSION = '0.0.1'
# автор додатку
AUTHOR = 'User'

# Батьківська директорія
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# шлях до бази даних
DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

# кнопки управління
KEYBOARD = {
     'CHOOSE_GOODS': emojize(':open_file_folder: Вибрати товар'),
     'INFO': emojize(':speech_balloon: Про магазин'),
     'SETTINGS': emojize('⚙️ Налаштування'),
     'SEMIPRODUCT': emojize(':pizza: Напівфабрикати'),
     'GROCERY': emojize(':bread: Бакалія'),
     'ICE_CREAM': emojize(':shaved_ice: Морозиво'),
     '<<': emojize('⏪'),
     '>>': emojize('⏩'),
     'BACK_STEP': emojize('◀️'),
     'NEXT_STEP': emojize('▶️'),
     'ORDER': emojize('✅ ЗАМОВЛЕННЯ'),
     'X': emojize('❌'),
     'DOUWN': emojize('🔽'),
     'AMOUNT_PRODUCT': COUNT,
     'AMOUNT_ORDERS': COUNT,
     'UP': emojize('🔼'),
     'APPLAY': '✅ Оформити замовлення',
     'COPY': '©️'
}

# id категорій продуктів
CATEGORY = {
     'SEMIPRODUCT': 1,
     'GROCERY': 2,
     'ICE_CREAM': 3,
}

# назви команд
COMMANDS = {
     'START': "start",
     'HELP': "help",
}