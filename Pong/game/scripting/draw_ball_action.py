from constants import *
from game.scripting.action import Action


class DrawBallAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
<<<<<<< HEAD
        body = ball.get_body()

        rectangle = body.get_rectangle()
        self._video_service.draw_rectangle(rectangle, WHITE)
            
        # image = ball.get_image()
        # position = body.get_position()
        # self._video_service.draw_image(image, position)
=======
        self._video_service.clear_buffer()
        body = ball.get_body()
        rectangle = body.get_rectangle()         
        self._video_service.draw_rectangle(rectangle, PURPLE)
        self._video_service.flush_buffer()
>>>>>>> fa41fa3e664b9af7f9faa12c884d1e2fd8a5236c
