from User import *
import time

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    
    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                return
        print("Неправильный логин или пароль")
    
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
    
    def log_out(self):
        self.current_user = None
    
    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)
    
    def get_videos(self, search_word):
        search_word = search_word.lower()
        return [video.title for video in self.videos if search_word in video.title.lower()]
    
    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=' ', flush=True)
                    time.sleep(1)  # Задержка в 1 секунду
                print("Конец видео")
                video.time_now = 0
                return
        
        print("Видео не найдено")
