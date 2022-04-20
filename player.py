from main import Game
import pygame , os

#class untuk hero yang akan dimainkan 
class Hero(Game):
    def __init__ (self,nama,  health, armor, damage):
        Game.__init__(self)
        self.nama = nama
        self.health = health 
        self.armor = armor
        self.damage = damage

        self.__regen = 2
        self.width_P , self.height_P = 20, 40


    def attack(self):
        pass

    def defend(self):
        pass

    def regen(self):
        self.damage += self.__regen

    def display(self):
        pass

    def hotkey(self):
        self.get_event()


class Hero_1(Hero):
    def __init__ (self):
        super.__init__("layla", 10, 2, 5)

    def win_lose(self):
        pass

    def sound(self):
        pass

    def display_weapon(self):
        pass


class Hero_2(Hero):
    def __init__ (self):
        super.__init__("esper", 10, 2, 5)

    def win_lose(self):
        pass

    def sound(self):
        pass

    def display_weapon(self):
        pass


class Hero_3(Hero):
    def __init__ (self):
        super.__init__("Goblin", 10, 2, 5)

    def win_lose(self):
        pass

    def sound(self):
        pass

    def display_weapon(self):
        pass