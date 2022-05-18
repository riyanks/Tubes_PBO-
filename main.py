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

