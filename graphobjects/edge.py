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
        self.hover_margin = 5 ## Pixels from edge line
        self.init_blob_distance = 100 ## How far from the start node to move the blob when created
        self.font = self.set.small_font ## For edge weights

        ## Variables
        self.start = start_node
        self.fin = self.init_blob()


    def draw(self):
        """ Draw the edge as line between start/end nodes; draw the edge weight (int) """
        colour = self.get_draw_colour()
        start_coords = self.start.get_coords()
        fin_coords = self.fin.get_coords()

        pygame.draw.line(self.win, colour, start_coords, fin_coords, self.thickness)

        self.draw_edge_weight(start_coords, fin_coords)


    def draw_edge_weight(self, start_coords, fin_coords):
        """ Draw the length (in pixels) of the edge at its midpoint """

        ## Update edge weight
        self.edge_weight = int(self.euclid(start_coords, fin_coords))

        midpoint_coords = self.get_edge_midpoint_coords(start_coords, fin_coords)
        self.draw_edge_weight_rect(midpoint_coords) ## Draw mask for weight to print on

        text = str(self.edge_weight)
        print_edge_weight = self.font.render(text, True, self.set.white)

        self.win.blit( print_edge_weight, midpoint_coords )


    def draw_edge_weight_rect(self, midpoint):
        """ Cover the edge with a rect so the weight is easy to read """

        x = midpoint[0] - 4
        y = midpoint[1]
        w, h = 30, 15
        pygame.draw.rect(self.win, self.set.black, (x, y, w, h), 0)
        pygame.draw.rect(self.win, self.set.grey, (x, y, w, h), 1 ) ## border


    def get_fin_blob(self):
        return self.fin


    def update_hovering(self):
        """ Change colour and hover flag if mouse hovering on edge """

        self.cancel_hovering()

        start = self.start.get_coords()
        fin = self.fin.get_coords()

        mouse_coords = pygame.mouse.get_pos()
        proximity = self.edge_proximity_finder(start, fin, mouse_coords)

        if proximity < self.hover_margin:

            self.set_hovering()


    def check_ends(self):
        """ Check whether a start or fin node was deleted. Replace any with new blob. """

        start_blob = fin_blob = None

        if not self.start.is_alive():
            coords = self.start.get_coords()
            start_blob = self.create_blob(coords, 0)

        if not self.fin.is_alive():
            coords = self.fin.get_coords()
            fin_blob = self.create_blob(coords, 1)

        ## Send any new blobs back to Main to include in self.nodes list
        return [start_blob, fin_blob]


    def create_blob(self, coords, end):
        """ if the edge's start/fin node has been deleted, create a blob to replace it """
        if end == 0: # Start
            self.start = blob = Node(self.win, coords, True)

        else:
            self.fin = blob = Node(self.win, coords, True)

        return blob


    def init_blob(self):
        """ Defines where an edge is spawned by placing new (fin) blob a set x,y distance from start_node """

        x, y = self.start.get_coords()
        x += self.init_blob_distance
        y += self.init_blob_distance

        return Node(self.win, (x, y), True) # True = it is a blob


    def connect(self, node, blob):
        for object in [self.start, self.fin]:
            if object == blob:
                object = node
