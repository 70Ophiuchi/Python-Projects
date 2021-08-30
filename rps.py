import random

moves = ['rock', 'paper', 'scissors']


class Player:

    def __init__(self) -> None:
        self.my_move = ""
        self.their_move = ""

    def move(self):
        self.reflect = "rock"
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Player_random(Player):

    def move(self):
        mv = random.choice(moves)
        return mv


class Player_human(Player):

    def move(self):
        while True:
            user_choice = input("* Rock" +
                                "\n* Paper" +
                                "\n* Scissors" +
                                "\nChoice > "
                                )

            user = user_choice.casefold()

            if user == "rock":
                return "rock"
            elif user == "paper":
                return "paper"
            elif user == "scissors":
                return "scissors"
            else:
                print("Please pick a valid option")


class Player_reflect(Player):

    def __init__(self) -> None:
        super().__init__()

    def move(self):
        if len(self.their_move) < 1:
            return random.choice(moves)
        else:
            return self.their_move


class Player_cycle(Player):

    def __init__(self) -> None:
        super().__init__()
        self.cycle = 0
    def move(self):
        while True:
            if self.cycle < 1:
                self.cycle += 1
                return moves[0]
            elif self.cycle < 2:
                self.cycle += 1
                return moves[1]
            elif self.cycle == 2:
                self.cycle += 1
                return moves[2]
            else:
                self.cycle = 0

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_cpu = 0
        self.score_player = 0
        self.status = "null"

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if move1 == move2:
            self.status = "TIED!"
        elif beats(move1, move2) is True:
            self.status = "YOU LOST!"
            self.score_cpu += 1
        else:
            self.status = "YOU WON!"
            self.score_player += 1

        print(f"\n{self.status}" +
              f"\nYOU Picked: {move2}" +
              f"\nCPU Picked: {move1}" +
              f"\nScore:" +
              f"\nCPU: {self.score_cpu}" +
              f"\nYou: {self.score_player}\n")

    def play_game(self):
        while True:
            games = input("How many games" +
                          " would you like to play? 10 MAX" +
                          " Reply with a number only! >  "
                          )
            if games in ["1", "2", "3", "4",
                         "5", "6", "7", "8",
                         "9", "10"
                         ]:
                games1 = int(games)
                break
            else:
                print("Please enter a number" +
                      " between 1 and 10 only!")

        print("Game start!")
        for round in range(games1):
            print(f"Round {round}:")
            self.play_round()
        if self.score_player < self.score_cpu:
            print("YOU LOSE! CPU WINS" +
                  "\nFinal Score: " +
                  f"\nCPU: {self.score_cpu}" +
                  f"\nPlayer: {self.score_player}")
        elif self.score_player == self.score_cpu:
            print("TIED" +
                  "\nFinal Score: " +
                  f"\nCPU: {self.score_cpu}" +
                  f"\nPlayer: {self.score_player}")
        else:
            print("YOU WIN! CPU LOSES" +
                  "\nFinal Score: " +
                  f"\nCPU: {self.score_cpu}" +
                  f"\nPlayer: {self.score_player}")
        print("\nGame over!")


if __name__ == '__main__':
    while True:
        game_mode = input("Which game mode would" +
                          " you like to play?\n" +
                          "Options (reply with number): "
                          "\n1. CPU vs CPU (Basic CPU)" +
                          "\n2. CPU vs CPU (Random CPU)" +
                          "\n3. Human vs CPU (Random CPU)" +
                          "\n4. Human vs CPU (Self-learning CPU)" +
                          "\n5. Human vs CPU (CPU Cycles Options)" +
                          "\n>  "
                          )
        if game_mode == "1":
            p1 = Player()
            p2 = Player()
            break
        elif game_mode == "2":
            p1 = Player()
            p2 = Player_random()
            break
        elif game_mode == "3":
            p1 = Player_random()
            p2 = Player_human()
            break
        elif game_mode == "4":
            p1 = Player_reflect()
            p2 = Player_human()
            break
        elif game_mode == "5":
            p1 = Player_cycle()
            p2 = Player_human()
            break
        else:
            print("Please reply with a" +
                  " number between 1 and 5!")

    game = Game(p1, p2)
    game.play_game()
