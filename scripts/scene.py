# Scene of the game.
# Represents a distinct view that has different game rules and inputs

class Scene:
  def __init__(self, game_state):
    self.game_state = game_state

  def get_game_state(self):
    return self.game_state

class MainMenuScene(Scene):
  def test_scene(self):
    print("Scene is working!")


