#!/usr/bin/env python3

import arcade as ac
from yi.gua import GuaSprite

WIDTH = 1000
HEIGHT = 800
TITLE = "变卦"
YAO_WIDTH = 200
YAO_HEIGHT = 40
DEFAULT_GUA = [0, 0, 0, 0, 0, 0]
BG_COLOR = ac.color.AMAZON


class MainWindow(ac.Window):
    def __init__(self, width: int, height: int, title: str):
        super().__init__(width=width, height=height, title=title, resizable=True)

    def setup(self):
        ac.set_background_color(BG_COLOR)
        self.gua_list = ac.SpriteList()

        self.gua = GuaSprite(
            YAO_WIDTH,
            YAO_HEIGHT,
            self.background_color,
            values=DEFAULT_GUA,
            center_x=self.width / 2,
            center_y=self.height / 2,
        )
        self.gua_list.append(self.gua)

    def on_draw(self):
        ac.start_render()
        self.gua.draw()


def main():
    window = MainWindow(WIDTH, HEIGHT, TITLE)
    window.setup()
    ac.run()


if __name__ == "__main__":
    main()
