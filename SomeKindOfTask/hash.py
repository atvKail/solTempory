import hashlib
import os

def generate_salt(length=16):
    return os.urandom(length)

def custom_hash(password, salt=None, iterations=100000):
    """
    Хеширование пароля с использованием соли и многократного хеширования.

    :param password: Пароль для хеширования (строка).
    :param salt: Соль, если не передана, создается новая (байты).
    :param iterations: Количество итераций хеширования.
    :return: Кортеж (salt, hashed_password), где оба значения в виде байтов.
    """
    if salt is None:
        salt = generate_salt()

    password_bytes = password.encode('utf-8')

    hashed = hashlib.pbkdf2_hmac('sha256', password_bytes, salt, iterations)

    return salt, hashed

def verify_password(stored_password, stored_salt, provided_password, iterations=100000):
    """Проверка соответствия введенного пароля и сохраненного хеша."""
    _, new_hash = custom_hash(provided_password, stored_salt, iterations)
    return new_hash == stored_password
