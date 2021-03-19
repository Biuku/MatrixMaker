""" March 18, 2021 """

import pygame
from settings import Settings

class Helpers:

    def __init__(self, win):
        self.set = Settings()
        self.win = win

    def check_hovering(self, objects):
        for object in objects:
            if object.get_hovering():
                return True

        return False

    def get_hovering(self, objects):
        hovering = []
        for object in objects:
            if object.get_hovering():
                hovering.append(object)
        return hovering

    def get_moving(self, objects):
        for object in objects:
            if object.get_moving():
                return object

        return False

    def check_dbclick(self):
        self.set.db_timer = self.set.db_clock.tick()

        if 30 < self.set.db_timer < self.set.db_max_time:
            return True

        return False


    def print_instructions(self):

        # Find a spot at top-right
        x = self.set.win_w * 0.82 ## lower number --> leftward
        y = self.set.win_h * 0.04 ## lower number --> upward

        texts = [
            "New node: double-click",
            "New edge: double-click a node",

            "Quit: Q",
            ]

        for text in texts:
            printr = self.set.med_font.render(text, True, self.set.grey)
            self.win.blit( printr, (x, y) )
            y += 20
