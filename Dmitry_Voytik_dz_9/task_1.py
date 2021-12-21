from time import sleep
from itertools import cycle


class TrafficLight:
    __color = ['  ', [7, 2, 4], ['\033[41m\033[1m', '\033[43m\033[1m', '\033[42m\033[1m']]

    def running(self):
        colors = ['', '']
        for i in cycle((0, 1, 2)):
            colors[1] = self.__color[2][i]
            print(f'\r[{colors[int(i == 0)]}{self.__color[0]}\033[0m]'
                  f'[{colors[int(i == 1)]}{self.__color[0]}\033[0m]'
                  f'[{colors[int(i == 2)]}{self.__color[0]}\033[0m]', end='')
            sleep(self.__color[1][i])


traffic_light = TrafficLight()
traffic_light.running()




# def out_red(text):
#     print("\033[31m {}" .format(text))
# def out_yellow(text):
#     print("\033[33m {}" .format(text))
# def out_blue(text):
#     print("\033[34m {}" .format(text))
# out_red("Вывод красным цветом")
# out_yellow("Текст жёлтого цвета")
# out_blue("Синий текст")
# print("\033[1m\033[32m\033[40m{}\033[0m".format("Python 3"))
