class Positions:

    def __init__(self):
        self.dict = {
            '1': '1',
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            '8': '8',
            '9': '9'
        }
        self.count = 0

    def game_board(self):
        print((f'    |   {self.dict["1"]}    |   {self.dict["2"]}    |   {self.dict["3"]}    |\n'
               '-----------------------------------\n'
               f'    |   {self.dict["4"]}    |   {self.dict["5"]}    |   {self.dict["6"]}    |\n'
               '-----------------------------------\n'
               f'    |   {self.dict["7"]}    |   {self.dict["8"]}    |   {self.dict["9"]}    |\n'))

    def player_move(self, x_or_o):

        user_move = input(f"Player {x_or_o} move: ")
        item = self.dict.get(user_move, "Not playable")
        if item == 'X' or item == 'O' or item == 'Not playable':
            print('not playable')
            self.game_board()
            self.player_move(x_or_o)
        else:
            self.dict[user_move] = x_or_o
            self.count += 1
            self.game_board()

    def winner(self):
        p1 = self.dict.get('1')
        p2 = self.dict.get('2')
        p3 = self.dict.get('3')
        p4 = self.dict.get('4')
        p5 = self.dict.get('5')
        p6 = self.dict.get('6')
        p7 = self.dict.get('7')
        p8 = self.dict.get('8')
        p9 = self.dict.get('9')

        if p1 == p5 == p9:
            print(f'{p1} wins')
            return True
        elif p3 == p5 == p7:
            print(f'{p3} wins')
            return True
        elif p2 == p5 == p8:
            print(f'{p2} wins')
            return True
        elif p1 == p4 == p7:
            print(f'{p1} wins')
            return True
        elif p3 == p6 == p9:
            print(f'{p3} wins')
            return True
        elif p1 == p2 == p3:
            print(f'{p1} wins')
            return True
        elif p4 == p5 == p6:
            print(f'{p4} wins')
            return True
        elif p7 == p8 == p9:
            print(f'{p7} wins')
            return True
        else:
            return False
