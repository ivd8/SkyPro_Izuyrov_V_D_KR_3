
from def_urok_6 import writ_words, shuffle_words, ask_questions, writ_file, statistics_output

user_name = input('Введите ваше имя: ')
words = writ_words('words.txt')
words_mix = shuffle_words(words)
statistical_data = ask_questions(words_mix, words) + user_name
writ_file(statistical_data)
print(statistics_output('history.txt'))