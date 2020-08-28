# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


file_name = "events.txt"
file_name_out = "out3.txt"
list_out = []
stat_out = {}

class Parser:

    def __init__(self, file_name, file_name_out):
        self.file_name = file_name
        self.file_name_out = file_name_out

    def method(self):
        self.read()
        self.statistics()

    def read(self):
        with open(self.file_name, mode='r') as file:
            for line in file:
                if "NOK" in line:
                    list_out.append(line)

    def statistics(self):
        for i, item in enumerate(list_out):
            list_out[i] = item[0:17] + ']'
        set_of_time = set(list_out)
        for i, item in enumerate(set_of_time):
            stat_out[item] = list_out.count(item)

        with open(self.file_name_out, mode='w') as file:
            for key in stat_out:
                file.write("{} --> {}\n".format(key, stat_out[key]))


class SortHours(Parser):
    def statistics(self):
        for i, item in enumerate(list_out):
            list_out[i] = item[0:14] + ']'
        set_of_time = set(list_out)
        for i, item in enumerate(set_of_time):
            stat_out[item] = list_out.count(item)

        with open(self.file_name_out, mode='w') as file:
            for key in stat_out:
                file.write("{} --> {}\n".format(key, stat_out[key]))

class SortMonth(Parser):
    def statistics(self):
        for i, item in enumerate(list_out):
            list_out[i] = item[0:8] + ']'
        set_of_time = set(list_out)
        for i, item in enumerate(set_of_time):
            stat_out[item] = list_out.count(item)

        with open(self.file_name_out, mode='w') as file:
            for key in stat_out:
                file.write("{} --> {}\n".format(key, stat_out[key]))

pars1 = Parser(file_name = "events.txt",file_name_out = "out3.txt")
pars1.method()
print(list_out)





