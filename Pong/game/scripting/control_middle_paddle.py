from constants import *
from game.scripting.action import Action


class ControlMiddlePaddle(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        paddles = cast.get_actors(PADDLE_GROUP)
        paddle_middle = paddles[2]

        if self._keyboard_service.is_key_down("up"): 
            paddle_middle.swing_up()
        elif self._keyboard_service.is_key_down("down"): 
            paddle_middle.swing_down() 
        else:
            paddle_middle.stop_moving()