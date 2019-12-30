def win_spots = [
  [0,1,2],
  [3,4,5],
  [6,7,8],

]

class GameState:
  def __init__(self, board_state: str):
    self.board_state = board_state

  def is_player_one_turn (self) -> bool:
    x_count = self.board_state.count('x')
    o_count = self.board_state.count('o')
    move_count = x_count + o_count

    return move_count % 2 == 0

  def is_player_two_turn (self) -> bool:
    return self.is_player_one_turn() == False

