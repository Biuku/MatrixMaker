""" March 18, 2021 """

import pygame
from settings import Settings

class Helpers:

    def __init__(self, win):
        self.set = Settings()
        self.win = win
        self.node_names = self.get_node_names_stack()
        self.set.db_timer = self.set.db_clock.tick()


    def get_hover_objects(self, objects):
        hovering = []
        for object in objects:
            if object.get_hovering():
                hovering.append(object)
        return hovering


    def get_moving_object(self, objects):
        for object in objects:
            if object.get_moving():
                return object

        return False


    def check_dbclick(self):
        self.db_timer = self.set.db_clock.tick()

        if 75 < self.db_timer < self.set.db_max_time:
            return True
        else:
            #self.set.db_timer = self.set.db_clock.tick() # Prevent triple clicks registering as double clicks
            return False


    def print_instructions(self):

        colour = self.set.instructions_font_colour
        x = self.set.win_w * 0.82 ## lower number --> leftward
        y = self.set.win_h * 0.04 ## lower number --> upward

        texts = [
            "New node: double-click",
            "New edge: double-click a node",
            "Show adjacency matrix: M",
            "Re-alphabeticalize nodes: A",
            "Quit: Q",
            ]

        for text in texts:
            printr = self.set.med_font.render(text, True, colour)
            self.win.blit( printr, (x, y) )
            y += 20


    def get_node_name(self):
        return self.node_names.pop(0)


    def get_node_names_stack(self):
        alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        stack = []

        for i in range(-1, len(alpha)):
            for j in range(len(alpha)):

                if i < 0:
                    stack.append(alpha[j])
                else:
                    stack.append(alpha[i] + alpha[j])

        return stack

    def reset_node_names_stack(self):
        self.node_names = self.get_node_names_stack()
