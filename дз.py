


class Analysis:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}

    def collection(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha() and char in self.stat:
                        self.stat[char] += 1
                    elif char.isalpha() and char not in self.stat:
                        self.stat[char] = 0
                    else:
                        continue

    def sort_frequency_up(self):
        #  - по частоте по возрастанию
        #  - по алфавиту по возрастанию
        #  - по алфавиту по убыванию
        self.list1 = list(self.stat.items())
        self.list1.sort(key=lambda i:i[1])

    def sort_frequency_down(self):
        self.list1 = list(self.stat.items())
        self.list1.sort(key=lambda i: i[1], reverse=True)

    def sort_alfa_down(self):
            self.list1 = list(self.stat.items())
            self.list1.sort(reverse=True)


    def vivod(self):

        print('+', '-' * 10, '+', '-' * 10, '+')
        print('|{item:^12}|{val:^12}|'.format(item="буква", val="частота"))
        print('+', '-' * 10, '+', '-' * 10, '+')
        all = 0
        for item in self.list1:
            all += item[1]
            print('|{item:^12}|{val:^12}|'.format(item=item[0], val=item[1]))

        print('+', '-' * 10, '+', '-' * 10, '+')
        print('|{item:^12}|{val:^12}|'.format(item="итого", val=all))
        print('+', '-' * 10, '+', '-' * 10, '+')

analiz = Analysis(file_name = "python_snippets\\voyna-i-mir.txt")
analiz.collection()
analiz.sort_frequency_down()
analiz.vivod()