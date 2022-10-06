import random

from greed.shared.color import Color
from greed.shared.point import Point
from greed.shared.constant import Constants

Constant = Constants()

class Actor:
  """A visible, moveable thing that participates in the game
  The responsibility of Actor is to keep track of its appearance, position and velocity in 2d space.

  Attributes:
    _text (string): The text to display
    _font_size (int): The font size to use.
    _color (Color): The color of the text.
    _position (Point): The screen coordinates.
    _velocity (Point): The speed and direction.
  """
  def __init__(self):
    """Construct a new Actor"""
    self._text = ""
    self._font_size = 15
    self._color = Color(255, 255, 255)
    self._position = Point(0, 0)
    self._velocity = Point(0, 0)
    
  def get_color(self):
    """Get the actor's color as a tuple of three ints (r, g, b)
    Returns:
      Color: The actor's text color
    """
    return self._color
  
  def get_font_size(self):
    """Get the actor's font size
    Returns:
      Point: The actor's font size
    """
    return self._font_size
  
  def get_position(self):
    """Get the actor's position in 2d space
    Returns:
      Point: Thea actor's position in 2d space
    """
    return self._position
  
  def get_text(self):
    """Get the actor's textual representation
    Returns:
      string: The actor's textual representation
    """
    return self._text
  
  def get_velocity(self):
    """Gets the actor's speed and direction.
    Returns:
      Point: The actor's speed and direction.
    """
    return self._velocity
  
  def move_text(self, max_x, max_y):
    """Moves the actor to its next position according to the velocity.
    Will wrap the position from one side of the screen to the other when it reaches the given maximum x and y points
    Args:
      max_x (int): The maximum x point
      max_y (int): The maximum y point
    """
    x = (self._position.get_x() + self._velocity.get_x()) % max_x
    y = (self._position.get_y() + self._velocity.get_y()) % max_y
    self._position = Point(x, y)
    
  def set_color(self, color):
    """Updates the color to the given one
    Args:
      color (color): Given color
    """
    self._color = color
  
  def set_position(self, position):
    """Updates the position to the given one
    Args:
      position (Point): Given position
    """
    self._position = position
    
  def set_font_size(self, font_size):
    """Updates the font size to the given one
    Args:
      font_size (int): Given font size
    """
    self._font_size = font_size
    
  def set_text(self, text):
    """Updates the text to the fiven one
    Args:
      text (string): Given value
    """
    self._text = text
    
  def set_velocity(self, velocity):
    """Updates the veocity to the given one
    Args:
      velocity (Point): Given velocity
    """
    self._velocity = velocity
    
  def create_random_values(self):
    """Creates random values for color and position, and sets font size to standard
    """
    x = random.randint(1, Constants.COLS - 1)
    y = random.randint(1, Constants.ROWS - 1)
    position = Point( x, y)
    position = position.scale(Constants.CELL_SIZE)
    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = Color(r, g, b)
    
    self.set_font_size(Constants.FONT_SIZE)
    self.set_color(color)
    self.set_position(position)