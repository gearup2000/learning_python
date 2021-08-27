from enum import Enum
import pygame

CELL_SIZE = 50  # The size of cells
FPS = 60


class Cell(Enum):
    VOID = 0
    CROSS = 1
    ZERO = 2


class Player:
    """
    The class of Player. includes type of symbols (cross or zero) and the player name.
    """

    def __init__(self, name, cell_type):  # Player have to have player name and the cell type CROSS or ZERO.
        self.name = name
        self.cell_type = cell_type


class GameField:
    def __init__(self):
        self.height = 3
        self.width = 3
        self.cell = [[Cell.VOID] * self.width for i in range(self.height)]  # The number of cells for game board will
        # get the initial value of VOID and multiply it 3 times to make 3 columns and then in range of cell.width
        # multiply it to make 3 rows.


class GameFieldView:
    """
    Widget of game filed AKA game board, which do all calculations of figures on the board,
     and shows the coordinates of mouse clicks.
    """

    def __init__(self, field_to_observe):
        # upload pictures for symbols of cells
        # show start condition of the field AKA game board
        self._field = field_to_observe
        self._height = field_to_observe.height * CELL_SIZE
        self._width = field_to_observe.width * CELL_SIZE

    def draw(self):  # tells to GameFieldView to draw himself.
        pass

    def check_coords_correct(self, x, y):
        return True  # TODO: self._height take to account!!!

    def get_coords(self, x, y):
        return 0, 0  # TODO: calculate the cell of mouse click.


class GameRoundManager:
    """
    The game manager which handles all processes
    """

    # The list of players
    def __init__(self, player1: Player, player2: Player):
        self._player = [player1, player2]
        self._current_player = 0
        self.field = GameField()  # creates an empty standard board

    def handle_click(self, i, j):
        # i and j are referring to the coordinates of x and y of the board correspondingly.
        player = self._player[self._current_player]
        # the player made a turn on the field AKA game board
        print("click_handled", i, j)  # Print click handled and values of i and j to check that handle_click got
        # coordinates from main loop
        # handle_click section


class GameWindow:
    """
    includes widget of the board, and also manager of the game round
    """

    # widget of the board
    def __init__(self):  # Creates the round, board and manager of the game
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
        self._field_widget = GameFieldView(self._game_manager.field)  # gets the values of field from GameRoundManager

    # the main loop of the game aka manager
    def main_loop(self):
        finished = False
        clock = pygame.time.Clock()
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = mouse_pos  # get x and y coordinates from mouse_pos and send them to
                    # self._game_manager.handle_click
                    if self._field_widget.check_coords_correct(x, y):
                        # field_widget will check are these x and y coordinates are inside of the board area and if
                        # they are, calculate their positions and prepare to use them in handle.click as i and j.
                        i, j = self._field_widget.get_coords(x, y)
                        # i and j are referring to the coordinates of x and y of the board correspondingly.
                        self._game_manager.handle_click(i, j)

            # Update screen (Actually draw the picture in the windows.)
            pygame.display.flip()

            # Limit refresh rate of game loop
            clock.tick(FPS)


def main(): # the game begins from this function
    window = GameWindow()  # create the main window by calling GameWindow function
    window.main_loop()  # and dive to its main loop
    print('Game Over!')  # After game has completed print Game Over


if __name__ == "__main__": # protect the __main__ module from executing as a module, in that case start main
    main()
