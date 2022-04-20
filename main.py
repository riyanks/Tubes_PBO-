import pygame , os


class Game():
    def  __init__ (self):
        pygame.init()
        self.width , self.height = 900 , 500
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("1v1 Bang-Bang")
        self.run , self.running = True, True

    def loop (self):
        while self.run:
            self.get_event()



    def get_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                pygame.quit()







if __name__ == "__main__":
    BB1v1 = Game()
     
    while BB1v1.running:
        BB1v1.loop()


