import pygame , os
from abc import ABC , abstractmethod
#class untuk hero yang akan dimainkan 
class Hero(ABC):
    def __init__ (self , nama,  health, armor, damage, gambar, posisi_x, posisi_y):
        pygame.init()
        self.nama = nama
        self.health = health 
        self.health_def = health/2
        self.current_health = 200
        self.armor = armor
        self.damage = damage
        self.width_P , self.height_P = 80 , 90
        self.basic_image = gambar
        self.image = pygame.transform.scale( self.basic_image , (self.width_P , self.height_P))
        self.rect = pygame.Rect(posisi_x, posisi_y ,self.width_P , self.height_P)
        self.__regen = 2
        
        self.health_bar_length = 300
        self.health_ratio = self.health / self.health_bar_length
        self.health_change_speed = 7

        self.basic_att = []
        self.v_jump = 20

        self.jmp = True


    @abstractmethod
    def dead (self):
        pass

    @abstractmethod
    def maju (self):
        pass
    
    @abstractmethod
    def mundur (self):
        pass

    def basic_action (self):
        self.image = pygame.transform.scale( self.basic_image , (self.width_P , self.height_P))
        return self.image

    def jumping (self):
        gravitasi = 1
        self.rect.y -= self.v_jump
        self.v_jump -= gravitasi

        if self.v_jump < - 20:
            self.v_jump = 20
            self.jmp = False    
    
    def display (self, screen, check):
        transition_width = 0
        transition_color = (255,0,0)

        if self.current_health < self.health:
            self.current_health += self.health_change_speed

            transition_width = int((self.health - self.current_health) / self.health_ratio)
            transition_color = (0,255,0)
        
        if self.current_health > self.health:
         
            self.current_health -= self.health_change_speed
            transition_width = int((self.health - self.current_health) / self.health_ratio)
            transition_color = (255,255,0)

        if check == True:
            health_bar_width = int(self.current_health / self.health_ratio)
            health_bar = pygame.Rect(10 ,10,health_bar_width ,25)
            transition_bar = pygame.Rect(health_bar.right, 10,transition_width,25)

            pygame.draw.rect(screen,(255,0,0),health_bar)
            pygame.draw.rect(screen,transition_color,transition_bar)	
            pygame.draw.rect(screen,(255,255,255),(10,10,self.health_bar_length,25),4)	

        if check == False :
            health_bar_width = int(self.current_health / self.health_ratio)
            health_bar = pygame.Rect(800 - (health_bar_width),10,health_bar_width,25)
            transition_bar = pygame.Rect(health_bar.left,10,transition_width,25)

            pygame.draw.rect(screen,(255,0,0),health_bar)
            pygame.draw.rect(screen,transition_color,transition_bar)	
            pygame.draw.rect(screen,(255,255,255),(800-self.health_bar_length,10,self.health_bar_length,25),4)	

    def attack(self, enemy_damage):
        pass

    def defend(self, enemy_damage):
        if self.health > 0 :
            if self.health < self.health_def and self.armor > 1:
                self.health -= enemy_damage/self.armor
                self.armor -=1
                
            else :
                self.health -= enemy_damage
              
        else :
            self.health = 0

    def regen(self):
        self.damage += self.__regen


class Hero_1(Hero):
    def __init__ (self, react_x, react_y):
        self.Hero_G = pygame.image.load(os.path.join('Assets', 'hero1_diam_c.png'))
        Hero.__init__(self, "Mr.Spy", 1250, 10, 400 , self.Hero_G, react_x, react_y)


    def dead(self):
        dead_image = pygame.image.load(os.path.join('Assets', 'Hero1_mati.png'))
        self.image  = pygame.transform.scale(dead_image , (120 , 80))

    def maju(self):
        maju_image = pygame.image.load(os.path.join('Assets', 'Hero1_maju.png'))
        self.image = pygame.transform.scale(maju_image, (self.width_P , self.height_P))

    def mundur (self):
        mundur_image = pygame.image.load(os.path.join('Assets', 'Hero1_mundur.png'))
        self.image = pygame.transform.scale(mundur_image, (self.width_P , self.height_P))


    def attack(self):
        pass
            
    def win_lose(self):
        pass

    def sound(self):
        pass

    def display_weapon(self):
        pass


class Hero_2(Hero):
    def __init__ (self, react_x, react_y):
        self.Hero_G = pygame.image.load(os.path.join('Assets', 'Hero2_diam.png'))
        Hero.__init__(self, "Eptical Boy", 1800, 7, 250, self.Hero_G, react_x, react_y)

        self.dead_image = pygame.image.load(os.path.join('Assets', 'Hero2_mati.png'))

    def dead(self):
        self.image  = pygame.transform.scale(self.dead_image , (120,80))
    
    def maju(self):
        maju_image = pygame.image.load(os.path.join('Assets', 'Hero2_maju.png'))
        self.image = pygame.transform.scale(maju_image , (self.width_P , self.height_P))

    def mundur (self):
        mundur_image = pygame.image.load(os.path.join('Assets', 'Hero2_mundur.png'))
        self.image = pygame.transform.scale(mundur_image, (self.width_P , self.height_P))


    def win_lose(self):
        pass

    def sound(self):
        pass

    def display_weapon(self):
        pass


class Hero_3(Hero):
    def __init__ (self, react_x, react_y):
        self.Hero_G = pygame.image.load(os.path.join('Assets', 'Hero3_diam.png'))
        Hero.__init__(self, "Mr gun gun", 2000, 6, 100, self.Hero_G, react_x, react_y)

        self.dead_image = pygame.image.load(os.path.join('Assets', 'Hero3_mati.png'))

    def dead(self):
        self.image  = pygame.transform.scale(self.dead_image , (120 , 80))
    
    def maju(self):
        maju_image = pygame.image.load(os.path.join('Assets', 'Hero3_maju.png'))
        self.image = pygame.transform.scale(maju_image , (self.width_P , self.height_P))

    def mundur (self):
        mundur_image = pygame.image.load(os.path.join('Assets', 'Hero3_mundur.png'))
        self.image = pygame.transform.scale(mundur_image, (self.width_P , self.height_P))
    def win_lose(self):
        pass

    def sound(self):
        pass

    def display_weapon(self):
        pass
