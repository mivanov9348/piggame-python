import random


class PigGame:
    def __init__(self):
        self.scores = [0, 0]
        self.current_score = 0
        self.current_player = 0

    def roll_dice(self):
        roll = random.randint(1, 6)
        print(f'Player {self.current_player + 1} roll {roll}')

        if roll == 1:
            print(f'Player {self.current_player + 1} lose all points!')
            self.current_score = 0
            self.switch_player()
        else:
            self.current_score += roll

    def hold(self):
        print(f'Player {self.current_player + 1} hold {self.current_score} points')
        self.scores[self.current_player] += self.current_score
        self.current_score = 0
        self.switch_player()

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def check_winner(self):
        if self.scores[0] >= 100:
            print("Player 1 wins the game! 🏆")
            return True
        elif self.scores[1] >= 100:
            print("Player 2 wins the game! 🏆")
            return True
        return False
