
from def_dz_urok_6 import get_is_file, questions_displays_statistics, score_check, result_record





count_glob = 0
name = input('Введите ваше имя: ')

for i in range(4):
    word = get_is_file()
    print(word)
    count_glob += questions_displays_statistics(word)

result = f'{name}:{count_glob} \n'
check_result = score_check(result)
print(check_result)
result_record(result)

