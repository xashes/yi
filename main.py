#!/usr/bin/env python3

import arcade as ac

mainwindow_width = 1000
mainwindow_height = 800
app_title = "变卦"


class MainWindow(ac.Window):
    def __init__(self, width: int, height: int, title: str):
        super().__init__(width=width, height=height, title=title, resizable=True)

    def setup(self):
        ac.set_background_color(ac.color.AMAZON)

    def on_resize(self, width: float, height: float):
        return super().on_resize(width, height)

    def on_draw(self):
        ac.start_render()


def main():
    window = MainWindow(mainwindow_width, mainwindow_height, app_title)
    window.setup()
    ac.run()


if __name__ == "__main__":
    main()
