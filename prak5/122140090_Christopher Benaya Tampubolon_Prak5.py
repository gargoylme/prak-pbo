import pygame
import sys
import random

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Ular Tangga")
        self.clock = pygame.time.Clock()
        self.is_running = True

    def run(self):
        while self.is_running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

    def update(self):
        pass

    def draw(self):
        pass

class UlarTangga(Game):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.board_size = 10
        self.tile_size = 50
        self.board = self.generate_board()
        self.player_position = 0
        self.player_color = (255, 0, 0)
        self.dice_value = 1
        self.dice_font = pygame.font.SysFont(None, 36)
        self.dice_button_rect = pygame.Rect(self.width // 2 - 50, self.height - 100, 100, 50)

    def generate_board(self):
        board = []
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                row.append(i * self.board_size + j + 1)
            if i % 2 == 1:
                row.reverse()
            board.append(row)
        return board

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.dice_value = random.randint(1, 6)
            self.player_position += self.dice_value
            if self.player_position >= self.board_size ** 2:
                self.player_position = self.board_size ** 2
            elif self.player_position in {14, 23, 43, 49, 62, 69, 75, 84, 88}:
                self.player_position += 10
            elif self.player_position in {18, 25, 34, 41, 53, 57, 64, 68, 82}:
                self.player_position -= 10

    def draw(self):
        self.screen.fill((255, 255, 255))
        for i in range(self.board_size):
            for j in range(self.board_size):
                pygame.draw.rect(self.screen, (0, 0, 0), (j * self.tile_size, i * self.tile_size, self.tile_size, self.tile_size), 2)
                font = pygame.font.SysFont(None, 24)
                text = font.render(str(self.board[i][j]), True, (0, 0, 0))
                text_rect = text.get_rect(center=(j * self.tile_size + self.tile_size // 2, i * self.tile_size + self.tile_size // 2))
                self.screen.blit(text, text_rect)
        pygame.draw.circle(self.screen, self.player_color, self.get_player_position(), self.tile_size // 3)
        pygame.draw.rect(self.screen, (0, 0, 0), self.dice_button_rect, 2)
        dice_text = self.dice_font.render("Dadu: " + str(self.dice_value), True, (0, 0, 0))
        dice_text_rect = dice_text.get_rect(center=self.dice_button_rect.center)
        self.screen.blit(dice_text, dice_text_rect)
        pygame.display.flip()

    def get_player_position(self):
        row = self.player_position // self.board_size
        col = self.player_position % self.board_size
        if row % 2 == 1:
            col = self.board_size - 1 - col
        x = col * self.tile_size + self.tile_size // 2
        y = row * self.tile_size + self.tile_size // 2
        return x, y

if __name__ == "__main__":
    game = UlarTangga(500, 500)
    game.run()
