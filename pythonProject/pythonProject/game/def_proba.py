def proba(list):
    count_win_glob = 0
    count_loss_glob = 0

    stavka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    count_win = 0
    count_loss = 0

    stavka_1 = ['columns_3']
    stavka_2 = ['columns_1']

    print(f'count_loss {count_loss}')
    count_columns_3 = 0
    count_columns_2 = 0
    count_columns_1 = 0
    count_zero = 0

    for i in list:


        print(count_columns_3)
        print(count_columns_2)
        print(count_columns_1)
        print(count_zero)

        balans = 1000
        stavka_1_d = stavka[count_loss]
        stavka_2_d = stavka[count_loss]


        if i[3] == 'columns_3':
            if stavka_1[0] == i[3] or stavka_2[0] == i[3]:
                balans += stavka[count_loss] * 3
                print(type(stavka[count_loss]))

                print(f'''\nВы выйграли
                Выйграла: {i[3]}
                {stavka_1}
                {stavka_2}
                Cумма: +{stavka[count_loss] * 3}
                Ваш баланс: {balans}''')

                count_win_glob += 1
                count_win += 1
                count_loss = 0
                win = i[3]
                stavka_1.clear()
                stavka_1.append(win)
                if count_columns_3 >= count_columns_2 >= count_columns_1:
                    stavka_2.clear()
                    stavka_2.append('columns_3')
                elif count_columns_2 >= count_columns_3 >= count_columns_2:
                    stavka_2.clear()
                    stavka_2.append('columns_2')
                elif count_columns_1 >= count_columns_2 >= count_columns_3:
                    stavka_2.clear()
                    stavka_2.append('columns_1')
                count_columns_3 = 0
                count_columns_2 += 1
                count_columns_1 += 1
                count_zero += 0
            elif stavka_1[0] != i[3] or stavka_2[0] != i[3]:
                balans -= stavka_2_d + stavka_1_d

                print(f'''\nВы проиграли
                Выйграла: {i[3]}
                {stavka_1}
                {stavka_2}
                Cумма: -{stavka_2_d + stavka_1_d}
                Ваш баланс: {balans}''')

                count_loss_glob += 1
                count_loss += 1
                win = i[3]
                stavka_1.clear()
                stavka_1.append(win)
                if count_columns_3 >= count_columns_2 >= count_columns_1:
                    stavka_2.clear()
                    stavka_2.append('columns_3')
                elif count_columns_2 >= count_columns_3 >= count_columns_2:
                    stavka_2.clear()
                    stavka_2.append('columns_2')
                elif count_columns_1 >= count_columns_2 >= count_columns_3:
                    stavka_2.clear()
                    stavka_2.append('columns_1')
                count_columns_3 = 0
                count_columns_2 += 1
                count_columns_1 += 1
                count_zero += 0

        elif i[3] == 'columns_2':
            if stavka_1[0] == i[3] or stavka_2[0] == i[3]:
                balans += stavka[count_loss] * 3
                print(type(stavka[count_loss]))

                print(f'''\nВы выйграли
                Выйграла: {i[3]}
                {stavka_1}
                {stavka_2}
                Cумма: +{stavka[count_loss] * 3}
                Ваш баланс: {balans}''')

                count_win_glob += 1
                count_win += 1
                count_loss = 0
                win = i[3]
                stavka_1.clear()
                stavka_1.append(win)
                if count_columns_3 >= count_columns_2 >= count_columns_1:
                    stavka_2.clear()
                    stavka_2.append('columns_3')
                elif count_columns_2 >= count_columns_3 >= count_columns_2:
                    stavka_2.clear()
                    stavka_2.append('columns_2')
                elif count_columns_1 >= count_columns_2 >= count_columns_3:
                    stavka_2.clear()
                    stavka_2.append('columns_1')
                count_columns_3 += 1
                count_columns_2 = 0
                count_columns_1 += 1
                count_zero += 0

            elif stavka_1[0] != i[3] or stavka_2[0] != i[3]:
                balans -= stavka_2_d + stavka_1_d

                print(f'''\nВы проиграли
                Выйграла: {i[3]}
                {stavka_1}
                {stavka_2}
                Cумма: -{stavka_2_d + stavka_1_d}
                Ваш баланс: {balans}''')

                count_loss_glob += 1
                count_loss += 1
                win = i[3]
                stavka_1.clear()
                stavka_1.append(win)
                if count_columns_3 >= count_columns_2 >= count_columns_1:
                    stavka_2.clear()
                    stavka_2.append('columns_3')
                elif count_columns_2 >= count_columns_3 >= count_columns_2:
                    stavka_2.clear()
                    stavka_2.append('columns_2')
                elif count_columns_1 >= count_columns_2 >= count_columns_3:
                    stavka_2.clear()
                    stavka_2.append('columns_1')
                count_columns_3 += 1
                count_columns_2 = 0
                count_columns_1 += 1
                count_zero += 0

        elif i[3] == 'columns_1':
            if stavka_1[0] == i[3] or stavka_2[0] == i[3]:
                balans += stavka[count_loss] * 3
                print(type(stavka[count_loss]))
                print(f'''\nВы выйграли
                Выйграла: {i[3]}
                {stavka_1}
                {stavka_2}
                Cумма: +{stavka[count_loss] * 3}
                Ваш баланс: {balans}''')

                count_win_glob += 1
                count_win += 1
                count_loss = 0
                balans += stavka[count_loss] * 3
                win = i[3]
                stavka_1.clear()
                stavka_1.append(win)
                if count_columns_3 >= count_columns_2 >= count_columns_1:
                    stavka_2.clear()
                    stavka_2.append('columns_3')
                elif count_columns_2 >= count_columns_3 >= count_columns_2:
                    stavka_2.clear()
                    stavka_2.append('columns_2')
                elif count_columns_1 >= count_columns_2 >= count_columns_3:
                    stavka_2.clear()
                    stavka_2.append('columns_1')
                count_columns_3 += 1
                count_columns_2 += 1
                count_columns_1 = 0
                count_zero += 0

            elif stavka_1[0] != i[3] or stavka_2[0] != i[3]:
                balans -= stavka_2_d + stavka_1_d

                print(f'''\nВы проиграли
                Выйграла: {i[3]}
                {stavka_1}
                {stavka_2}
                Cумма: -{stavka_2_d + stavka_1_d}
                Ваш баланс: {balans}''')

                count_loss_glob += 1
                count_loss += 1
                win = i[3]
                stavka_1.clear()
                stavka_1.append(win)
                if count_columns_3 >= count_columns_2 >= count_columns_1:
                    stavka_2.clear()
                    stavka_2.append('columns_3')
                elif count_columns_2 >= count_columns_3 >= count_columns_2:
                    stavka_2.clear()
                    stavka_2.append('columns_2')
                elif count_columns_1 >= count_columns_2 >= count_columns_3:
                    stavka_2.clear()
                    stavka_2.append('columns_1')
                count_columns_3 += 1
                count_columns_2 += 1
                count_columns_1 = 0
                count_zero += 0

        if i[3] == 'zero':
            if stavka_1[0] != i[3] or stavka_2[0] != i[3]:
                balans -= stavka_2_d + stavka_1_d
                print(f'''\nВы проиграли
                Выйграла: {i[3]}
                {stavka_1}
                {stavka_2}
                Cумма: -{stavka_2_d + stavka_1_d}
                Ваш баланс: {balans}''')
                count_loss_glob += 1
                count_loss += 1
                stavka_1.clear()
                stavka_1.append(win)
                if count_columns_3 >= count_columns_2 >= count_columns_1:
                    stavka_2.clear()
                    stavka_2.append('columns_3')
                elif count_columns_2 >= count_columns_3 >= count_columns_2:
                    stavka_2.clear()
                    stavka_2.append('columns_2')
                elif count_columns_1 >= count_columns_2 >= count_columns_3:
                    stavka_2.clear()
                    stavka_2.append('columns_1')
                count_columns_3 += 1
                count_columns_2 += 1
                count_columns_1 += 1
                count_zero += 0

    print(count_win_glob)
    print(count_loss_glob)



