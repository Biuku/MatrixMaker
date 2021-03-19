""" March 17, 2021"""

import pygame

class Settings:

    def __init__(self):

        # pygame screen / window
        self.win_w = 1200
        self.win_h = 800

        ## google > rgb colour selector
        self.white, self.black = (255, 255, 255), (0, 0, 0),
        self.light_grey, self.grey, self.dark_grey = (200, 200, 200), (100,100,100), (75, 75, 75)
        self.blue, self.grey_blue = (164, 150, 255), (13, 0, 94)
        self.purple, self.red = (162, 50, 168), (235, 52, 52)

        ## Font
        self.small_font_size = 10
        self.med_font_size = 12
        self.small_font = pygame.font.SysFont('lucidasans', self.small_font_size)
        self.med_font = pygame.font.SysFont('lucidasans', self.med_font_size)

        ## Double click control
        self.db_clock = pygame.time.Clock()
        self.db_timer = 0
        self.db_max_time = 400

        self.mouse_coords = pygame.mouse.get_pos()
