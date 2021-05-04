#!/usr/bin/env python3

import pyglet


class Yao:
    def __init__(self, color, gap_color, width, height, x, y, batch=None) -> None:
        yao_image = pyglet.image.SolidColorImagePattern(color).create_image(
            width, height
        )
        yao_image.anchor_x = yao_image.width // 2
        yao_image.anchor_y = yao_image.height // 2

        gap_width = width // 5
        gap_image = pyglet.image.SolidColorImagePattern(gap_color).create_image(
            gap_width, height
        )
        gap_image.anchor_x = gap_image.width // 2
        gap_image.anchor_y = gap_image.height // 2

        self.yang_sprite = pyglet.sprite.Sprite(yao_image, x=x, y=y, batch=batch)
