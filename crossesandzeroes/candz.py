from enum import Enum
import pygame


CELL_SIZE = 50
FPS = 60


class Cell(Enum):
    VOID = 0
    CROSS = 1
    ZERO = 2


class Player:
    """
    The class of Player includes type of symbols (cross or zero) and the player name
    """
    def __init__(self, name, cell_type):
        self.name = name
        self.cell_type = cell_type


class GameField:
    def __init__(self):
        self.height = 3
        self.width = 3
        self.cell = [[Cell.VOID]*self.width for i in range(self.height)]


class GameFieldView:
    """
    Widget of game filed AKA game board, which do all geometry and shows the place of mouse clicks.
    """
    def __init__(self, field_to_observe):
        # upload pictures for symbols of cells
        # show start condition of the field AKA game board
        self._field = field_to_observe
        self._height = field_to_observe.height * CELL_SIZE
        self._width = field_to_observe.width * CELL_SIZE

    def draw(self):
        pass

    def check_coords_correct(self, x, y):
        return True  # TODO: self._height take to account!!!

    def get_coords(self, x, y):
        return 0, 0  # TODO: self._width take to account!!!


class GameRoundManager:
    """
    The game manager which handles all processes
    """

    def __init__(self, player1: Player, player2: Player):
        self._player = [player1, player2]
        self._current_player = 0
        self.field = GameField()

    def handle_click(self, i, j):
        player = self._player[self._current_player]
        # the player made a turn on the field AKA game board
        print("click_handled", i, j)


class GameWindow:
    """
    includes widget of the field, and also manager of the game round
    """
    def __init__(self):
        # initialization pygame
        pygame.init()

        # Window
        self._width = 800
        self._height = 600
        self._title = "Crosses & Zeroes"
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._title)
        player1 = Player("Noname1", Cell.CROSS)
        player2 = Player("Noname2", Cell.ZERO)
        self._game_manager = GameRoundManager(player1, player2)
        self._field_widget = GameFieldView(self._game_manager.field)

    def main_loop(self):
        finished = False
        clock = pygame.time.Clock()
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = mouse_pos
                    if self._field_widget.check_coords_correct(x, y):
                        i, j = self._field_widget.get_coords(x, y)
                        self._game_manager.handle_click(i, j)

            # Update screen (Actually draw the picture in the windows.)
            pygame.display.flip()

            # Limit refresh rate of game loop
            clock.tick(FPS)


def main():
    window = GameWindow()
    window.main_loop()
    print('Game Over!')


if __name__ == "__main__":
    main()
