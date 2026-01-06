#Рабочий код для Битрикс 24
# Получение данных сделки
import requests

BITRIX_WEBHOOK = "https://Вебхук/"
DEAL_ID = 421 # ID сделки

# Получение данных сделки
response = requests.get(f"{BITRIX_WEBHOOK}/crm.item.get", params={'entityTypeId': 2, 'id': DEAL_ID})
deal_data = response.json()

if 'result' in deal_data:
    fields = deal_data['result']['item']
    print("Данные сделки:", fields)
else:
    print(f"Ошибка при получении данных сделки: {deal_data}")