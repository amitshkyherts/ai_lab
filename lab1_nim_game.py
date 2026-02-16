#! /usr/bin/python3

from nim_game import IPlayer, Human, GameController, GameState


class Computer(IPlayer):
    def move(self, state: GameState) -> int:
        num_sticks = state.sticks % (state.max_pick_num + 1)
        if num_sticks == 0:
            num_sticks = state.max_pick_num
        print(f"{self.name} picked: {num_sticks}")
        return num_sticks


def on_game_end(curr_player: IPlayer):
    print(f"{curr_player.name} Wins!!!")


def main():
    total_sticks = 17
    max_num_sticks = 3
    players = [Human("Player 1"), Computer("Computer")]

    game = GameController(total_sticks, max_num_sticks, players, on_game_end)
    game.run()


if __name__ == "__main__":
    main()
