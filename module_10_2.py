
import threading as thr
import time as tm

class Knight(thr.Thread):
    def __init__(self, name, power):
        thr.Thread.__init__(self)
        self.name = name
        self.power = power

    def timer(self, name, power):
        enemies = 100
        counter = 0
        while enemies > 0:
            tm.sleep(1)
            enemies -= self.power
            counter += 1
            print(f'{self.name} сражается {counter} день(дня)..., осталось {enemies} врагов \n')
        return counter

    def run(self):
        print(f'{self.name}, на нас напали!')
        counter = self.timer(self.name, self.power)
        print(f'{self.name} одержал победу спустя {counter} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились')