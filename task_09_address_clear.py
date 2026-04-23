#вводим адреса
addresses = [
    "  г. Москва, ул. Ленина, д. 10 ",
    "г.Казань,ул.Баумана,д.15",
    "  г. Санкт-Петербург, ул. Невский, д. 100 "
]
#удаляем лишние пробелы, добавляем пробелы после сокращений, унифицируем запятые
for i, addr in enumerate(addresses, 1):
    original = addr
    cleaned = addr.strip()
    cleaned = cleaned.replace("г.", "г. ")
    cleaned = cleaned.replace("ул.", "ул. ")
    cleaned = cleaned.replace("д.", "д. ")
    while "  " in cleaned:
        cleaned = cleaned.replace("  ", " ")
    cleaned = cleaned.replace(" ,", ",")
    cleaned = cleaned.replace(",", ", ")
    while "  " in cleaned:
        cleaned = cleaned.replace("  ", " ")
#выводим исправленные адреса
    print(f"#{i}")
    print(f"ДО  : '{original}'")
    print(f"ПОСЛЕ: '{cleaned}'")
