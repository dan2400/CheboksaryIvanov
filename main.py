import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.colors = ((0, 0, 0), (255, 255, 255))
        self.screen2 = pygame.Surface((self.width * self.cell_size, self.height * self.cell_size))

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        self.screen2 = pygame.Surface((self.width * self.cell_size, self.height * self.cell_size))
        for i in range(self.width):
            for j in range(self.height):
                color1 = self.colors[self.board[j][i]]
                pygame.draw.rect(self.screen2, color1, ((i * self.cell_size + 1, j * self.cell_size + 1),
                                                        (self.cell_size - 2, self.cell_size - 2)))
                pygame.draw.rect(self.screen2, (255, 255, 255), ((i * self.cell_size, j * self.cell_size),
                                                        (self.cell_size, self.cell_size)), 1)
        screen.blit(self.screen2, (self.left, self.top))


    def get_cell(self, mouse_pos):
        return ((mouse_pos[0] - self.left) // self.cell_size,
                (mouse_pos[1] - self.top) // self.cell_size)


    def on_click(self, cell_coords):
        for i in range(self.width):
            self.board[cell_coords[1]][i] = (self.board[cell_coords[1]][i] + 1) % 2
        for i in range(self.height):
            self.board[i][cell_coords[0]] = (self.board[i][cell_coords[0]] + 1) % 2
        self.board[cell_coords[1]][cell_coords[0]] = (self.board[cell_coords[1]][cell_coords[0]] + 1) % 2

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)
    board = Board(5, 7)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
