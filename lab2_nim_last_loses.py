#! /usr/bin/python3

# whoever takes the last stick loses

from nim_game import IPlayer, Human, GameController, GameState


class Computer(IPlayer):
    def move(self, state: GameState) -> int:
        num_sticks = (state.sticks - 1) % (state.max_pick_num + 1)
        if num_sticks == 0:
            num_sticks = 1
        print(f"{self.name} picked: {num_sticks}")
        return num_sticks


def on_game_end(curr_player: IPlayer):
    print(f"{curr_player.name} Loses!!!")


def main():
    total_sticks = 15
    max_num_sticks = 3
    players = [Human("Player 1"), Computer("Computer")]

    game = GameController(total_sticks, max_num_sticks, players, on_game_end)
    game.run()


if __name__ == "__main__":
    main()
