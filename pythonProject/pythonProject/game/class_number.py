class Number:
    """ Класс числа"""

    def __init__(self, namber):
        self.namber = int(namber)


    def number_characteristic(self):
        """
        Для Анализа больших массивов
        Метод определяет цвет, четность, дюжену, колону, размер выйгравшего числа

        Вход: Список с выйграшных номеров без Тегов, list.
        Выход: Список выйграшных номеров с Тегами, list.
        """

        self.characteristic = [
            ['zero', 'zero', 'zero', 'zero', 'zero'],  # 0
            ['red', 'odd', 'dozens_1', 'columns_1', '1 to 18'],  # 1
            ['black', 'even', 'dozens_1', 'columns_2', '1 to 18'],  # 2
            ['black', 'even', 'dozens_1', 'columns_1', '1 to 18'],  # 3
            ['red', 'odd', 'Dozens_1', 'columns_2', '1 to 18'],  # 4
            ['red', 'odd', 'dozens_1', 'columns_3', '1 to 18'],  # 5
            ['black', 'even', 'dozens_1', 'columns_3', '1 to 18'],  # 6
            ['red', 'odd', 'dozens_1', 'columns_1', '1 to 18'],  # 7
            ['black', 'even', 'dozens_1', 'columns_2', '1 to 18'],  # 8
            ['red', 'odd', 'dozens_1', 'columns_1', '1 to 18'],  # 9
            ['black', 'even', 'dozens_1', 'columns_2', '1 to 18'],  # 10
            ['red', 'odd', 'dozens_1', 'columns_3', '1 to 18'],  # 11
            ['black', 'even', 'dozens_1', 'columns_1', '1 to 18'],  # 12
            ['red', 'odd', 'dozens_2', 'columns_2', '1 to 18'],  # 13
            ['black', 'even', 'dozens_2', 'columns_3', '1 to 18'],  # 14
            ['red', 'odd', 'dozens_2', 'columns_1', '1 to 18'],  # 15
            ['black', 'even', 'dozens_2', 'columns_2', '1 to 18'],  # 16
            ['black', 'odd', 'dozens_2', 'columns_3', '1 to 18'],  # 17
            ['red', 'even', 'dozens_2', 'columns_1', '1 to 18'],  # 18
            ['red', 'odd', 'dozens_2', 'columns_2', '19 to 36'],  # 19
            ['black', 'even', 'dozens_2', 'columns_3', '19 to 36'],  # 20
            ['red', 'odd', 'dozens_2', 'columns_1', '19 to 36'],  # 21
            ['black', 'even', 'dozens_2', 'columns_2', '19 to 36'],  # 22
            ['red', 'odd', 'dozens_2', 'columns_3', '19 to 36'],  # 23
            ['black', 'even', 'dozens_2', 'columns_1', '19 to 36'],  # 24
            ['red', 'odd', 'dozens_3', 'columns_2', '19 to 36'],  # 25
            ['black', 'even', 'dozens_3', 'columns_3', '19 to 36'],  # 26
            ['red', 'odd', 'dozens_3', 'columns_1', '19 to 36'],  # 27
            ['black', 'even', 'dozens_3', 'columns_2', '19 to 36'],  # 28
            ['black', 'odd', 'dozens_3', 'columns_3', '19 to 36'],  # 29
            ['red', 'even', 'dozens_3', 'columns_1', '19 to 36'],  # 30
            ['black', 'odd', 'dozens_3', 'columns_2', '19 to 36'],  # 31
            ['red', 'even', 'dozens_3', 'columns_3', '19 to 36'],  # 32
            ['black', 'odd', 'dozens_3', 'columns_1', '19 to 36'],  # 33
            ['red', 'even', 'dozens_3', 'columns_2', '19 to 36'],  # 34
            ['black', 'odd', 'dozens_3', 'columns_3', '19 to 36'],  # 35
            ['red', 'even', 'dozens_3', 'columns_1', '19 to 36']  # 36
        ]
        self.characteristic[self.namber].append(str(self.namber))
        return self.characteristic[self.namber]

    def tag_count(self, lists_characteristic):
        '''
        Для Анализа больших массивов
        Метод считает сколько раз подряд было или небыло определенного Тега,
        разбивает по разным спискам в зависемости от Тегов.

        Вход: Список с выйграшных номеров с тегами, list.
        Выход: Словарь со списками количество подряд выпавших и не выпавших Тегов, dict.
        '''

        # Только для анализа прошедших игр, в словарь добавляется с
        # задержкой в 1 ход, для динамичной игры нужно будет перебрать

        self.lists_characteristic = lists_characteristic

        lists_tag = {}

        list_zero_several_row = []
        list_zero_not_have = []

        list_red_several_row = []
        list_red_not_have = []
        list_black_several_row = []
        list_black_not_have = []

        list_even_several_row = []
        list_even_not_have = []
        list_odd_several_row = []
        list_odd_not_have = []

        list_dozens_1_several_row = []
        list_dozens_1_not_have = []
        list_dozens_2_several_row = []
        list_dozens_2_not_have = []
        list_dozens_3_several_row = []
        list_dozens_3_not_have = []

        list_columns_1_several_row = []
        list_columns_1_not_have = []
        list_columns_2_several_row = []
        list_columns_2_not_have = []
        list_columns_3_several_row = []
        list_columns_3_not_have = []

        list_o1_to_18_several_row = []
        list_o1_to_18_not_have = []
        list_o19_to_36_several_row = []
        list_o19_to_36_not_have = []

        # zero
        zero_several_row = 0
        zero_not_have = 0

        # color
        red_several_row = 0
        red_not_have = 0
        black_several_row = 0
        black_not_have = 0

        # even/ odd
        even_several_row = 0
        even_not_have = 0
        odd_several_row = 0
        odd_not_have = 0

        # dozens
        dozens_1_several_row = 0
        dozens_1_not_have = 0
        dozens_2_several_row = 0
        dozens_2_not_have = 0
        dozens_3_several_row = 0
        dozens_3_not_have = 0

        # columns
        columns_1_several_row = 0
        columns_1_not_have = 0
        columns_2_several_row = 0
        columns_2_not_have = 0
        columns_3_several_row = 0
        columns_3_not_have = 0

        # big/ small
        o1_to_18_several_row = 0
        o1_to_18_not_have = 0
        o19_to_36_several_row = 0
        o19_to_36_not_have = 0

        for list in self.lists_characteristic:

            if list[0] == 'zero':
                zero_several_row += 1

                list_zero_not_have.append(zero_not_have)
                zero_not_have = 0

                red_not_have += 1
                black_not_have += 1
                even_not_have += 1
                odd_not_have += 1
                dozens_1_not_have += 1
                dozens_2_not_have += 1
                dozens_3_not_have += 1
                columns_1_not_have += 1
                columns_2_not_have += 1
                columns_3_not_have += 1
                o1_to_18_not_have += 1
                o19_to_36_not_have += 1
                continue
            else:
                list_zero_several_row.append(zero_several_row)
                zero_several_row = 0
                zero_not_have += 1

            if list[0] == 'red':
                red_several_row += 1
                list_red_not_have.append(red_not_have)
                red_not_have = 0
                list_black_several_row.append(black_several_row)
                black_several_row = 0
                black_not_have += 1
            else:
                black_several_row += 1
                list_black_not_have.append(black_not_have)
                black_not_have = 0
                list_red_several_row.append(red_several_row)
                red_several_row = 0
                red_not_have += 1

            if list[1] == 'even':
                even_several_row += 1
                list_even_not_have.append(even_not_have)
                even_not_have = 0
                list_odd_several_row.append(odd_several_row)
                odd_several_row = 0
                odd_not_have += 1
            else:
                odd_several_row += 1
                list_odd_not_have.append(odd_not_have)
                odd_not_have = 0
                list_even_several_row.append(even_several_row)
                even_several_row = 0
                even_not_have += 1

            if list[2] == 'dozens_1':
                dozens_1_several_row += 1
                list_dozens_1_not_have.append(dozens_1_not_have)
                dozens_1_not_have = 0
                list_dozens_2_several_row.append(dozens_2_several_row)
                dozens_2_several_row = 0
                list_dozens_3_several_row.append(dozens_3_several_row)
                dozens_3_several_row = 0
                dozens_2_not_have += 1
                dozens_3_not_have += 1
            elif list[2] == 'dozens_2':
                dozens_2_several_row += 1
                list_dozens_2_not_have.append(dozens_2_not_have)
                dozens_2_not_have = 0
                list_dozens_1_several_row.append(dozens_1_several_row)
                dozens_1_several_row = 0
                list_dozens_3_several_row.append(dozens_3_several_row)
                dozens_3_several_row = 0
                dozens_1_not_have += 1
                dozens_3_not_have += 1
            else:
                dozens_3_several_row += 1
                list_dozens_3_not_have.append(dozens_3_not_have)
                dozens_3_not_have = 0
                list_dozens_1_several_row.append(dozens_1_several_row)
                dozens_1_several_row = 0
                list_dozens_2_several_row.append(dozens_2_several_row)
                dozens_2_several_row = 0
                dozens_1_not_have += 1
                dozens_2_not_have += 1

            if list[3] == 'columns_1':
                columns_1_several_row += 1
                list_columns_1_not_have.append(columns_1_not_have)
                columns_1_not_have = 0
                list_columns_2_several_row.append(columns_2_several_row)
                columns_2_several_row = 0
                list_columns_3_several_row.append(columns_3_several_row)
                columns_3_several_row = 0
                columns_2_not_have += 1
                columns_3_not_have += 1
            elif list[3] == 'columns_2':
                columns_2_several_row += 1
                list_columns_2_not_have.append(columns_2_not_have)
                columns_2_not_have = 0
                list_columns_1_several_row.append(columns_1_several_row)
                columns_1_several_row = 0
                list_columns_3_several_row.append(columns_3_several_row)
                columns_3_several_row = 0
                columns_1_not_have += 1
                columns_3_not_have += 1
            else:
                columns_3_several_row += 1
                list_columns_3_not_have.append(columns_3_not_have)
                columns_3_not_have = 0
                list_columns_1_several_row.append(columns_1_several_row)
                columns_1_several_row = 0
                list_columns_2_several_row.append(columns_2_several_row)
                columns_2_several_row = 0
                columns_1_not_have += 1
                columns_2_not_have += 1

            if list[4] == '1 to 18':
                o1_to_18_several_row += 1
                list_o1_to_18_not_have.append(o1_to_18_not_have)
                o1_to_18_not_have = 0
                list_o19_to_36_several_row.append(o19_to_36_several_row)
                o19_to_36_several_row = 0
                o19_to_36_not_have += 1
            else:
                o19_to_36_several_row += 1
                list_o19_to_36_not_have.append(o19_to_36_not_have)
                o19_to_36_not_have = 0
                list_o1_to_18_several_row.append(o1_to_18_several_row)
                o1_to_18_several_row = 0
                o1_to_18_not_have += 1

        lists_tag = {'list_zero_several_row': list_zero_several_row,
                     'list_zero_not_have': list_zero_not_have,
                     'list_red_several_row': list_red_several_row,
                     'list_red_not_have': list_red_not_have,
                     'list_black_several_row': list_black_several_row,
                     'list_black_not_have': list_black_not_have,
                     'list_even_several_row': list_even_several_row,
                     'list_even_not_have': list_even_not_have,
                     'list_odd_several_row': list_odd_several_row,
                     'list_odd_not_have': list_odd_not_have,
                     'list_dozens_1_several_row': list_dozens_1_several_row,
                     'list_dozens_1_not_have': list_dozens_1_not_have,
                     'list_dozens_2_several_row': list_dozens_2_several_row,
                     'list_dozens_2_not_have': list_dozens_2_not_have,
                     'list_dozens_3_several_row': list_dozens_3_several_row,
                     'list_dozens_3_not_have': list_dozens_3_not_have,
                     'list_columns_1_several_row': list_columns_1_several_row,
                     'list_columns_1_not_have': list_columns_1_not_have,
                     'list_columns_2_several_row': list_columns_2_several_row,
                     'list_columns_2_not_have': list_columns_2_not_have,
                     'list_columns_3_several_row': list_columns_3_several_row,
                     'list_columns_3_not_have': list_columns_3_not_have,
                     'list_o1_to_18_several_row': list_o1_to_18_several_row,
                     'list_o1_to_18_not_have': list_o1_to_18_not_have,
                     'list_o19_to_36_several_row': list_o19_to_36_several_row,
                     'list_o19_to_36_not_have': list_o19_to_36_not_have
                     }
        return lists_tag

    def max_tag_count(self, tag_count):
        self.tag_count = tag_count
        self.max_tag_count = {}

        zero_max_several_row = max(self.tag_count['list_zero_several_row'])
        zero_max_not_have = max(self.tag_count['list_zero_max_not_have'])

        red_max_several_row = max(self.tag_count['list_red_max_several_row'])
        red_max_not_have = max(self.tag_count['list_red_max_not_have'])
        black_max_several_row = max(self.tag_count['list_black_max_several_row'])
        black_max_not_have = max(self.tag_count['list_black_max_not_have'])

        even_max_several_row = max(self.tag_count['list_even_max_several_row'])
        even_max_not_have = max(self.tag_count['list_even_max_not_have'])
        odd_max_several_row = max(self.tag_count['list_odd_max_several_row'])
        odd_max_not_have = max(self.tag_count['list_odd_max_not_have'])

        dozens_1_max_several_row = max(self.tag_count['list_dozens_1_max_several_row'])
        dozens_1_max_not_have = max(self.tag_count['list_dozens_1_max_not_have'])
        dozens_2_max_several_row = max(self.tag_count['list_dozens_2_max_several_row'])
        dozens_2_max_not_have = max(self.tag_count['list_dozens_2_max_not_have'])
        dozens_3_max_several_row = max(self.tag_count['list_dozens_3_max_several_row'])
        dozens_3_max_not_have = max(self.tag_count['list_dozens_3_max_not_have'])

        columns_1_max_several_row = max(self.tag_count['list_columns_1_max_several_row'])
        columns_1_max_not_have = max(self.tag_count['list_columns_1_max_not_have'])
        columns_2_max_several_row = max(self.tag_count['list_columns_2_max_several_row'])
        columns_2_max_not_have = max(self.tag_count['list_columns_2_max_not_have'])
        columns_3_max_several_row = max(self.tag_count['list_columns_3_max_several_row'])
        columns_3_max_not_have = max(self.tag_count['list_columns_3_max_not_have'])

        o1_to_18_max_several_row = max(self.tag_count['list_o1_to_18_max_several_row'])
        o1_to_18_max_not_have = max(self.tag_count['list_o1_to_18_max_not_have'])
        o19_to_36_max_several_row = max(self.tag_count['list_o19_to_36_max_several_row'])
        o19_to_36_max_not_have = max(self.tag_count['list_o19_to_36_max_not_have'])

        self.max_tag_count = {
            'zero_max_several_row': zero_max_several_row,
            'zero_max_not_have': zero_max_not_have,
            'red_max_several_row': red_max_several_row,
            'red_max_not_have': red_max_not_have,
            'black_max_several_row': black_max_several_row,
            'black_max_not_have': black_max_not_have,
            'even_max_several_row': even_max_several_row,
            'even_max_not_have': even_max_not_have,
            'odd_max_several_row': odd_max_several_row,
            'odd_max_not_have': odd_max_not_have,
            'dozens_1_max_several_row': dozens_1_max_several_row,
            'dozens_1_max_not_have': dozens_1_max_not_have,
            'dozens_2_max_several_row': dozens_2_max_several_row,
            'dozens_2_max_not_have': dozens_2_max_not_have,
            'dozens_3_max_several_row': dozens_3_max_several_row,
            'dozens_3_max_not_have': dozens_3_max_not_have,
            'columns_1_max_several_row': columns_1_max_several_row,
            'columns_1_max_not_have': columns_1_max_not_have,
            'columns_2_max_several_row': columns_2_max_several_row,
            'columns_2_max_not_have': columns_2_max_not_have,
            'columns_3_max_several_row': columns_3_max_several_row,
            'columns_3_max_not_have': columns_3_max_not_have,
            'o1_to_18_max_several_row': o1_to_18_max_several_row,
            'o1_to_18_max_not_have': o1_to_18_max_not_have,
            'o19_to_36_max_several_row': o19_to_36_max_several_row,
            'o19_to_36_max_not_have': o19_to_36_max_not_have
        }
        return self.max_tag_count

nam = Number(3)
print(nam.number_characteristic())

