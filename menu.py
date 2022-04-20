from main import Game
import pygame , os
import rectangle

#class untuk menampilkan menu
class Menu(Game):
    def __init__ (self, nama, gambar, sound):
        Game.__init__(self)
        self.width_M , self.height_M = 20, 60
        self.run = True
        self.rectangle = None
        self.gambar = gambar
        self.sound = sound
        self.nama = nama

    def display_Menu(self):
        pass

    def check_input(self):
        pass


class Start (Menu):
    def __init__ (self, gambar, sound):
        Super.__init__ ("Start", gambar, sound)

    def update(self):
        pass


class Option (Menu):
    def __init__ (self, gambar, sound):
        Super.__init__ ("Option", gambar, sound)

    def update(self):
        pass
    
    def setting_sound(self):
        pass

    def setting_display(self):
        pass

class Exit (Menu):
    def __init__ (self, gambar, sound):
        Super.__init__ ("Exit", gambar, sound)

    def update(self):
        pass

class load_game (Menu):
    def __init__ (self, gambar, sound):
        Super.__init__ ("LOAD", gambar, sound)

    def update(self):
        pass
    