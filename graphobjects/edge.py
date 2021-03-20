""" March 19, 2021 """

import pygame
from graphobjects.graphObject import GraphObject
from graphobjects.node import Node

class Edge(GraphObject):

    def __init__(self, win, start_node):
        super().__init__(win)
        self.colour = self.set.edge_colour
        self.thickness = 2
        self.hover_margin = 5 ## Pixels from edge line
        self.init_blob_distance = 100 ## How far from the start node to move the blob when created
        self.font = self.set.small_font ## For edge weights
        self.edge_weight = 0

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
        """ Print the edge's weight (length in pixels) at its midpoint """

        colour = self.set.edge_weight_font_colour

        ## Update edge weight
        self.edge_weight = int(self.euclid(start_coords, fin_coords))
        midpoint_coords = self.get_edge_midpoint_coords(start_coords, fin_coords)
        self.draw_edge_weight_rect(midpoint_coords) ## Draw mask for weight to print on

        text = str(self.edge_weight)
        print_edge_weight = self.font.render(text, True, colour)
        self.win.blit( print_edge_weight, midpoint_coords )


    def draw_edge_weight_rect(self, midpoint):
        """ Cover the edge with a rect so the weight is easy to read """
        fill_colour = self.set.screen_background_colour

        x = midpoint[0] - 4
        y = midpoint[1]
        width, height = 30, 15
        pygame.draw.rect(self.win, fill_colour, (x, y, width, height), 0)
        pygame.draw.rect(self.win, self.colour, (x, y, width, height), 1 ) ## border


    def get_fin_blob(self):
        """ When creating an edge object, send back the blob to add to self.nodes """
        return self.fin


    def get_blobs(self):
        blobs = []
        for node in [self.start, self.fin]:
            if node.is_blob():
                blobs.append(node)

        return blobs


    def get_nodes(self):
        """ Return 2 nodes only if start and fin of edge are not blobs.
            For building the adjacency matrix """

        nodes = []
        for node in [self.start, self.fin]:
            if not node.is_blob():
                nodes.append(node)

        if len(nodes) == 2:
            return nodes

        return []

    def get_weight(self):
        return self.edge_weight



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
            self.start = blob = Node(self.win, coords, "", True)

        else:
            self.fin = blob = Node(self.win, coords, "", True)

        return blob


    def init_blob(self):
        """ Defines where an edge is spawned by placing new (fin) blob a set x,y distance from start_node """

        x, y = self.start.get_coords()
        x += self.init_blob_distance
        y += self.init_blob_distance

        return Node(self.win, (x, y), "", True) # "" = no name; True = it is a blob


    def connect(self, node, blob):
        """ Connect an end of an edge to an existing node """
        if self.start == blob:
            self.start = node

        else:
            self.fin = node


    def get_draw_colour(self):
        """ Draw edge with normnal colour or hover colour """

        if self.get_hovering():
            return self.hover_colour

        return self.colour
