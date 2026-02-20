from typing import Callable
from random import randint


class GameState:
    def __init__(self, total_num_sticks: int):
        self.sticks: int = total_num_sticks


class IPlayer:
    def __init__(self, name):
        self.name = name

    def move(self, state: GameState, max_pick_num) -> int:
        pass


class Human(IPlayer):
    def move(self, state: GameState, max_pick_num) -> int:
        while True:
            move = int(input(f"{self.name} (from 1 to {max_pick_num}): "))
            if move > 0 and move <= max_pick_num and move <= state.sticks:
                return move


class RandomMove(IPlayer):
    def move(self, state: GameState, max_pick_num) -> int:
        num_sticks = randint(1, min(max_pick_num, state.sticks))
        print(f"{self.name} picked: {num_sticks}")
        return num_sticks


class GameController:
    def __init__(self, num_sticks: int, max_pick_num: int,
                 players: list[IPlayer],
                 fn_on_game_end: Callable[[IPlayer], None]):
        if num_sticks <= 0:
            raise ValueError(
                "Total number of sticks should be greater than 0!")

        if max_pick_num < 2:
            raise ValueError(
                "Max number of sticks that can be taken should be at least 2!")

        if len(players) < 2:
            raise ValueError("There should be at least 2 players!")

        self.players: list[IPlayer] = players
        self.state = GameState(num_sticks)
        self.max_pick_num = max_pick_num
        self.on_game_end = fn_on_game_end
        self.is_running: bool = True

    def run(self):
        while self.is_running:
            for player in self.players:
                print(f"Remaining sticks: {self.state.sticks}")
                self.move_manager(player)

                if self.state.sticks <= 0:
                    self.on_game_end(player)
                    self.is_running = False
                    break

    def move_manager(self, player):
        num_sticks = player.move(self.state, self.max_pick_num)
        self.state.sticks -= num_sticks
