""" March 17, 2021 """

import pygame
from graphobjects.graphObject import GraphObject

class Node(GraphObject):

    def __init__(self, win, coords, blob = False):
        super().__init__(win)
        self.radius = 20
        #self.colour = self.set.light_grey
        self.colour = self.set.purple
        self.hover_colour = self.set.blue
        self.hover_margin = self.radius * 1.2

        self.blob_status = blob
        self.blob_radius = 10

        self.coords = coords


    def draw(self):
        fill_colour = self.get_draw_colour()
        radius = self.get_radius()

        pygame.draw.circle(self.win, fill_colour, self.coords, radius, 0)

        if not self.is_blob():
            pygame.draw.circle(self.win, self.set.dark_grey, self.coords, radius+1, 2)


    def get_radius(self):
        if self.is_blob():
            return self.blob_radius

        return self.radius


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

    def start_moving(self):
        if self.hovering:
            self.moving = True

    def move(self):
        if self.moving:
            self.coords = pygame.mouse.get_pos()


    """ BLOB STUFF """
    def is_blob(self):
        return self.blob_status
