from constants import *
from game.scripting.action import Action


class DrawRacketAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        paddle = cast.get_first_actor(PADDLE_GROUP)
        body = paddle.get_body()

        rectangle = body.get_rectangle()
        self._video_service.clear_buffer()
        self._video_service.draw_rectangle(rectangle, PURPLE)
        self._video_service.flush_buffer()
            
        # animation = racket.get_animation()
        # image = animation.next_image()
        # position = body.get_position()
        # self._video_service.draw_image(image, position)