class AnswerError(Exception):
    def __str__(self):
        return 'Invalid input!'
