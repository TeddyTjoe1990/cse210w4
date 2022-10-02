from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
  """
  An item of cultural or historical interest.
  The responsibility of an Artifact is to provide a message about itself.
  Attributes:
      _message (string): A short description about the artifact
  """
  def __init__(self):
    super().__init__()
    self.message = ""
  
  def get_message(self):
    """Get the artifact's message"""
    return self._message
  
  def set_message(self, message):
    """Updates the message to the given one"""
    self._message = message
  