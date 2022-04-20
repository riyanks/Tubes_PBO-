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

    def load_player():
        pass

    def load_menu():
        pass

    def get_FPS():
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

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


