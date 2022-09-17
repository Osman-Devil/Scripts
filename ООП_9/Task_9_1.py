from colorama import Fore
import time


class TrafficLight:
    def __init__(self):
        self.__color = ['красный', 'желтый', 'зелёный']

    def running(self):
        while True:
            if self.__color[0] == 'красный':
                print(Fore.RED + 'красный ')
                for sec in range(1, 8):
                    print(str(sec))
                    time.sleep(1)
                    sec += 1
            if self.__color[1] == 'желтый':
                print(Fore.YELLOW + 'жёлтый')
                for sec in range(1, 3):
                    print(str(sec))
                    time.sleep(1)
                    sec += 1
            if self.__color[2] == 'зелёный':
                print(Fore.GREEN + 'зелёный')
                for sec in range(1, 8):
                    print(str(sec))
                    time.sleep(1)
                    sec += 1
            break


a = TrafficLight()
a.running()


