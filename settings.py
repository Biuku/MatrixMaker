""" March 17, 2021"""

import pygame

class Settings:

    def __init__(self):

        # pygame screen / window
        self.win_w = 1910
        self.win_h = 1070

        ## google > rgb colour selector
        self.white, self.black = (255, 255, 255), (0, 0, 0)
        self.light_grey, self.grey, self.dark_grey = (200, 200, 200), (100,100,100), (45, 45, 45)
        self.blue, self.grey_blue = (164, 150, 255), (13, 0, 94)
        self.purple, self.red = (22, 1, 97), (235, 52, 52)
        self.green = (35, 130, 60)


        """ COLOUR STYLES """
        self.hulu_yellow_subtitle = (255, 204, 0)


        ### Data Viz Colour Style -- dark
        self.dv_dark_background = (21, 40, 54)
        self.dv_grey_object = (87, 110, 124)

        ## Data Viz colour pallett
        #self.hover_colour = self.blue
        #self.node_colour = self.dv_grey_object
        #self.instructions_font_colour = self.hulu_yellow_subtitle
        #self.screen_background_colour = self.dv_dark_background


        ### 538 white colour style
        self.background_538 = self.white
        self.object1_538 = (217, 240, 222)
        self.object2_538 = (255, 234, 217)
        self.light_grey_object_538 = (221, 221, 221)

        ### 538 COLOUR PALLETT
        self.screen_background_colour = self.background_538
        self.node_colour = self.object1_538
        self.hover_colour = self.light_grey_object_538
        self.node_ring = self.hover_colour
        self.edge_colour = self.light_grey
        self.node_font_colour = self.grey
        self.edge_weight_font_colour = self.light_grey
        self.instructions_font_colour = self.light_grey
        self.am_font_colour = self.node_font_colour


        ## Page border
        self.page_margin = 0.02 ## % of screen that is unused margi
        self.border_top = self.win_h * self.page_margin
        self.border_bottom = self.win_h * (1-self.page_margin)
        self.border_right = self.win_w *(1-self.page_margin)
        self.border_left = self.win_w * self.page_margin
        self.border_thickness = 4
        self.border_colour = self.light_grey

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
