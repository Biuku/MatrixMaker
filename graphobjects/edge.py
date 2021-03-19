""" March 18, 2021 """

import pygame
from graphobjects.graphObject import GraphObject
from graphobjects.node import Node

class Edge(GraphObject):

    def __init__(self, win, start_node):
        super().__init__(win)
        self.colour = self.set.light_grey
        self.hover_colour = self.set.blue
        self.thickness = 2
        self.hover_tolerance = 7 ## Pixels from edge line
        self.init_blob_distance = 100 ## How far from the start node to move the blob when created
        self.font = self.set.small_font ## For edge weights

        ## Variables
        self.start = start_node
        self.fin = self.init_blob()


    def get_fin_blob(self):
        return self.fin


    def check_ends(self):
        new_start_blob = new_fin_blob = None
        if not self.start.is_alive():
            coords = self.start.get_coords()
            new_start_blob = self.create_blob(coords, 0)

        if not self.fin.is_alive():
            coords = self.fin.get_coords()
            new_fin_blob = self.create_blob(coords, 1)

        return [new_start_blob, new_fin_blob]


    def create_blob(self, coords, end):
        if end == 0: # Start
            self.start = Node(self.win, coords, True)
            return self.start
        if end == 1: # Find
            self.fin = Node(self.win, coords, True)
            return self.fin


    def init_blob(self):
        x, y = self.start.get_coords()
        x += self.init_blob_distance
        y += self.init_blob_distance

        return Node(self.win, (x, y), True) # True = it is a blob

    def draw(self):
        colour = self.get_draw_colour()

        start_coords = self.start.get_coords()
        fin_coords = self.fin.get_coords()

        pygame.draw.line(self.win, colour, start_coords, fin_coords, self.thickness)

    def connect(self, node, blob):
        for object in [self.start, self.fin]:
            if object == blob:
                object = node

    def update_hovering(self):
        pass
