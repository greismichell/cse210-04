from game.casting.item import Item
import random

class Gem(Item):
  def __init__(self, cell_size, font_size):
      super().__init__('gems', '<*>',random.randint(1, 6), cell_size, font_size)
