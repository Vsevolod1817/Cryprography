# № 8 Реализовать криптосистему
# RSA
# для шифрования и
# расшифрования вводимых сообщений. Открытый ключ показывать
# пользователю, закрытый ключ записывать в файл.

from sympy import randprime, gcd

# Функция для генерации ключей RSA
def Generation():
    # Генерируем два простых числа
    p = randprime(100, 1000)
    q = randprime(100, 1000)
    while q == p:
        q = randprime(100, 1000)
        # Вычисляем n и функцию Эйлера от n (phi)
    n = p * q
    phi = (p - 1) * (q - 1)
    # Выбираем e, взаимно простое с phi
    e = 2
    while gcd(e, phi) != 1:
        e += 1
        # Вычисляем d, обратное к e по модулю phi
    d = pow(e, -1, phi)
    # Возвращаем открытый и закрытый ключи
    return ((e, n), (d, n))

# Функция для расшифровки
def Decrypt(cipher_text, private_key):
    d, n = private_key
    # Расшифровываем сообщение, применяя преобразование RSA
    decrypted_msg = [chr(pow(char, d, n)) for char in cipher_text]
    return ''.join(decrypted_msg)

# Функция для шифрования
def Encrypt(message, public_key):
    e, n = public_key
    # Шифруем сообщение, применяя преобразование RSA
    encrypted_msg = [pow(ord(char), e, n) for char in message]
    return encrypted_msg

# Генерация ключей
pub_key, pri_key = Generation()
# Показываем открытый ключ
print(f'Публичный ключ: {pub_key}')
# Рассказываем о закрытом ключе
print(f'\nЗакрытый ключ записывается в файл private_key.txt')
# Запись закрытого ключа в файл
private_key_path = "C:\Cryptography\LR\private_key.txt"
with open(private_key_path, "w+") as file:
    file.write(f"({pri_key[0]}, {pri_key[1]})")
# print(f"private key: {private_key}")
msg = input("Сообщение: ")
# Шифрование
cipher_text = Encrypt(msg, pub_key)
print("Зашифрованное сообщение:", cipher_text)
# Расшифровка
decrypted_msg = Decrypt(cipher_text, pri_key)
print("Расшифрованное сообщение:", decrypted_msg)