""" March 19, 2021"""

"""
Priorities for March 19
1. Stay focused on functionality before cute features (weighted, undirected):
    - DONE -- Hover on edges (BUT NEED TO IMPROVE)
    - DONE -- Delete edges
    - DONE -- Edge weights
    - Calculate and export adjacency list
    - Calculate and export adjacency list

2. Refactoring and git pushes

3. Cute features
     - Make blobs distinct -- can almost be small hollow circles
     - Re-do all the colours of objects
        - DONE FOR NODES
     - Margins/borders
        - Does the main surface need a border? What would look nice?
        - Define a margin around the instructions. Maybe the whole right side?
     - Toggle full screen??
     - Edge weight rect to cover the edge behind the text weight

"""


import pygame

from settings import Settings
from helpers import Helpers
from graphobjects.node import Node
from graphobjects.edge import Edge


class Main:

    def __init__(self):
        pygame.init()

        ### Imports
        self.set = Settings()
        self.win = pygame.display.set_mode( (self.set.win_w, self.set.win_h) ) ## win must go after settings and before helpers
        self.h = Helpers(self.win)

        ### Not imports
        self.nodes = []
        self.edges = []


    """ CHECK EVENTS """

    def _check_events(self):
        self.mouse_coords = pygame.mouse.get_pos()  ## Update mouse_coords each cycle (not multiple times)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit(), quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_button_down_events()

            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_button_up_events()

            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)


    """ CHECK EVENTS -- HELPER FUNCTIONS """

    def mouse_button_down_events(self):
        if pygame.mouse.get_pressed()[0]:
            self.left_click_events()

        if pygame.mouse.get_pressed()[2]:
            self.right_click_events()


    def left_click_events(self):
        """ Double clicks make nodes/edges; single click drags node """

        hovering = self.h.get_hover_objects( self.nodes )
        double_click = self.h.check_dbclick()

        if not hovering and double_click:
            self.make_node()

        if hovering and not double_click:
            for node in self.nodes:
                node.start_moving()

        if hovering and double_click:
            self.make_edge()

    def right_click_events(self):
        """ Delete objects """

        hover_objects = self.h.get_hover_objects(self.nodes + self.edges)

        for object in hover_objects:
            if object in self.nodes:
                self.nodes.remove(object)
            else:
                self.edges.remove(object)

            object.die() ## Can't literally erase an object, so just set alive flag to False


    def mouse_button_up_events(self):
        self.connect_edge()

        for node in self.nodes:
            node.cancel_moving()

    def keydown_events(self, event):
        if event.key == pygame.K_q:
            pygame.quit(), quit()


    """ Make a node """
    def make_node(self):
        node = Node(self.win, self.mouse_coords)
        self.nodes.append(node)

    """ Make an edge """
    def make_edge(self):
        start_node = self.h.get_hover_objects(self.nodes)
        start_node = start_node[0]

        if start_node:
            edge = Edge(self.win, start_node)
            self.edges.append(edge)
            self.nodes.append(edge.get_fin_blob())

    def _update_edge_ends(self):
        """ Check if node for an edge has been deleted. If so, spawn a blob """

        for edge in self.edges:
            possible_blobs = edge.check_ends()

            for possible_blob in possible_blobs:
                if possible_blob:
                    self.nodes.append(possible_blob)

    def connect_edge(self):
        """ If drag blob onto node and mouse_up, attach the blob's edge to the node """

        connection_edge = blob = node = None

        moving_object = self.h.get_moving_object(self.nodes)
        hovering_objects = self.h.get_hover_objects(self.nodes)

        if moving_object and moving_object.is_blob():
            blob = moving_object

            for object in hovering_objects:
                if not object.is_blob:
                    node = object

        if node and blob:
            for edge in self.edges:
                if blob in edge.get_blobs:
                    edge.connect(node, blob)


    """ UPDATES """

    def _update_hovering(self):
        for object in self.nodes + self.edges:
            object.update_hovering()

    def _update_moving(self):
        for node in self.nodes:
            node.move()

    def _update_screen(self):
        """ UPDATE SCREEN """
        for object in self.edges + self.nodes:
            object.draw()

        self.h.print_instructions()

        pygame.display.update()


    """ MAIN """

    def main(self):

        while True:
            self.win.fill( self.set.black )
            self._check_events()
            self._update_hovering()
            self._update_moving()
            self._update_edge_ends()
            self._update_screen()

if __name__ == "__main__":
    mm = Main()
    mm.main()
