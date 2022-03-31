from constants import *
from game.scripting.action import Action


class DrawPaddleAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        paddles = cast.get_actors(PADDLE_GROUP)
        for paddle in paddles:

            body = paddle.get_body()

            rectangle = body.get_rectangle()
            
            self._video_service.draw_rectangle(rectangle, PURPLE)
        
            
        # animation = racket.get_animation()
        # image = animation.next_image()
        # position = body.get_position()
        # self._video_service.draw_image(image, position)