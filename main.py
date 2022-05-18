import pygame, os
from player import *

pygame.font.init()


#class ini merupakan kelas dari seluruh tampilan dan inisialisasi game
class Game():
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 500  #lebar jendela window
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("1v1 Bang-Bang")  #judul window
        self.run, self.running = True, True  #varibel untuk mengecek kejadian
        self.FPS = 60
        self.vel = 5
        self.b_vel = 7
        self.WINNER_FONT = pygame.font.SysFont('comicsans', 100)
        self.bg = pygame.transform.scale(
            pygame.image.load(os.path.join('Assets', 'background_1.png')),
            (self.width, self.height))
        self.batas = pygame.Rect(self.width // 2 - 5, 0, 10, self.height)

        self.player1_hit = pygame.USEREVENT + 1
        self.player2_hit = pygame.USEREVENT + 2
        self.peluru = 3
        self.Player_1 = None
        self.Player_2 = None

        self.jump_1 = False
        self.jump_2 = False

        #atribut background
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)

    #fungsi ini untuk melakukan perulangan terhadap game
    def loop(self):
        self.load_player()
        clock = pygame.time.Clock()
        while self.run:
            clock.tick(self.FPS)
            self.get_event()
            winner_text = ""
            if self.Player_1.health <= 0:
                self.Player_1.dead()
                self.draw_window()
                winner_text = "Player 2 Wins!"

            if self.Player_2.health <= 0:
                winner_text = "Player 1 Wins!"

            if winner_text != "":
                self.draw_winner(winner_text)
                break

            self.Player_1.basic_action(self.window)
            keys_pressed = pygame.key.get_pressed()
            self.movement_handle(keys_pressed)
            self.attck_handle()
            self.draw_window()

        pygame.quit()

    def get_winner(self):
        pass

    def draw_winner(self, text):
        draw_text = self.WINNER_FONT.render(text, 1, self.WHITE)
        self.window.blit(draw_text,
                         (self.width / 2 - draw_text.get_width() / 2,
                          self.height / 2 - draw_text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(5000)

    def attck_handle(self):
        for bulet in self.Player_1.basic_att:
            bulet.x += self.b_vel
            if self.Player_2.rect.colliderect(bulet):
                pygame.event.post(pygame.event.Event(self.player2_hit))
                self.Player_1.basic_att.remove(bulet)
            elif bulet.x > self.width:
                self.Player_1.basic_att.remove(bulet)

        for bulet in self.Player_2.basic_att:
            bulet.x -= self.b_vel
            if self.Player_1.rect.colliderect(bulet):
                pygame.event.post(pygame.event.Event(self.player1_hit))
                self.Player_2.basic_att.remove(bulet)
            elif bulet.x < 0:
                self.Player_2.basic_att.remove(bulet)

    #fungsi ini agar player dapat berjalan
    def movement_handle(self, keys_pressed):
        if keys_pressed[
                pygame.K_a] and self.Player_1.rect.x - self.vel > 0:  # LEFT
            self.Player_1.rect.x -= self.vel
            self.Player_1.mundur()
        if keys_pressed[
                pygame.
                K_d] and self.Player_1.rect.x + self.Player_1.width_P + self.vel < self.batas.x:  # RIGHT
            self.Player_1.rect.x += self.vel
            self.Player_1.maju()
        if keys_pressed[
                pygame.K_w] and self.Player_1.rect.y - self.vel > 0:  # UP
            self.jump_1 = True
        # if keys_pressed[pygame.K_s] and self.Player_1.rect.y + self.Player_1.height_P + self.vel + 60 < self.height:  # DOWN
        #     self.Player_1.rect.y += self.vel

        if keys_pressed[
                pygame.
                K_LEFT] and self.Player_2.rect.x - self.vel > self.batas.x:  # LEFT
            self.Player_2.rect.x -= self.vel
        if keys_pressed[
                pygame.
                K_RIGHT] and self.Player_2.rect.x + self.vel < self.width - 50:  # RIGHT
            self.Player_2.rect.x += self.vel
        if keys_pressed[
                pygame.K_UP] and self.Player_2.rect.y - self.vel > 0:  # UP
            self.jump_2 = True
        # if keys_pressed[pygame.K_DOWN] and self.Player_2.rect.y + self.Player_2.height_P + self.vel + 60 < self.height:  # DOWN
        #     self.Player_2.rect.y += self.vel

        if self.jump_1:
            self.Player_1.jumping()

            if self.Player_1.jmp == False:
                self.jump_1 = False
                self.Player_1.jmp = True
        else:
            pass

        if self.jump_2:
            self.Player_2.jumping()

            if self.Player_2.jmp == False:
                self.jump_2 = False
                self.Player_2.jmp = True
        else:
            pass

    #fungsi untuk mendapatkan event terhadap kejadian pada game. Mis QUIT, PLAY, START, dll
    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(
                        self.Player_1.basic_att) < self.peluru:
                    bullet = pygame.Rect(
                        self.Player_1.rect.x + self.Player_1.width_P,
                        self.Player_1.rect.y + self.Player_1.height_P // 2 - 2,
                        10, 5)
                    self.Player_1.basic_att.append(bullet)
                if event.key == pygame.K_RCTRL and len(
                        self.Player_2.basic_att) < self.peluru:
                    bullet = pygame.Rect(
                        self.Player_2.rect.x,
                        self.Player_2.rect.y + self.Player_2.height_P // 2 - 2,
                        10, 5)
                    self.Player_2.basic_att.append(bullet)

            if event.type == self.player1_hit:
                self.Player_1.attack(self.Player_2.damage)

            if event.type == self.player2_hit:
                self.Player_2.attack(self.Player_1.damage)

    #fungsi ini untuk menampilkan tampilan game
    def draw_window(self):
        self.window.blit(self.bg, (0, 0))
        pygame.draw.rect(self.window, self.BLACK, self.batas)

        self.Player_1.display(self.window, True)
        self.Player_2.display(self.window, False)

        self.window.blit(self.Player_1.image,
                         (self.Player_1.rect.x, self.Player_1.rect.y))
        self.window.blit(self.Player_2.image,
                         (self.Player_2.rect.x, self.Player_2.rect.y))

        for bulet in self.Player_1.basic_att:
            pygame.draw.rect(self.window, self.RED, bulet)

        for bulet in self.Player_2.basic_att:
            pygame.draw.rect(self.window, self.GREEN, bulet)

        pygame.display.update()

    #fungsi ini instansiasi objek
    def load_player(self):
        self.Player_1 = Hero_1(100, 370)
        self.Player_2 = Hero_2(700, 370)

    #fungsi ini untuk membuat objek menu
    def load_menu():
        pass

    #Fungsi ini untuk membuat background dari game
    def background():
        text_surface = self.font.render(text, True, color)
        #text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)


if __name__ == "__main__":
    BB1v1 = Game()

    while BB1v1.running:
        BB1v1.loop()
