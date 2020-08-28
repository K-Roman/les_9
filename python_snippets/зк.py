# Сделать генератор текста на основе статистики
# Идея проста: подсчитаем какие буквы наиболее часто стоят рядом
# Точнее, подсчитаем как часто за буковой Х идет буква У, на основе некоего текста.
# После этого начнем с произвольной буквы и каждую следующую будем выбирать в зависимости от
# частоты её появления в статистике.

import zipfile


from pprint import pprint
from random import randint


class Chatterer:
    analize_count = 4

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect(self):

        if self.file_name.endswith('.zip'):
            self.unzip()
        self.sequence = ' ' * self.analize_count
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self._collect_for_line(line = line[:-1])

    def _collect_for_line(self, line):
        for char in line:
            if self.sequence in self.stat:
                if char in self.stat[self.sequence]:
                    self.stat[self.sequence][char] += 1
                else:
                    self.stat[self.sequence][char] = 1
            else:
                self.stat[self.sequence] = {char: 1}
            self.sequence = self.sequence[1:] + char

    def prepare(self):
        self.totals = {}
        self.stat_for_generate = {}
        for sequence, char_stat in self.stat.items():
            self.totals[sequence] = 0
            self.stat_for_generate[sequence] = []
            for char, count in char_stat.items():
                self.totals[sequence] += count
                self.stat_for_generate[sequence].append([count, char])
                self.stat_for_generate[sequence].sort(reverse=True)

    def chat(self, N, out_file_name=None):
        N = 1000
        printed = 0
        if out_file_name is not None:
            file = open(out_file_name, 'w', encoding='utf8')
        else:
            file = None
        sequence = ' ' * self.analize_count
        space_printed = 0
        while printed < N:
            char = self._get_char(char_stat=self.stat_for_generate[sequence], total=self.totals[sequence])
            if file:
                file.write(char)
            else:
                print(char, end='')
            if char == ' ':
                space_printed += 1
                if space_printed >= 10:
                    if file:
                        file.write('\n')
                    else:
                        print()
                    space_printed = 0
            printed += 1
            sequence = sequence[1:] + char
        if file:
            file.close()

    def _get_char(self, char_stat, total):
        dice = randint(1, total)
        pos = 0
        for count, char in char_stat:
            pos += count
            if dice <= pos:
                break
        return char


chaterer = Chatterer(file_name="voyna-i-mir.txt")
chaterer.collect()
chaterer.prepare()
chaterer.chat(N=10000, out_file_name='out.txt')







# file_name = "voyna-i-mir.txt"
#
# stat = {}
# stat = {'а' : {'т' : 500, 'х' : 5,}, 'т': {'о' : 100, 'у' : 50,}}


# pprint(stat)
# pprint(len(stat))



# N = 1000
# printed = 0
# sequence = ' ' * analize_count
# space_printed = 0
# while printed < N:
#     char_stat = stat_for_generate[sequence]
#     total = totals[sequence]
#     dice = randint(1, total)
#     pos = 0
#     for count, char in char_stat:
#         pos += count
#         if dice <= pos:
#             break
#     print(char, end='')
#     if char == ' ':
#         space_printed +=1
#         if space_printed >= 10:
#             print()
#             space_printed = 0
#     printed += 1
#     sequence = sequence[1:] + char




# pprint(totals)
# pprint(stat_for_generate)

