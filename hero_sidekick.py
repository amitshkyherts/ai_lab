#! /usr/bin/python3

from typing import Generator
from pprint import pp
from problem import IProblem, dfs


type Person = tuple[str, int]
type PersonSideDict = dict[Person, str]
type PersonSideTup = tuple[Person, str]
type HeroSidekickState = tuple[PersonSideDict, str]


class HeroSidekick(IProblem):
    def start(self) -> HeroSidekickState:
        return ({
            ("hero", 1): "left",
            ("kick", 1): "left",
            ("hero", 2): "left",
            ("kick", 2): "left",
            ("hero", 3): "left",
            ("kick", 3): "left",
        }, "left")

    def is_goal(self, state: HeroSidekickState) -> bool:
        person_side: PersonSideDict
        person_side, _ = state
        for person in person_side:
            if person_side[person] != "right":
                return False
        return True

    def successor_states(self, state: HeroSidekickState) -> HeroSidekickState:
        """
        Generate all possible next states (safe states)
        """
        person_side: PersonSideDict
        boat: str
        (person_side, boat) = state
        # people on the same side as the boat
        person_with_boat: list[Person] = [person
                                          for person in person_side
                                          if person_side[person] == boat]

        travellers: list[Person]
        for travellers in self.select_travellers(person_with_boat):
            new_side: dict[PersonSideDict] = person_side.copy()

            traveller: Person
            for traveller in travellers:
                # the traveller moves to the other side
                new_side[traveller] = self.other_side[person_side[traveller]]

            new_state: HeroSidekickState = (new_side, self.other_side[boat])
            if self.is_safe(new_state):
                yield new_state

    def token(self,
              state: HeroSidekickState) -> tuple[PersonSideTup, str]:
        person_side, boat = state
        pairs: tuple[Person, str] = sorted(person_side.items())
        return (tuple(pairs), boat)

    def select_travellers(self,
                          candidates: list[PersonSideDict]) -> Generator[
            list[Person], None, None]:
        """
        Generate all the possible permutations of travellers
        travelling one at a time and two at a time
        """
        for first in range(len(candidates)):
            yield [candidates[first]]

        for first in range(len(candidates)):
            for second in range(first + 1, len(candidates)):
                yield [candidates[first], candidates[second]]

    def is_safe(self, state: HeroSidekickState) -> bool:
        """
        Check if the sidekicks are alone with other heros
        """
        person_side, _ = state
        for side in ["left", "right"]:
            # all the sidekicks whose heros are not on the same side
            lone_kick: list[int] = [index for (person, index) in person_side
                                    if person == "kick"
                                    if person_side[(person, index)] == side
                                    if person_side[("hero", index)] != side]
            # get all the heros present on the current side
            hero_present: list[int] = [index for (person, index) in person_side
                                       if person == "hero"
                                       if person_side[(person, index)] == side]

            # if there are sidekicks alone with other heros
            if lone_kick and hero_present:
                return False

        return True

    other_side = {
        "left": "right",
        "right": "left",
    }


def main():
    h = HeroSidekick()
    pp(dfs(h, h.start()))


if __name__ == "__main__":
    main()
