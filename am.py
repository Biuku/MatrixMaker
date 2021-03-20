""" March 20, 2021 """

import pygame
from settings import Settings

class AdjacencyMatrixBuilder:

    def __init__(self, win):
        self.set = Settings()
        self.win = win
        self.am = [] # Adjacency matrix

        self.nodes = []
        self.node_names = []

        self.col_gap = 27
        self.row_gap = 25


    def build_am(self, edges):

        self.nodes, valid_edges = self.get_valid_objects(edges)

        if self.nodes:
            self.get_node_names()
            self.alphabeticalize_nodes_list()
            self.reset_am_array()

            node_lookups = self.get_node_lookups() ## Links node names to


            for edge in valid_edges:
                start, fin = edge.get_nodes()
                weight = edge.get_weight()

                i = node_lookups[start]
                j = node_lookups[fin]

                self.am[i][j] = weight
                self.am[j][i] = weight


    def get_node_lookups(self):
        """ Build dict for easy lookups of index location of node names """
        node_lookups = {}

        for i, name in enumerate(self.nodes):
            node_lookups[name] = i

        return node_lookups



    def draw_am(self):
        x = left_edge = self.set.win_w * 0.80 ## lower number --> leftward
        y = self.set.win_h * 0.25 ## lower number --> upward

        ## To do -- make top index
        y = self.draw_am_top_row(x, y)

        row_index = self.node_names

        for row in self.am:
            ### Print the node name for this row
            text = row_index.pop(0)
            print_item = self.set.small_font.render(text, True, self.set.am_font_colour)
            self.win.blit( print_item, (x, y) )
            x += self.col_gap

            for item in row:
                print_item = self.set.small_font.render(str(item), True, self.set.am_font_colour)
                self.win.blit( print_item, (x, y) )
                x += self.col_gap
            y += self.row_gap
            x = left_edge


    def draw_am_top_row(self, x, y):
        colour = self.set.am_font_colour
        x += self.col_gap

        for node_name in self.node_names:
            print_item = self.set.small_font.render(node_name, True, colour)
            self.win.blit( print_item, (x, y) )
            x += self.col_gap

        y += self.row_gap

        return y


    def get_node_names(self):
        """Build list of the string names of the valid_nodes, sorted alphabetically"""
        self.node_names = []

        for node in self.nodes:
            self.node_names.append(node.get_name())

        self.node_names.sort()


    def alphabeticalize_nodes_list(self):
        """ I want self.nodes to be in the same order as self.node_names """
        arr = []

        for name in self.node_names:
            for node in self.nodes:
                if name == node.get_name():
                    arr.append(node)
                    break

        self.nodes = arr


    def get_valid_objects(self, edges):
        """ Get only the nodes 1) attached to edges 2) that have two nodes """
        node_set = set()
        valid_edges = []

        for edge in edges:
            nodes = edge.get_nodes() ## Returns 2 actual nodes or empty list

            if nodes:
                node_set.add(nodes[0])
                node_set.add(nodes[1])
                valid_edges.append(edge)

        return list(node_set), valid_edges


    def reset_am_array(self):
        """ Initialize empty matrix """

        self.am = []
        nodes_len = len(self.nodes)

        for i in range(nodes_len):
            self.am.append([])
            for j in range(nodes_len):
                self.am[i].append(0)
