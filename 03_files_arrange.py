# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


class FotoSort:


    def __init__(self,folder_in,folder_out):

        self.folder_in = folder_in
        self.folder_out = folder_out
        self.list_date = []

    def prohod(self):
        for dirpath, dirnames, filenames in os.walk(self.folder_in):
            for file in filenames:
                self.full_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(self.full_path)
                self.file_time = time.gmtime(secs)
                # print(self.file_time)
                if (self.file_time[0], self.file_time[1]) not in self.list_date:
                    self.list_date.append((self.file_time[0], self.file_time[1]))
                else:
                    continue
        # print(self.list_date)

    def create(self):
        for item in self.list_date:
            path = '{}\\{}\\{}'.format(self.folder_out, item[0], item[1])
            print(path)
            if os.path.exists(path):
                continue
            else:
                os.makedirs(path)

    def copy_icons(self):
        for dirpath, dirnames, filenames in os.walk(self.folder_in):
            for file in filenames:
                self.full_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(self.full_path)
                self.file_time = time.gmtime(secs)
                item_path = os.path.join(self.folder_out, str(self.file_time[0]), str(self.file_time[1]))
                print(item_path)
                shutil.copy2(self.full_path, item_path)

v1 = FotoSort('icons', 'icons_by_year')
v1.prohod()
v1.create()
v1.copy_icons()


# v1.copy_icons()
