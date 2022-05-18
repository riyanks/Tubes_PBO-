import pygame , os
from player import *
from menu import *
from pygame import mixer
pygame.font.init()

#class ini merupakan kelas dari seluruh tampilan dan inisialisasi game
class Game(): 
    def  __init__ (self):
        pygame.init()
        self.width , self.height = 800 , 500 #lebar jendela window
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("1v1 Bang-Bang") #judul window
        self.run = True #varibel untuk mengecek kejadian 
        self.FPS = 60
        self.vel = 5
        self.b_vel = 7
        self.WINNER_FONT = pygame.font.SysFont('comicsans', 100)
        self.bg = pygame.transform.scale( pygame.image.load(os.path.join('Assets', 'background_1.png')) , (self.width , self.height))
        self.bg_menu = pygame.transform.scale( pygame.image.load(os.path.join('Assets', 'bg_menu.png')) , (self.width , self.height))
        self.menuhome = pygame.transform.scale( pygame.image.load(os.path.join('Assets', 'bg_menuhome.png')) , (self.width , self.height))
        self.batas = pygame.Rect(self.width//2 - 5 , 0 , 10, self.height)

        self.player1_hit = pygame.USEREVENT + 1
        self.player2_hit = pygame.USEREVENT + 2
        self.peluru = 2


        #sound
        
        self.Start = None
        self.Quit = None
        self.Player_1 = None
        self.Player_2 = None

        self.jump_1 = False 
        self.jump_2 = False 

        #atribut background
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0,0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)

    #fungsi ini untuk melakukan perulangan terhadap game
    def loop (self):
        clock =  pygame.time.Clock()
        mixer.music.load('Assets/sound_war.wav')
        mixer.music.play(-1)
        while self.run:
            clock.tick(self.FPS)
            
            self.get_event()

            keys_pressed = pygame.key.get_pressed()
            self.movement_handle(keys_pressed)
            self.attck_handle()         
            self.draw_window()   

            if self.Player_1.health <= 0 or self.Player_2.health <= 0:
                pygame.time.delay(4000)    
                break 
        self.login_game()
        
    def get_winner (self):
        winner_text = ""
        if self.Player_1.current_health <= 0:
                self.Player_1.dead()
                winner_text = "Player 2 Wins!"

        if self.Player_2.current_health <= 0:
                self.Player_2.dead()
                winner_text = "Player 1 Wins!"

        if winner_text != "":
            draw_text = self.WINNER_FONT.render(winner_text, 1, self.WHITE)
            self.window.blit(draw_text, (self.width/2 - draw_text.get_width() /2, self.height/2 - draw_text.get_height()/2))
        
    def endgame(self):
        self.window.blit(self.bg_menu, (0,0))


        startimg = pygame.image.load(os.path.join('Assets', 'Start.png'))
        quitimg = pygame.image.load(os.path.join('Assets', 'Quit.png'))

        playagain = Menu(startimg, self.width/4, 250, 150, 150)
        Exit = Menu(quitimg, self.width*(2/4) + 50, 250, 150, 150)

        if playagain.display_Menu(self.window):
            self.loop()
            
        if Exit.display_Menu(self.window):
            self.run = False

        pygame.display.update()
        
    def attck_handle(self):
        for bulet in self.Player_1.basic_att:
            bulet.x += self.b_vel
            if self.Player_2.rect.colliderect(bulet):
                pygame.event.post(pygame.event.Event(self.player2_hit))
                self.Player_1.basic_att.remove(bulet)
            elif bulet.x > self.width :
                self.Player_1.basic_att.remove(bulet)

        for bulet in self.Player_2.basic_att:
            bulet.x -= self.b_vel
            if self.Player_1.rect.colliderect(bulet):
                pygame.event.post(pygame.event.Event(self.player1_hit))
                self.Player_2.basic_att.remove(bulet)
            elif bulet.x < 0 :
                self.Player_2.basic_att.remove(bulet)

    #fungsi ini agar player dapat berjalan 
    def movement_handle (self, keys_pressed):
        if keys_pressed[pygame.K_a] and self.Player_1.rect.x - self.vel > 0 :  # LEFT
            self.Player_1.rect.x -= self.vel
            self.Player_1.mundur()
        if keys_pressed[pygame.K_d] and self.Player_1.rect.x + self.Player_1.width_P  + self.vel < self.batas.x:  # RIGHT
            self.Player_1.rect.x += self.vel
            self.Player_1.maju()
        if keys_pressed[pygame.K_w] and self.Player_1.rect.y - self.vel > 0: # UP
            self.jump_1 = True       
        # if keys_pressed[pygame.K_s] and self.Player_1.rect.y + self.Player_1.height_P + self.vel + 60 < self.height:  # DOWN
        #     self.Player_1.rect.y += self.vel

        if keys_pressed[pygame.K_LEFT] and self.Player_2.rect.x - self.vel > self.batas.x:  # LEFT
            self.Player_2.rect.x -= self.vel
            self.Player_2.maju()
        if keys_pressed[pygame.K_RIGHT] and self.Player_2.rect.x + self.vel < self.width - 50:  # RIGHT
            self.Player_2.rect.x += self.vel
            self.Player_2.mundur()
        if keys_pressed[pygame.K_UP] and self.Player_2.rect.y - self.vel > 0:  # UP
            self.jump_2 = True
        # if keys_pressed[pygame.K_DOWN] and self.Player_2.rect.y + self.Player_2.height_P + self.vel + 60 < self.height:  # DOWN
        #     self.Player_2.rect.y += self.vel

        if self.jump_1 :
            self.Player_1.jumping()

            if self.Player_1.jmp == False:
                self.jump_1 = False
                self.Player_1.jmp = True
        else :
            pass

        if self.jump_2 :
            self.Player_2.jumping()

            if self.Player_2.jmp == False:
                self.jump_2 = False
                self.Player_2.jmp = True
        else :
            pass
