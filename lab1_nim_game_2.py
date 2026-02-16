class IPlayer:
    def __init__(self, name):
        self.name = name

    def move(self, state: int) -> int:
        pass


class Computer(IPlayer):
    def move(self, state: int) -> int:
        num_sticks = state % 4
        if num_sticks == 0:
            num_sticks = 3
        print(f"\n{self.name} picked: {num_sticks}")
        return num_sticks


class Human(IPlayer):
    def move(self, state: int) -> int:
        while True:
            print(f"\n{self.name}:")
            num_sticks = int(input("Pick either 1, 2, or 3 sticks: "))
            if num_sticks < 0 or num_sticks > 3 or num_sticks > state:
                print("Invalid number of sticks picked. Try again!")
                continue
            return num_sticks


class GameController:
    def __init__(self, num_sticks: int, players: list[IPlayer]):
        self.state: int = num_sticks
        self.players: list[IPlayer] = players
        self.is_running: bool = True

    def run(self):
        while self.is_running:
            for player in self.players:
                print(f"\nRemaining sticks: {self.state}")
                self.move_manager(player)
                if self.state <= 0:
                    print(f"{player.name} is the winner!!!!!")
                    self.is_running = False
                    break

    def move_manager(self, player):
        num_sticks = player.move(self.state)
        self.state -= num_sticks


def main():
    total_sticks = 16
    players = [Human("Player 1"), Computer("Computer")]
    game = GameController(total_sticks, players)
    game.run()


if __name__ == "__main__":
    main()
