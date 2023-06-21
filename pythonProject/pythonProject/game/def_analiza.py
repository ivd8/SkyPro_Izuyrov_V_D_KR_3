
lightning_roulette_file = '../caseno/Analiz_v_0_1/lightning-roulette.txt'

def read_file():
    ''' Функция переводит txt в список
    Вход: txt
    Выход: list
    '''


    files = []
    with open(lightning_roulette_file, 'r') as f:
        for line in f.readlines():
            f_1 = line.strip('\n')
            f_2 = f_1.replace('\t',' ')
            files.append(f_2.split(' '))
    return files

def columns(file_list):
    '''
    Функция определяет теги columns и записывает в список
    :param file_list, list:
    :return ,list:
    '''

    zero = 0
    columns_3 = '3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36'
    columns_2 = '2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35'
    columns_1 = '1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34'

    file = []
    for list_st_2 in file_list:
        if int(list_st_2[2]) == zero:
            list_st_2.append('zero')
            file.append(list_st_2)

        elif list_st_2[2] in columns_3:
            list_st_2.append('columns_3')
            file.append(list_st_2)

        elif list_st_2[2] in columns_2:
            list_st_2.append('columns_2')
            file.append(list_st_2)

        elif list_st_2[2] in columns_1:
            list_st_2.append('columns_1')
            file.append(list_st_2)
        else:
            continue
    return file

def counter_col(columns_tag):
    columns_3 = 'columns_3'
    columns_2 = 'columns_2'
    columns_1 = 'columns_1'

    counter_3 = 0
    counter_2 = 0
    counter_1 = 0
    counter_zero = 0

    counter_3_list = []
    counter_2_list = []
    counter_1_list = []
    counter_zero_list = []

    compl_columns = {}

    for i in columns_tag:

        if i[3] == 'columns_3' or i[3] == 'columns_2' or i[3] == 'columns_1':
            if i[3] == columns_3:
                if counter_zero > 0:
                    counter_zero_list.append(counter_zero)
                counter_zero = 0
                counter_3 += 1
                if counter_2 > 0:
                    counter_2_list.append(counter_2)
                counter_2 = 0
                if counter_1 > 0:
                    counter_1_list.append(counter_1)
                counter_1 = 0

            elif i[3] == columns_2:
                if counter_zero > 0:
                    counter_zero_list.append(counter_zero)
                counter_zero = 0
                if counter_3 > 0:
                    counter_3_list.append(counter_3)
                counter_3 = 0
                counter_2 += 1
                if counter_1 > 0:
                    counter_1_list.append(counter_1)
                counter_1 = 0

            elif i[3] == columns_1:
                if counter_zero > 0:
                    counter_zero_list.append(counter_zero)
                counter_zero = 0
                if counter_3 > 0:
                    counter_3_list.append(counter_3)
                counter_3 = 0
                if counter_2 > 0:
                    counter_2_list.append(counter_2)
                counter_2 = 0
                counter_1 += 1
        else:
            counter_zero += 1
            if counter_3 > 0:
                counter_3_list.append(counter_3)
            counter_3 = 0
            if counter_2 > 0:
                counter_2_list.append(counter_2)
            counter_2 = 0
            if counter_3 > 0:
                counter_1_list.append(counter_1)
            counter_1 = 0

    compl_columns['counter_3_list'] = counter_3_list
    compl_columns['counter_2_list'] = counter_2_list
    compl_columns['counter_1_list'] = counter_1_list
    compl_columns['counter_zero_list'] = counter_zero_list
    return compl_columns

def nam_tag(file):
    counter_3_list_max = max(file['counter_3_list'])
    counter_2_list_max = max(file['counter_2_list'])
    counter_1_list_max = max(file['counter_1_list'])
    counter_zero_list_max = max(file['counter_zero_list'])
    print(counter_3_list_max)
    print(counter_2_list_max)
    print(counter_1_list_max)
    print(counter_zero_list_max)












# red(Красное) / Black(чёрное)
    # red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    # black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

# Even(Чётное) / Odd(нечётное)
    #Even = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    #Odd = [1, 3, 5, 7, 9, 11, 13, 15, 16, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]

# Dozens(Дюжины)
    #d_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    #d_2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    #d_3 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

# Columns(Колонны)
    #Columns_3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
    #Columns_2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    #Columns_1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]

#1 to 18 Малые Low(меньше)/Manqu(больше)
    #low_manqu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

#19 to 36 Большие High(меньше)/Passe(больше)
    #high_passe = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

# Red Snake(красная змея)
    #red_snake = [1, 5, 9, 12, 14, 16, 19, 23, 27, 30, 32, 34]


stav_x = 1
stav_y = 2
z_x = 1
z_y = 1
z = 1000

columns_3_count = 0
columns_2_count = 0
columns_1_count = 0
count = 0
if columns_1_count < columns_3_count < columns_2_count:
    x_2 = 2
else

for i in file_list:
    win = 0
    stav_1 = win
    stav_2 =

    if i[3] in columns_3:
        win = 3
        columns_3_count = 0
        columns_2_count += 1
        columns_1_count += 1

    elif i[3] in columns_2:
        win = 2
        columns_3_count += 1
        columns_2_count = 0
        columns_1_count += 1

    elif i[3] in columns_1:
        win = 1
        columns_3_count += 1
        columns_2_count += 1
        columns_1_count = 0
    else:
        win = 0
        columns_3_count += 1
        columns_2_count += 1
        columns_1_count += 1





