# № 8 Реализовать программный продукт построения sha-384 для введенного
# текста.


import hashlib


def generate_sha384_hash(input_text):
    # Создание объекта хэша SHA-384
    sha384_hash = hashlib.sha384()

    # Кодирование введённого текста в байты и обновление объекта хэша
    sha384_hash.update(input_text.encode('utf-8'))

    # Получение хэша в виде шестнадцатеричной строки
    hex_dig = sha384_hash.hexdigest()

    return hex_dig


# Запрос ввода текста от пользователя
input_text = input("Введите текст для генерации SHA-384 хэша: ")

print(f'Введенный текст: {input_text}')

# Генерация и вывод хэша
print("SHA-384 хэш введённого текста:", generate_sha384_hash(input_text))