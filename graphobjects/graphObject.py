""" March 19, 2021 """

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

        self.hover_colour = self.set.hover_colour

    """ Hovering """
    def set_hovering(self):
        self.hovering = True

    def cancel_hovering(self):
        self.hovering = False

    def get_hovering(self):
        return self.hovering


    """ select hover colour or node colour """
    def get_draw_colour(self):

        if self.get_hovering():
            return self.hover_colour

        return self.colour


    """ Moving """
    def set_moving(self):
        if self.get_hovering():
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


    """ Calculate euclidian distance """
    def euclid(self, coords1, coords2):
        x1, y1 = coords1
        x2, y2 = coords2

        return ( (x2-x1)**2 + (y2-y1)**2)**0.5


    """ Edge weights """


    def get_edge_midpoint_coords(self, start_coords, fin_coords):
        x, y = start_coords
        x1, y1 = fin_coords

        xR = (x1-x)//2 + x
        yR = (y1-y)//2 + y

        return xR, yR


    """ Edge proximity finder -- for calculating distance from mouse to edge """
    """ NOTE -- THIS ONLY WORKS FOR MORE-HORIZONTAL LINES. NEED BETTER SOLUTION. """
    def edge_proximity_finder(self, start, end, point):
        m = self.edge_get_slope(start, end) # slope of edge
        delta_x = point[0] - start[0] # Get Δx from point to start_node
        relative_delta_y = m * delta_x # Get where point vertically intersects edge
        b = start[1] + (relative_delta_y) # convert relative vertical intercept to graph coordinate
        deviation = abs(b - point[1])  #Find vertical deviation between point and its y intercept of the edge

        return deviation

    def edge_get_slope(self, start, end):
        delta_x, delta_y = self.edge_get_deltas(start, end)

        if delta_x == 0:
            delta_x = 0.0001 # Edge case -- prevent divide by 0

        return delta_y/delta_x

    def edge_get_deltas(self, s, e):
        x, y = s[0], s[1]
        x1, y1 = e[0], e[1]

        delta_x = x1 - x
        delta_y = y1 - y

        return delta_x, delta_y
