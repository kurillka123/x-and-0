'''
1 игрок - X
2 игрок - О
игровое поле из 9 клетокЖ 3 на 3
игроки ходят по очереди
сделать ход - поставить X или O в свободную клетку поля
условие победы: 3 одинаковых символов по горизонтали/вертикали/наискосок
если победитель не выявлен, а свободные клетки кончились - ничья
'''

from os import system

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
    system('cls')
    for i in range(0, 9, 3):
        print(field[i], field[i + 1], field[i + 2]) 

def make_move(field: list, player: str, is_auto: bool) -> None:
    '''
    Спрашивает у играка номер клетки поля
    Проверяет, что клетка с таким номером в пределах поля
    Проверяет, занята ли клетка
    При удачных проверок:
    Изменяет клетку под выбранным номером на player - символ игрока
    '''
    if not is_auto:
        while True:
            try:
                cell_num = int(input(f'Ведите номер клетки для хода {player}: '))  #FIXME принимать только целые числа
            except ValueError:
                print('Ошибка! номер должен быть цифрой')
                continue
            if cell_num < 1 or cell_num > 9:
                print('Ошибка! Номер клетки должен быть от 1 до 9 вкл!')
            elif field[cell_num - 1] != EMPTY:
                print('Ошибка! Это клетка занята!')
            else:
                field[cell_num - 1] = player
                break
    else:
        '''
        coброть пустые клетки в список
        выбрать клетку из этого списка
        поставить туда себя
        '''
        empty_cells = []
        for cell in field:
            if cell == EMPTY:
                empty_cells.append(cell)
        

def get_winner(field: list, player: str) -> str:
    for i in range(0, 7, 3):
        if field[i] == field[i + 1] == field[i + 2] == player:
            return player
        for i in range(3):
            if field[i] == field[i + 3] == field[i + 6] == player:
                return player
        for i in range(3):
            if field[0] == field[4] == field[8] == player:
                return player
            if field[2] == field[4] == field[6] == player:
                return player
    return ''


def main() -> None:
    '''
    создает поле
    включает все функции
    '''
    field = get_field()
    moves = 1
    while moves <= 9:
        draw_fielnd(field)
        if moves % 2:
            player = PLAYER_1
            is_auto = False
        else:
            player = PLAYER_2
            is_auto = True
        make_move(field, player, is_auto)
        moves += 1
        winner = get_winner(field, player)

        if winner: 
            draw_fielnd(field)
            print('победил', player)
            break
    else:
        draw_fielnd(field)   
        print('Ничья!')



main()