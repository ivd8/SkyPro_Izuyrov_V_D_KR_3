import utils
from player import Player

url = "https://api.npoint.io/49db25cfd1feff5b5692"

def main():
    name_player = input("Ввведите имя игрока: ").strip().title()
    player = Player(username=name_player, words_used=None)
    print(f"Привет, {player.username}!\n")

    question_word = utils.load_random_word(url)
    print(f"Составьте {question_word.count_set_subwords()} слов из "
          f"слова {question_word.original_word.upper()}\n")
    print(f"лова должны быть не короче 3 букв\n")
    print(f"Чтобы закончить игру, угадайте все слова или напишите 'stop'\n")
    print(f"Поехали, ваше первое слово?: ")

    while player.number_words_used() < question_word.count_set_subwords():
        user_answer = input('Введите слово: ').strip().lower()
        if user_answer in ["stop", "стоп"]:
            break
        elif len(user_answer) < 3:
            print(f'\nСлишком короткое слово, {question_word.count_set_subwords() - player.number_words_used()} слов')

        elif player.check_words_used(user_answer):
            print(f'\nТакое слово уже отгадано, {question_word.count_set_subwords() - player.number_words_used()} слов')

        elif question_word.response_check(user_answer) == True:
            player.add_words_used(user_answer)
            print(f'\nВерно, отсталось отгадать {question_word.count_set_subwords() - player.number_words_used()} слов')

        elif question_word.response_check(user_answer) != True:
            print(f'\nНе верно, отсталось отгадать {question_word.count_set_subwords() - player.number_words_used()} слов')

    print(f'\nИгра завершина, Вы отгадали {player.number_words_used()} слов')


if __name__ == "__main__":
    main()
