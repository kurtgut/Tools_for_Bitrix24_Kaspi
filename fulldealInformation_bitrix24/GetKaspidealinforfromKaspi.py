# получение полной информации о сделке с Каспи по номеру
# Выводиться общая информация и Json информация
# Требует кредс
import requests
import creds
import json
from loguru import logger

order_code = 668909064

def get_order_by_code(order_code):
    url = f"https://kaspi.kz/shop/api/v2/orders?filter[orders][code]={order_code}"

    headers = {
        'User-Agent': 'Mozilla/5.0',
        'X-Auth-Token': creds.kaspi_token,
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status() # Вызов ошибки, если статус != 200
        data = response.json().get('data', [])
        if data:
            logger.info(f"Заказ {order_code} найден.")
            return data[0] # Возвращаем первый (и единственный) заказ
        else:
            logger.warning(f"Заказ с кодом {order_code} не найден.")
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка запроса: {e}")
        return None

#order_code = 672880905
order = get_order_by_code(order_code)

if order:
    # Вывод информации через print
    print("Информация о заказе:")
    print(f"Код заказа: {order['attributes']['code']}")
    print(f"ID заказа: {order['id']}")


    print(f"Дата создания: {order['attributes']['creationDate']}")
    print(f"Статус: {order['attributes']['status']}")
    print(f"Сумма: {order['attributes']['totalPrice']}")

    customer = order['attributes'].get('customer', {})
    print(f"Имя клиента: {customer.get('firstName', 'Не указано')}")
    print(f"Фамилия клиента: {customer.get('lastName', 'Не указано')}")
    print(f"Телефон клиента: {customer.get('cellPhone', 'Не указано')}")

    delivery_address = order['attributes'].get('deliveryAddress', {})
    print(f"Адрес доставки: {delivery_address.get('formattedAddress', 'Не указано')}")

    print(f"Способ доставки: {order['attributes'].get('deliveryMode', 'Не указано')}")
    print(f"Способ оплаты: {order['attributes'].get('paymentMode', 'Не указано')}")

    # Создание списка с информацией о заказе
    order_info = {
        "Код заказа": order['attributes']['code'],
        "ID заказа": order['id'],
        "Дата создания": order['attributes']['creationDate'],
        "Статус": order['attributes']['status'],
        "Сумма": order['attributes']['totalPrice'],
        "Имя клиента": customer.get('firstName', 'Не указано'),
        "Фамилия клиента": customer.get('lastName', 'Не указано'),
        "Телефон клиента": customer.get('cellPhone', 'Не указано'),
        "Адрес доставки": delivery_address.get('formattedAddress', 'Не указано'),
        "Способ доставки": order['attributes'].get('deliveryMode', 'Не указано'),
        "Способ оплаты": order['attributes'].get('paymentMode', 'Не указано')
    }


    # Вывод полной JSON-информации о заказе
    print("\nПолная JSON-информация о заказе:")
    print(json.dumps(order, indent=4, ensure_ascii=False))

else:
    print(f"Заказ с кодом {order_code} не найден.")