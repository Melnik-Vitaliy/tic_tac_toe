# Может быть пустым или содержать, например,
#  общие для всех модулей пакета импорты, переменные и константы.
from .parts import Board  # Точка в записи означает текущий каталог.
from .exception import FieldIndexError
from .exception import CellOccupiedError