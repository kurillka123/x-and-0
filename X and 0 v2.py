'''
1 игрок - X
2 игрок - О
игровое поле из 9 клетокЖ 3 на 3
игроки ходят по очереди
сделать ход - поставить X или O в свободную клетку поля
условие победы: 3 одинаковых символов по горизонтали/вертикали/наискосок
если победитель не выявлен, а свободные клетки кончились - ничья
'''
# глобальные константы
EMPTY = '.'
PLAYER_1 = 'X'
PLAYER_2 = 'O'


def get_field() -> list[str]:
    ''' Возвращает поле из 9 пустых клеток '''
    field = []
    for _ in range(9):
        field.append(EMPTY)
    return field


field = get_field()


def draw_fielnd(field: list) -> None:
    ''' Выводит на поле 3 клетки в ряд '''
    for i in range(0, 9, 3):
        print(field[i], field[i + 1], field[i + 2]) 


def make_move(field: list, player: str) -> None:
    '''
    Спрашивает у играка номер клетки поля
    Проверяет, что клетка с таким номером в пределах поля
    Проверяет, занята ли клетка
    При удачных проверок:
    Изменяет клетку под выбранным номером на player - символ игрока
    '''
    while True:
        cell_num = int(input(f'Ведите номер клетки для хода {player}: '))
        if cell_num < 1 or cell_num > 9:
            print('Ошибка! Номер клетки должен быть от 1 до 9 вкл!')
        elif field[cell_num - 1] != EMPTY:
            print('Ошибка! Это клетка занята!')
        else:
            field[cell_num - 1] = player
            break


def main():
    field = get_field()
    moves = 1
    while moves <= 9:
        draw_fielnd(field)
        if moves % 2:
            make_move(field, PLAYER_1)
        else:
            make_move(field, PLAYER_2)
        moves += 1
    else: # сработает без break
        draw_fielnd(field)
        print('ничья')


main()