class MoveError(Exception):
    def __str__(self):
        return 'Invalid move!'
