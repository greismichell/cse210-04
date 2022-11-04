from game.casting.item import Item
import random

class Rock(Item):
  def __init__(self, cell_size, font_size):
      super().__init__('rocks', '©', (random.randint(1, 6) * -1), cell_size, font_size)