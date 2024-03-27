# № 8 Реализовать программный продукт, позволяющий подписывать и
# проверять подпись вводимого сообщения согласно схеме RSA. Возможно
# пользоваться встроенными библиотеками языков для хэш функции.


from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii

def generate_keys():
    """
    Генерация пары ключей RSA
    """
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def sign_message(private_key, message):
    """
    Подпись сообщения с использованием приватного ключа
    """
    rsakey = RSA.import_key(private_key)
    msg_hash = SHA256.new(message.encode())
    signer = pkcs1_15.new(rsakey)
    signature = signer.sign(msg_hash)
    return binascii.hexlify(signature).decode()

def verify_signature(public_key, message, signature):
    """
    Проверка подписи сообщения с использованием публичного ключа
    """
    rsakey = RSA.import_key(public_key)
    msg_hash = SHA256.new(message.encode())
    signature = binascii.unhexlify(signature)
    try:
        pkcs1_15.new(rsakey).verify(msg_hash, signature)
        return True
    except (ValueError, TypeError):
        return False

# Пример использования
private_key, public_key = generate_keys()

print(f'private key: {private_key}')
print(f'public key: {public_key}')

# Подпись сообщения
message = "Hello, World!"
print(f'message: {message}')
signature = sign_message(private_key, message)
print(f"Подпись: {signature}")

# Проверка подписи
verification_result = verify_signature(public_key, message, signature)
print(f"Результат проверки подписи: {'Успешно' if verification_result else 'Ошибка'}")