from game.casting.actor import Actor
from game.shared.color import Color
from game.shared.point import Point
import random

COLS = 60
ROWS = 40

class Item(Actor):
  def __init__(self, group, text, value, cell_size, font_size):
      super().__init__()
      
      self._group = group
      self._value = value
      r = random.randint(0, 255)
      g = random.randint(0, 255)
      b = random.randint(0, 255)
      self.set_color(Color(r, g, b))

      x = random.randint(1, COLS)
      y = random.randint(1, ROWS)

      self.set_position(Point(x, y).scale(cell_size))
      self.set_text(text)
      self.set_font_size(font_size)
  
  def get_value(self):
    """gets the item value
    
    Returns: 
    int: the value"""
    
    return self._value

  def get_group(self):
    """Gets the group for the item
    
    Returns: 
    str: the group"""
    return self._group

