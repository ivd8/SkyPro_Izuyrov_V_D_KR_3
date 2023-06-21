class Player:
    """
    Класс для работы c Юзером, записывает Имя и введеные правильные ответы
    """

    def __init__(self, username="", words_used=None):
        """ Метод инициирует Поля (имя пользователя и использованные слова пользователя)
        Вход: str
        Выход: str
        """
        self.username = username
        self.words_used = words_used if words_used else []

    def __repr__(self):
        return f"Player(username='{self.username}', words_used={self.words_used})"

    def number_words_used(self):
        """ Метод получает количества использованных слов
        Вход: list
        Выход: int
        """
        return len(self.words_used)

    def add_words_used(self, words_used):
        """ Метод добавление слова в использованные слова
        Вход: str
        Выход: str
        """

        if words_used is not self.words_used:
            self.words_used.append(words_used)

    def check_words_used(self, words_used):
        """ Метод проверка использования слова до этого
        Вход: str
        Выход: bool
        """
        return words_used in self.words_used