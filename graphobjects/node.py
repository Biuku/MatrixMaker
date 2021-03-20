""" March 19, 2021 """

import pygame
from graphobjects.graphObject import GraphObject

class Node(GraphObject):

    def __init__(self, win, coords, name = "", blob = False):
        super().__init__(win)
        self.radius = 20
        self.colour = self.set.node_colour

        self.hover_margin = self.radius * 1.2
        self.name = name
        self.font = self.set.small_font
        self.font_size = self.set.small_font_size

        self.blob_status = blob
        self.blob_radius = 5
        self.blob_colour = self.set.red

        self.coords = coords


    def draw(self):
        fill_colour = self.get_draw_colour()
        #if self.is_blob():
        #    fill_colour = self.blob_colour
        radius = self.radius

        ## If not blob, draw a border around the node, and draw the node name on top
        if self.is_alive():
            if not self.is_blob():
                pygame.draw.circle(self.win, fill_colour, self.coords, radius, 0)
                pygame.draw.circle(self.win, self.set.node_ring, self.coords, radius+1, 1)
                self._draw_name()

            else:
                radius = self.blob_radius
                pygame.draw.circle(self.win, fill_colour, self.coords, radius, 0)
                #pygame.draw.circle(self.win, self.set.white, self.coords, radius, 2)

    def _draw_name(self):
        colour = self.set.node_font_colour
        font = self.set.small_font_size ## Just for calibrating letter position
        x, y = self.get_coords()
        fx = x - (self.font_size * 0.3)
        fy = y - (self.font_size * 0.7)

        if len(self.name) > 1:
            fx = x - (self.font_size * 0.7)

        text = self.font.render(self.name, True, colour)
        self.win.blit(text, (fx, fy))


    def get_coords(self):
        return self.coords


    def update_hovering(self):
        self.cancel_hovering()

        mouse_coords = pygame.mouse.get_pos()
        proximity = self.euclid(self.coords, mouse_coords)

        if proximity < self.hover_margin:
            if not self.suppress_hovering:
                self.set_hovering()
        else:
            self.suppress_hovering = False


    """ MOVING FUNCTIONS """

    def move(self):
        mouse = pygame.mouse.get_pos()

        if self.moving and not self.get_moving_collision(mouse):
                self.coords = mouse

    def get_moving_collision(self, mouse):
        x, y = mouse

        left = self.set.border_left + (self.radius * 1.3)
        right = self.set.border_right - (self.radius * 1.3)
        top = self.set.border_top + (self.radius * 1.3)
        bot = self.set.border_bottom - (self.radius * 1.3)

        if x > right or x < left:
            return True

        if y > bot or y < top:
            return True

        return False


    """ BLOB STUFF """
    def is_blob(self):
        return self.blob_status


    def update_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name
