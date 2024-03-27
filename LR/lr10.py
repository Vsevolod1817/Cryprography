# № 8 Реализовать криптосистему
# RSA
# для шифрования и
# расшифрования вводимых сообщений. Открытый ключ показывать
# пользователю, закрытый ключ записывать в файл.

from sympy import randprime, gcd

# Функция для генерации ключей RSA
def generate_rsa_keys():
    # Генерируем два простых числа (в реальности должны быть гораздо больше)
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


# Функция для расшифровки сообщения
def decrypt_message(cipher_text, private_key):
    d, n = private_key
    # Расшифровываем сообщение, применяя преобразование RSA
    decrypted_msg = [chr(pow(char, d, n)) for char in cipher_text]
    return ''.join(decrypted_msg)

# Функция для шифрования сообщения
def encrypt_message(message, public_key):
    e, n = public_key
    # Шифруем сообщение, применяя преобразование RSA
    encrypted_msg = [pow(ord(char), e, n) for char in message]
    return encrypted_msg


# Генерируем ключи
public_key, private_key = generate_rsa_keys()

# Показываем открытый ключ пользователю
print(f'public key: {public_key}')

# Запись закрытого ключа в файл
private_key_path = "C:\Cryprography\LR\private_key.txt"
with open(private_key_path, "w+") as file:
    file.write(f"{private_key[0]}, {private_key[1]}")

# print(f"private key: {private_key}")

# Ввод сообщения
message = input("Введите сообщение для шифрования: ")

# Шифрование сообщения
cipher_text = encrypt_message(message, public_key)
print("Зашифрованное сообщение:", cipher_text)

# Расшифровка сообщения
decrypted_msg = decrypt_message(cipher_text, private_key)
print("Расшифрованное сообщение:", decrypted_msg)