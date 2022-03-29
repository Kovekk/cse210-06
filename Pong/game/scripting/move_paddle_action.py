from constants import *
from game.shared.point import Point
from game.scripting.action import Action


class MovePaddleAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        paddles = cast.get_actors(PADDLE_GROUP)
        for paddle in paddles:

            body = paddle.get_body()
            velocity = body.get_velocity()
            position = body.get_position()
            y = position.get_y()
            
            position = position.add(velocity)

            if y < 0:
                position = Point(position.get_x(), 0)
            elif y > (MAX_Y - PADDLE_HEIGHT):
                position = Point(position.get_x(), MAX_Y - PADDLE_HEIGHT)
            
            body.set_position(position)
        