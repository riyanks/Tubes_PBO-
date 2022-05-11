import pygame , os

#class ini merupakan kelas dari seluruh tampilan dan inisialisasi game
class Game(): 
    def  __init__ (self):
        pygame.init()
        self.width , self.height = 900 , 500 #lebar jendela window
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("1v1 Bang-Bang") #judul window
        self.run , self.running = True, True #varibel untuk mengecek kejadian 

    #fungsi ini untuk melakukan perulangan terhadap game
    def loop (self):
        while self.run:
            self.get_event()

    #fungsi untuk mendapatkan event terhadap kejadian pada game. Mis QUIT, PLAY, START, dll
    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                pygame.quit()

    #fungsi ini untuk membuat objek hero yang akan dipilih
    def load_player():
        pass

    #fungsi ini untuk membuat objek menu
    def load_menu():
        pass

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




if __name__ == "__main__":
    BB1v1 = Game()
     
    while BB1v1.running:
        BB1v1.loop()


