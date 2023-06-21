class Question():

    def __init__(self,question_text, complexity_issue, correct_answer):
        self.question_text = question_text
        self.complexity_issue = complexity_issue
        self.correct_answer = correct_answer

        self.is_aske = False
        self.user_answer = None
        self.score = self.complexity_issue * 10


    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.score


    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return  self.correct_answer == self.user_answer


    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f'\nВопрос: {self.question_text}'\
               f'Сложность: {self.complexity_issue}/5'


    def build_feedback(self):
        """Возвращает :
        Ответ верный и не верный ответ, получено __ баллов
        """
        if self.is_correct():
            return f'Ответ верный, получено {self.score} баллов'
        return f'Ответ неверный, верный ответ - {self.correct_answer}'



