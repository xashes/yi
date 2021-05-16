import arcade as ac
from typing import List
from yi.data import gua64_data


class YaoSprite(ac.SpriteSolidColor):
    def __init__(self, width: int, height: int, color, value: int, center_x, center_y):
        super().__init__(width, height, color)
        self.value = value
        self.center_x = center_x
        self.center_y = center_y

        self.setup()

    def setup(self):
        self.sprite_list = ac.SpriteList()
        gap_width = int(self.height * 1 / 3)
        height = int(self.height - gap_width)
        color = ac.color.WHITE
        x = self.center_x
        y = self.bottom + int(height * 1 / 2)
        position = (x, y)

        gap_color = ac.color.AMAZON
        gap_sprite = ac.SpriteSolidColor(gap_width, height, gap_color)
        gap_sprite.position = position

        sprite = ac.SpriteSolidColor(self.width, height, color)
        sprite.position = position

        self.sprite_list.append(sprite)
        if self.value == 0:
            self.sprite_list.append(gap_sprite)

        # 阴爻也可用左中右三个长方形排成，左右两个同形，中间透明

    def draw(self):
        self.sprite_list.draw()


class GuaSprite(ac.SpriteSolidColor):
    def __init__(
        self,
        width: int,
        yao_height: int,
        color,
        values: List[int],
        center_x: float,
        center_y: float,
    ):
        height = yao_height * len(values)
        super().__init__(width, height, color)
        self.alpha = 0
        self.yao_height = yao_height
        self.center_x = center_x
        self.center_y = center_y

        self.values = values

        self.setup()

    def setup(self):
        self.yao_list = ac.SpriteList()
        x = self.center_x
        for i, v in enumerate(self.values):
            y = self.bottom + i * self.yao_height + 1 / 2 * self.yao_height
            yao = YaoSprite(
                self.width, self.yao_height, self.color, value=v, center_x=x, center_y=y
            )
            self.yao_list.append(yao)

    def value(self):
        binary = "".join([str(i) for i in self.values])
        return int(binary, 2)

    def set_values(self, values):
        self.values = values
        self.setup()

    def change_value(self, i, value):
        self.values[i] = value
        self.setup()

    def get_data(self) -> dict:
        k = self.value()
        return gua64_data[k]

    def draw(self):
        for yao in self.yao_list:
            yao.draw()
