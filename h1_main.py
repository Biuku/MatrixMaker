""" March 17, 2021"""

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
        hovering = self.h.check_hovering( self.nodes )
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
        for node in self.nodes:
            if node.get_hovering():
                self.nodes.remove(node)
                node.die() ## Can't literally erase an object, so just set alive flag to False

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
        start_node = self.h.get_hovering(self.nodes)
        start_node = start_node[0]

        if start_node:
            edge = Edge(self.win, start_node)
            self.edges.append(edge)
            self.nodes.append(edge.get_fin_blob())

    def _update_edge_ends(self):
        """
        Check if node for an edge has been deleted.
        If so, spawn a blob
        """
        for edge in self.edges:
            possible_blobs = edge.check_ends()

            for possible_blob in possible_blobs:
                if possible_blob:
                    self.nodes.append(possible_blob)

    def connect_edge(self):
        connection_edge = connection_blob = connection_node = None

        moving_node = self.h.get_moving(self.nodes)
        hovering = self.h.get_hovering(self.nodes)

        if moving_node and moving_node.get_is_blob():
            connection_blob = moving_node
            if hovering:
                for node in hovering:
                    if not node.get_is_blob:
                        connection_node = node

        if connection_node and connection_blob:
            for edge in self.edges:
                if connection_blob in edge.get_blobs:
                    connection_edge = edge

        if connection_edge:
            connection_edge.connect(connection_node, connection_blob)


    """ UPDATES """

    def _update_hovering(self):
        for node in self.nodes:
            node.update_hovering()

    def _update_moving(self):
        for node in self.nodes:
            node.move()

    def _update_screen(self):
        """ UPDATE SCREEN """

        for edge in self.edges:
            edge.draw()

        for node in self.nodes:
            node.draw()

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

x = Main()
x.main()
