from constants import *
from game.scripting.action import Action


class CollidePaddleAction(Action):

    def __init__(self, physics_service):
        self._physics_service = physics_service
        
    def execute(self, cast, script, callback):
        
        ball = cast.get_first_actor(BALL_GROUP)
        paddles = cast.get_actors(PADDLE_GROUP)
        
        ball_body = ball.get_body()
        for paddle in paddles:
            paddle_body = paddle.get_body()

            if self._physics_service.has_collided(ball_body, paddle_body):
                ball.bounce_x() 