from constants import *
from game.scripting.action import Action
from game.shared.point import Point
import random

class MoveBallAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):

        ball = cast.get_actors(BALL_GROUP)

        body = ball.get_body()

        x_velocity = body.get_velocity()
        y_velocity = body.get_velocity()
        position = body.get_position()
        y = position.get_y()
        x = position.get_x()

        y_position = position.add(y_velocity)
        x_position = position.add(x_velocity)

        if y < 0:
            ball.bounce_y()
        elif y < (MAX_Y - BALL_HEIGHT):
            ball.bounce_y()