"""
The MIT License (MIT)
Copyright (c) 2016 Jeppe Pihl
"""
import pygame


class Light(object):

    def __init__(self):
        pygame.init()
        info = pygame.display.Info()
        size = (info.current_w, info.current_h)

        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

        self.screen.fill((0, 0, 0))

    def run(self):
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT or \
               event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                break
            pygame.display.flip()
        pygame.quit()

    def toggle(self):
        on = self.screen.get_at((0, 0)).r == 255
        if on:
            color = (0, 0, 0)
        else:
            color = (255, 255, 255)
        self.screen.fill(color)
