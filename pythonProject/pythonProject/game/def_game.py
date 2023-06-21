file_txt = 'lightning-roulette.txt'

def read_file():
    ''' Функция переводит txt в список
    Вход: txt
    Выход: list
    '''


    files = []
    with open(file_txt, 'r') as f:
        for line in f.readlines():
            f_1 = line.strip('\n')
            f_2 = f_1.replace('\t',' ')
            files.append(f_2.split(' '))
            files.reverse()
    return files

def columns_win(file_list):
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
