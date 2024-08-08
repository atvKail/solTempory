from UrTube import *
from Video import *
from User import *
from hash import *

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')


# # Хеширование пароля
# password = "sdaklsdkasd"
# salt, hashed_password = custom_hash(password)

# print(f"Соль: {salt.hex()}")
# print(f"Хеш пароля: {hashed_password.hex()}")

# # Проверка пароля
# is_correct = verify_password(hashed_password, salt, "sdaklsdkasd")
# print(f"Пароль правильный: {is_correct}")

# # Проверка неверного пароля
# is_incorrect = verify_password(hashed_password, salt, "wrongpassword")
# print(f"Пароль неправильный: {is_incorrect}")
