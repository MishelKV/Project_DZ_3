import threading
import time

Total_enemies = 100

class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.remaining_warrior = Total_enemies
        self.day_counter = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.remaining_warrior > 0:
            time.sleep(1)
            self.remaining_warrior -= self.power
            self.day_counter += 1
            print(f"{self.name}, сражается {self.day_counter} день(дня), осталось {self.remaining_warrior} воинов.")

        print(f"{self.name}, одержал победу спустя {self.day_counter} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")