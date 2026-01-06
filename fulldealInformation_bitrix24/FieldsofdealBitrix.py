#Рабочий код для Битрикс 24
# Получение пользовательских полей сделки
import requests

BITRIX_WEBHOOK = "https://Битрикс вебхук/"
CUSTOM_FIELD_CODE = "UF_CRM_1756986488157" # Код пользовательского поля

# Получение списка пользовательских полей сделки
response = requests.get(f"{BITRIX_WEBHOOK}/crm.deal.userfield.list")
fields = response.json().get('result', [])

# Проверка наличия поля
for field in fields:
    if field['FIELD_NAME'] == CUSTOM_FIELD_CODE: # Проверяем по ключу FIELD_NAME
        print(f"Поле найдено: {field}")
        break
else:
    print(f"Поле {CUSTOM_FIELD_CODE} не найдено.")