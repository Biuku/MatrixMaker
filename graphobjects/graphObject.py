""" March 17, 2021 """

import pygame
from settings import Settings

class GraphObject:

    def __init__(self, win):
        self.win = win
        self.set = Settings()
        self.hovering = False
        self.suppress_hovering = True
        self.moving = False
        self.alive = True ## When you delete a node from self.nodes, it doesn't die

    """ Hovering """
    def set_hovering(self):
        self.hovering = True

    def cancel_hovering(self):
        self.hovering = False

    def get_hovering(self):
        return self.hovering


    """ Moving """
    def set_moving(self):
        self.moving = True

    def cancel_moving(self):
        self.moving = False

    def get_moving(self):
        return self.moving

    """ Kill a deleted object """
    def die(self):
        self.alive = False

    def is_alive(self):
        return self.alive

    """ Something """
    def get_draw_colour(self):

        if self.get_hovering():
            return self.hover_colour

        return self.colour


    """ Calculate euclidian distance """
    def euclid(self, coords1, coords2):
        x1, y1 = coords1
        x2, y2 = coords2

        return ( (x2-x1)**2 + (y2-y1)**2)**0.5
