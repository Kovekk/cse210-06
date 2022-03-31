from constants import *

class StartBallAction:

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

    def execute(self, cast, script, callback):
        if self._keyboard_service.is_key_pressed('enter'):
            self._activate_ball(cast)
        

    def _activate_ball(self, cast):
        ball = cast.get_first_actor(BALL_GROUP)
        ball.release()    