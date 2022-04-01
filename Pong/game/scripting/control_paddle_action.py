from constants import *
from game.scripting.action import Action


class ControlPaddleAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        paddles = cast.get_actors(PADDLE_GROUP)
        paddle_left = paddles[0]
        paddle_right = paddles[1]
        
        if self._keyboard_service.is_key_down("w"): 
            paddle_left.swing_up()
        elif self._keyboard_service.is_key_down("s"): 
            paddle_left.swing_down() 
        else:
            paddle_left.stop_moving()
        if self._keyboard_service.is_key_down("i"):
            paddle_right.swing_up()
        elif self._keyboard_service.is_key_down("k"):
            paddle_right.swing_down()
        else: 
            paddle_right.stop_moving()        