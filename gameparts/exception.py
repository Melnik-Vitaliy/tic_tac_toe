class FieldIndexError(IndexError):
    """Выбрасывается, если выбрано значение вне поля."""

    def __init__(self, massage='Введено значение за границами игрового поля!'):
        super().__init__(massage)


class CellOccupiedError(Exception):
    """Выбрасывается, если хотели изменить занятую ячейку."""

    def __init__(self, message='Попытка изменить занятую ячейку'):
        super().__init__(message)
