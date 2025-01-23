from gameparts import Board
from gameparts import FieldIndexError
from gameparts import CellOccupiedError


def save_result(result):
    # Открыть файл results.txt в режиме "добавление".
    # Если нужно явно указать кодировку, добавьте параметр encoding='utf-8'.
    with open('results.txt', 'a', encoding='utf-8') as f:
        # Записать в файл содержимое переменной result.
        f.write(result + '\n')


def main():
    game = Board()  # Создать игровое поле - объект класса Board.
    current_player = 'X'
    # Это флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True
    game.display()  # Отрисовать поле в терминале.
    while running:

        print(f'Ход делают {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or row >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError(
                        'Ячейка занята. Введите другие координаты.')
            except FieldIndexError:
                # ...выводятся сообщения...
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                # ...и цикл начинает свою работу сначала,
                # предоставляя пользователю ещё одну попытку ввести данные.
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            # Если в блоке try исключения не возникло...
            else:
                # ...значит, введённые значения прошли все проверки
                # и могут быть использованы в дальнейшем.
                # Цикл прерывается.
                break
        game.make_move(row, column, current_player)  # сделать ход.
        print('Ход сделан!')  # Перерисовать поле с учётом сделанного хода.
        current_player = 'O' if current_player == 'X' else 'X'
        game.display()
        if game.check_win(current_player):
            result = f'Победили {current_player}.'
            print(result)
            save_result(result)
            running = False
        elif game.is_board_full():
            result = 'Ничья!'
            print(result)
            running = False


if __name__ == '__main__':
    main()
