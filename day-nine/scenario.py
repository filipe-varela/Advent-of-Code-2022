import numpy as np

class Canvas(object):
    def __init__(self) -> None:
        self.dot = '.'
        self.print_board = self.__generate_board__(3)
        self.position_board = []
        self.draw()
        
    def __generate_board__(self, size: int) -> np.array:
        return np.array(
            [
                [self.dot for _ in range(size + int(size % 2 == 0))] for _ in range(size + int(size % 2 == 0))
            ]
        )

    def clear(self) -> None:
        self.position_board.clear()
        self.print_board = self.__generate_board__(self.print_board.shape[0])

    def draw(self) -> None:
        for row in self.print_board: print(" ".join(row))
        self.clear()

    def draw_point(self, descriptor: str, point: list[int]) -> None:
        wasChanged = False
        if (x_dim := abs(point[0])) > self.print_board.shape[1]//2: 
            self.print_board = self.__generate_board__(2*x_dim+2)
            wasChanged = True

        if (y_dim := abs(point[1])) > self.print_board.shape[0]//2: 
            self.print_board = self.__generate_board__(2*y_dim+2)
            wasChanged = True

        origin = [i//2 for i in self.print_board.shape]

        if wasChanged:
            for p in self.position_board: 
                self.print_board[origin[1] - p[1][1], origin[0] + p[1][0]] = p[0]

        self.print_board[origin[1] - point[1], origin[0] + point[0]] = descriptor
        self.position_board.append([descriptor, point])