# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
from pprint import pprint
import os

stat = {}

file_name = "python_snippets\\voyna-i-mir.txt"

with open(file_name, 'r', encoding='cp1251') as file:
    for line in file:
        for char in line:
            if char.isalpha() and char in stat:
                stat[char] += 1
            elif char.isalpha() and char not in stat:
                stat[char] = 0
            else:
                continue

list_keys = list(stat.keys())
list_keys.sort()

print('+','-'*10,'+','-'*10,'+')
print('|{item:^12}|{val:^12}|'.format(item="буква", val="частота"))
print('+','-'*10,'+','-'*10,'+')
all = 0
for item in list_keys:
    all += stat[item]
    print('|{item:^12}|{val:^12}|'.format(item=item, val=stat[item]))

print('+','-'*10,'+','-'*10,'+')
print('|{item:^12}|{val:^12}|'.format(item="итого", val=all))
print('+','-'*10,'+','-'*10,'+')


# 2374102

