import pygame


def fit(min_value, max_value, value):
    if value < min_value:
        return min_value

    if value > max_value:
        return max_value

    return value


class AudioBar:

    def __init__(self, x, y, freq, color, width=50, min_height=10, max_height=100, min_decibel=-80, max_decibel=0):
        self.x, self.y, self.freq = x, y, freq
        self.color = color
        self.width, self.min_height, self.max_height = width, min_height, max_height
        self.height = min_height
        self.min_decibel, self.max_decibel = min_decibel, max_decibel
        self.__decibel_height_ratio = (self.max_height - self.min_height) / (self.max_decibel - self.min_decibel)

    def update(self, dt, decibel):
        desired_height = decibel * self.__decibel_height_ratio + self.max_height
        speed = (desired_height - self.height) * 10
        self.height += speed * dt
        self.height = fit(self.min_height, self.max_height, self.height)
        color_value = int(self.height * 255 / self.max_height)
        self.color = (color_value, color_value, color_value)

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y + self.max_height - self.height, self.width, self.height))
