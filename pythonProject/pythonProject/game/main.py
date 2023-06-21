from def_game import read_file, columns_win
from def_proba import proba

file_list = read_file()
teg = columns_win(file_list)
proba_1 = proba(teg)
print(proba_1)
