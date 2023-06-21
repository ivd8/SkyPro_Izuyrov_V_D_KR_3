class BasicWord:
    """
    Класс для работы с словами из
    которого составляются слова
    """

    def __init__(self, original_word="", set_subwords=None):
        """ Метод инициирует Поля (исходное слово и набор допустимых подслов)
        Вход: str, list
        Выход: self.str ,self.list
        """
        self.original_word = original_word
        self.set_subwords = set_subwords if set_subwords else []

    def __repr__(self):
        return f"BasicWord (original_word= '{self.original_word}', set_subwords= {self.set_subwords}"

    def response_check(self, original_word):
        """ Метод осуществляет проверку введенного слова в списке допустимых подслов
        Вход: Ответ пользователя, str
        Выход: Проверка такого слова ,bool
        """
        return original_word.lower() in self.set_subwords

    def count_set_subwords(self):
        """ подсчет количества подслов
        Вход: list
        Выход: int
        """
        return len(self.set_subwords)