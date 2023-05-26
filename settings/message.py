# імпортуємо налаштування для відображення емоджі
from .config import KEYBOARD, VERSION, AUTHOR

# відповідь користувачу під час відвідування блоку "Про магазин"
trading_store = """

<b>Ласкаво просимо до додатку
             GroceryStore !!!</b>

Цей додаток розроблено
спеціально для торгових представників,
далі <i>(ТП/СВ)</i>, а також для комірників,
комерційних організацій, що здійснюють
оптово-роздрібну торгівлю.

ТП використовуючи програму GroceryStore,
у зручній інтуїтивній формі зможуть без
особливих труднощів прийняти замовлення від клієнта.
GroceryStore допоможе сформувати замовлення
і в зручному вигляді адресує комірнику
фірми для подальшого комплектування замовлення.

"""
# відповідь користувачу при відвідуванні блоку "Налаштування"
settings = """
<b>Спільне керівництво додатком:</b>

<i>Навігація:</i>

-<b>({}) - </b><i>назад</i>
-<b>({}) - </b><i>вперед</i>
-<b>({}) - </b><i>збільшити</i>
-<b>({}) - </b><i>зменшити</i>
-<b>({}) - </b><i>наступний</i>
-<b>({}) - </b><i>попередній</i>

<i>Спеціальні кнопки:</i>

-<b>({}) - </b><i>видалити</i>
-<b>({}) - </b><i>замовлення</i>
-<b>({}) - </b><i>Оформити замовлення</i>

<i>Загальна інформація:</i>

-<b>версія програми: - </b><i>({})</i>
-<b>розробник: -</b><i>({})</i>


<b>{}Ваше ім'я</b>

""".format(
     KEYBOARD['<<'],
     KEYBOARD['>>'],
     KEYBOARD['UP'],
     KEYBOARD['DOUWN'],
     KEYBOARD['NEXT_STEP'],
     KEYBOARD['BACK_STEP'],
     KEYBOARD['X'],
     KEYBOARD['ORDER'],
     KEYBOARD['APPLAY'],
     VERSION,
     AUTHOR,
     KEYBOARD['COPY'],
)
# відповідь користувачу при додаванні товару на замовлення
product_order = """
Вибраний товар:

{}
{}
Вартість: {} грн

доданий на замовлення!

На складі залишилось {} од.
"""
# відповідь користувачу при відвідуванні блоку із замовленням
order = """

<i>Назва:</i> <b>{}</b>

<i>Опис:</i> <b>{}</b>

<i>Вартість:</i> <b>{} грн за 1 од.</b>

<i>Кількість позицій:</i> <b>{} од.</b>
"""

order_number = """

<b>Позиція на замовлення № </b> <i>{}</i>

"""
# відповідь користувачу, коли замовлення немає
no_orders = """
<b>Замовлення відсутнє !!!</b>
"""
# відповідь користувачу під час підтвердження оформлення замовлення
applay = """
<b>Ваше замовлення оформлене !!!</b>

<i>Загальна вартість замовлення складає:</i> <b>{} грн</b>

<i>Загальна кількість позицій становить:</i> <b>{} од.</b>

<b>ЗАКАЗ НАПРЯМОК НА СКЛАД,
ДЛЯ ЙОГО КОМПЛЕКТУВАННЯ !!!</b>
"""
# словник відповідей користувачу
MESSAGES = {
     'trading_store': trading_store,
     'product_order': product_order,
     'order': order,
     'order_number': order_number,
     'no_orders': no_orders,
     'applay': applay,
     'settings': settings
}