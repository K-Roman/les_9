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

import zipfile
from pprint import pprint


class FotoSort:


    def __init__(self,folder_in,folder_out):

        self.folder_in = folder_in
        self.folder_out = folder_out
        self.name_path_time = {}

    def procedure(self):
        self.prohod()
        self.create()
        self.copy_icons()



    def prohod(self):
        for dirpath, dirnames, filenames in os.walk(self.folder_in):
            for file in filenames:
                self.full_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(self.full_path)
                self.file_time = time.gmtime(secs)
                self.name_path_time[file] = [self.full_path, str(self.file_time[0]), str(self.file_time[1])]
        # print(self.name_path_time)

    def create(self):
        for item in self.name_path_time:
            path = '{}\\{}\\{}'.format(self.folder_out, self.name_path_time[item][1], self.name_path_time[item][2])
            if os.path.exists(path):
                continue
            else:
                os.makedirs(path)

    def copy_icons(self):
        for item in self.name_path_time:
            item_path = os.path.join(self.folder_out, self.name_path_time[item][1], self.name_path_time[item][2])
            print(item_path)
            print(self.name_path_time[item][0])
            shutil.copy2(self.name_path_time[item][0], item_path)


class FotosortZip(FotoSort):

    # def __init__(self, zip_in, folder_out):
    #     # super().__init__(self, folder_out)
    #     self.zip_in = zip_in
    #     self.folder_out = folder_out

    def prohod(self):
        zfile = zipfile.ZipFile(self.folder_in, 'r')
        for info in zfile.infolist():
            if 'png' in info.filename:
                # self.full_path = os.path.join(info.filename,"1")
                # print(str(info.filename).rfind('/'))
                self.name_path_time[info.filename[info.filename.rfind('/')+1:]] = [info.filename,
                                                                                   str(info.date_time[0]),
                                                                                   str(info.date_time[1])]
        # pprint(self.name_path_time)

    def copy_icons(self):
        with zipfile.ZipFile(self.folder_in, 'r') as zfile:
            for info in zfile.infolist():
                if 'png' in info.filename:
                    path = '{}\\{}\\{}'.format(self.folder_out,
                                               self.name_path_time[info.filename[info.filename.rfind('/')+1:]][1],
                                               self.name_path_time[info.filename[info.filename.rfind('/')+1:]][2])
                    print(info)
                    info.filename = os.path.basename(info.filename)
                    # print(info.filename)
                    print(info)


                    zfile.extract(info, path=path)

    # def copy_icons(self):
    #     zfile = zipfile.ZipFile(self.folder_in, 'r')
    #     for item in self.name_path_time:
    #         path = '{}\\{}\\{}'.format(self.folder_out,
    #                                    self.name_path_time[item][1],
    #                                    self.name_path_time[item][2])
    #         file = item[item.rfind('/')+1:]
    #         zfile.extract(file, path=path)
    #     # zfile = zipfile.ZipFile(self.folder_in, 'r')
    #     # for info in zfile.infolist():
    #     #     if 'png' in info.filename:
    #     #         path =
    #     #     print(zfile.namelist())
    #     #     zfile.extract(member=filename,path= )




# v1 = FotoSort('icons', 'icons_by_year')
# v1.procedure()
#
v1 = FotosortZip('icons.zip', 'icons_by_year')
v1.procedure()

