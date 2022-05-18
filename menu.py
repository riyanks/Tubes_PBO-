
###################################### Syafira ############################################3
def display_Menu(self, screen):
        play = False

        self.rect.y = self.original_y
        #posisi mouse
        pos_mouse = pygame.mouse.get_pos()

        #check jika posisi mouse berada pada gambar

        if self.rect.collidepoint(pos_mouse):
            if self.check:
                self.curs_sound.play()
                self.check = False
            
            self.rect.y = self.original_y + self.dinamic_elevation
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.butten_sound.play()
                self.image = self.image_elevation
                play = True
                self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked == False
                self.image = self.image_original
        else :
            self.check = True


        
        screen.blit(self.image, (self.rect.x, self.rect.y))
        

        return play
