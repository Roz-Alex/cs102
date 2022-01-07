import pathlib
import random
import typing as tp
from pprint import pprint as pp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        """
            Создание списка клеток.

            Клетка считается живой, если ее значение равно 1, в противном случае клетка
            считается мертвой, то есть, ее значение равно 0.

            Parameters
            ----------
            randomize : bool
                Если значение истина, то создается матрица, где каждая клетка может
                быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

            Returns
            ----------
            out : Grid
                Матрица клеток размером `cell_height` х `cell_width`.
        """
        grid = []
        for i in range(self.rows):
            grid.append([])
            for j in range(self.cols):
                if randomize:
                    grid[i].append(random.randint(0, 1))
                else:
                    grid[i].append(0)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        # Copy from previous assignment
        pass

    def get_next_generation(self) -> Grid:
        # Copy from previous assignment
        pass

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        pass

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        pass

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        pass

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        pass

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        pass

game = GameOfLife((4, 4))
grid = game.create_grid(randomize=False)
for i in range(4):
    print(grid[i])