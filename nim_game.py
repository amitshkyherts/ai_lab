from typing import Callable
from random import randint


class GameState:
    def __init__(self, sticks, max_pick_num):
        self.sticks = sticks
        self.max_pick_num = max_pick_num


class IPlayer:
    def __init__(self, name):
        self.name = name

    def move(self, state: GameState) -> int:
        pass


class Human(IPlayer):
    def move(self, _: GameState) -> int:
        return int(input(f"{self.name}: "))


class RandomMove(IPlayer):
    def move(self, state: GameState) -> int:
        num_sticks = randint(1, state.max_pick_num
                             if state.sticks > state.max_pick_num
                             else state.sticks)
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

        self.state = GameState(num_sticks, max_pick_num)
        self.players: list[IPlayer] = players
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
        while True:
            num_sticks = player.move(self.state)
            if num_sticks < 1 \
                    or num_sticks > self.state.max_pick_num \
                    or num_sticks > self.state.sticks:
                print("Invalid number of sticks picked. Try again!")
                continue
            break

        self.state.sticks -= num_sticks
