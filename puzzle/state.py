from __future__ import annotations
from typing import List, Optional, Tuple


GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)


class State:
    """Representa um estado do 8-puzzle como tupla imutável de 9 inteiros (0 = espaço vazio)."""

    def __init__(self, tiles: Tuple[int, ...], parent: Optional["State"] = None, action: Optional[str] = None, cost: int = 0):
        if len(tiles) != 9 or set(tiles) != set(range(9)):
            raise ValueError("Estado inválido: deve conter exatamente os valores 0-8.")
        self.tiles = tiles
        self.parent = parent
        self.action = action
        self.cost = cost

    @property
    def is_goal(self) -> bool:
        return self.tiles == GOAL_STATE

    @property
    def blank_index(self) -> int:
        return self.tiles.index(0)

    def move(self, direction: str, target: int) -> "State":
        blank = self.blank_index
        tiles = list(self.tiles)
        tiles[blank], tiles[target] = tiles[target], tiles[blank]
        return State(tuple(tiles), parent=self, action=direction, cost=self.cost + 1)

    def neighbors(self) -> List["State"]:
        """Retorna os estados filhos válidos a partir deste estado."""
        blank = self.blank_index

        children = []
        if self.blank_index == 0: 
                children.append(self.move("RIGHT", 1))
                children.append(self.move("DOWN", 3))
        
        elif self.blank_index == 1:
                children.append(self.move("LEFT", 0))
                children.append(self.move("RIGHT", 2))
                children.append(self.move("DOWN", 4))

        elif self.blank_index == 2:
                children.append(self.move("LEFT", 1))
                children.append(self.move("DOWN", 5))

        elif self.blank_index == 3:
                children.append(self.move("UP", 0))
                children.append(self.move("RIGHT", 4))
                children.append(self.move("DOWN", 6))

        elif self.blank_index == 4:
                children.append(self.move("UP", 1))
                children.append(self.move("LEFT", 3))
                children.append(self.move("RIGHT", 5))
                children.append(self.move("DOWN", 7))

        elif self.blank_index == 5:
                children.append(self.move("UP", 2))
                children.append(self.move("LEFT", 4))
                children.append(self.move("DOWN", 8))

        elif self.blank_index == 6:
                children.append(self.move("UP", 3))
                children.append(self.move("RIGHT", 7))

        elif self.blank_index == 7:
                children.append(self.move("UP", 4))
                children.append(self.move("LEFT", 6))
                children.append(self.move("RIGHT", 8))

        elif self.blank_index == 8:
                children.append(self.move("UP", 5))
                children.append(self.move("LEFT", 7))

        return children

    def path(self) -> List["State"]:
        states = []
        current = self

        while current is not None:
            states.append(current)
            current = current.parent

        states.reverse()
        return states

    def actions(self) -> List[str]:
        """Retorna a sequência de ações do estado inicial até este."""
        
        actions = []

        for state in self.path()[1:]:
                actions.append(state.action)

        return actions

    def __eq__(self, other: object) -> bool:
        return isinstance(other, State) and self.tiles == other.tiles

    def __hash__(self) -> int:
        return hash(self.tiles)

    def __lt__(self, other: "State") -> bool:
        return self.cost < other.cost

    def __repr__(self) -> str:
        t = self.tiles
        return (
            f"\n+-------+\n"
            f"| {t[0]} {t[1]} {t[2]} |\n"
            f"| {t[3]} {t[4]} {t[5]} |\n"
            f"| {t[6]} {t[7]} {t[8]} |\n"
            f"+-------+\n"
        ).replace("0", " ")
