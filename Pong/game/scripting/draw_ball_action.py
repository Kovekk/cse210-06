from constants import *
from game.scripting.action import Action


class DrawBallAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        self._video_service.clear_buffer()
        body = ball.get_body()
        rectangle = body.get_rectangle()         
        self._video_service.draw_rectangle(rectangle, PURPLE)
        self._video_service.flush_buffer()