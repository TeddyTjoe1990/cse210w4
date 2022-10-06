from greed.casting.actor import Actor

class Gem(Actor):
  """A small individual actor intended to raise the score of the player upon collision.
  Attributes:
    Actor (super): Actor class
  """
  def __init__(self):
    super().__init__()
    super().set_text("*")