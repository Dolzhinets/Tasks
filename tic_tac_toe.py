from abc import ABC, abstractmethod
from subprocess import call

class GameInterface(ABC):
    @abstractmethod
    def reset_game(self):
        pass

    @abstractmethod
    def table(self):
        pass

    @abstractmethod
    def get_row(self, index):
        pass

    @abstractmethod
    def get_column(self, index):
        pass

    @abstractmethod
    def get_rtl_diagonal(self):
        pass

    @abstractmethod
    def get_ltr_diagonal(self):
        pass

    @abstractmethod
    def set_point(self, point, value):
        pass

class PlayerInterface(ABC):
    @abstractmethod
    def game(self):
        pass

    @abstractmethod
    def mark(self, point):
        pass
        
class Game(GameInterface):
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self._table = [['-' for _ in range(3)] for _ in range(3)]

    def table(self):
        return self._table
    table = property(table)

    def get_row(self, index):
        if index >= 0 and index <= 2:
            return self.table[index]
        raise ValueError

    def get_column(self, index):
        if index >= 0 and index <= 2:
            return [row[index] for row in self.table]
        raise ValueError

    def get_rtl_diagonal(self):
        return [self.table[row][index] for row, index in zip(range(3),
                reversed(range(3)))]

    def get_ltr_diagonal(self):
        return [self.table[index][index] for index in range(3)]

    def set_point(self, point: tuple([int, int]), value):
        if self.table[point[0]][point[1]] != '-':
            raise IndexError
        self._table[point[0]][point[1]] = value

    def is_full(self):
        for row in self.table:
            for point in row:
                if point == '-':
                    return False
        return True

def check_for_winner(game: Game):
    if res := check_for_row_winner(game):
        return res
    if res := check_for_column_winner(game):
        return res
    if res := check_for_rtl_diagonal_winner(game):
        return res
    if res := check_for_ltr_diagonal_winner(game):
        return res
    return ''

def check_for_row_winner(game: Game):
    for row in range(3):
        processed_row = ['' if item == '-' else item
                         for item in game.get_row(row)]
        if all(processed_row) and len(set(processed_row)) == 1:
            return game.get_row(row)[0]
    return ''

def check_for_column_winner(game: Game):
    for column in range(3):
        processed_column = ['' if item == '-' else item
                            for item in game.get_column(column)]
        if all(processed_column) and len(set(processed_column)) == 1:
            return game.get_column(column)[0]
    return ''

def check_for_rtl_diagonal_winner(game: Game):
    processed_rtl_diagonal = ['' if item == '-' else item
                              for item in game.get_rtl_diagonal()]
    if all(processed_rtl_diagonal) and len(set(processed_rtl_diagonal)) == 1:
        return game.get_rtl_diagonal()[0]
    return ''

def check_for_ltr_diagonal_winner(game: Game):
    processed_ltr_diagonal = ['' if item == '-' else item
                              for item in game.get_ltr_diagonal()]
    if all(processed_ltr_diagonal) and len(set(processed_ltr_diagonal)) == 1:
        return game.get_ltr_diagonal()[0]
    return ''

class Player(PlayerInterface):
    def __init__(self, game: GameInterface, char: str):
        self._game = game
        self.char = char

    def game(self):
        return self._game
    game = property(game)

    def mark(self, point):
        self.game.set_point(point, self.char)        
        
def main():
    game = Game()
    first_player = Player(game, 'X')
    second_player = Player(game, 'O')
    while True:
        display_table(game.table)
        first_player.mark(get_point_by_numkey(int(input('X mark: '))))
        exit_if_game_is_finished(game)
        display_table(game.table)
        second_player.mark(get_point_by_numkey(int(input('O mark: '))))
        exit_if_game_is_finished(game)

def display_table(table):
    call('cls', shell=True)
    print(get_raw_table(table))

def get_raw_table(table):
    raw_str = str()
    for row in table:
        for i in row:
            raw_str += i
            raw_str += ' ' * 2
        raw_str += '\n'
    return raw_str

def get_point_by_numkey(numkey: int) -> tuple([int, int]):
    NUMKEYS_TO_POINTS = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                         4: (1, 0), 5: (1, 1), 6: (1, 2),
                         7: (2, 0), 8: (2, 1), 9: (2, 2)}
    return NUMKEYS_TO_POINTS[numkey]

def exit_if_game_is_finished(game: Game):
    if check_game_status(game):
        exit()
    if check_if_game_is_full(game):
        exit()

def check_game_status(game: Game):
    winner = check_for_winner(game)
    if winner:
        call('cls', shell=True)
        print(get_raw_table(game.table))
        print(f'Player {winner} won!')
        return True
    return False

def check_if_game_is_full(game: Game):
    if game.is_full():
        call('cls', shell=True)
        print(get_raw_table(game.table))
        print('no winner!')
        return True
    return False

if __name__ == '__main__':
    main()