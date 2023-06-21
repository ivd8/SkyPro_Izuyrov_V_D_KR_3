from def_analiza import read_file, columns, counter_col, nam_tag

lightning_roulette_file = 'lightning-roulette.txt'

# редактирование txt в читаемый list
file_list = read_file()
columns_tag = columns(file_list)
counter_columns = counter_col(columns_tag)
counter = nam_tag(counter_columns)


# Добавление к словарю тегов
#tag_list = tag(file_list_st_2)



