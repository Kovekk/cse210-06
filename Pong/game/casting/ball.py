import random
from game.casting.actor import Actor
from game.shared.point import Point
from constants import *


class Ball(Actor):

    def __init__(self, body):

        super().__init__()
        self._body = body

    def bounce_x(self):

        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x() * rn * -1
        vy = velocity.get_y()
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def bounce_y(self):

        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x()
        vy = velocity.get_y() * rn * -1
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def get_body(self):

        return self._body

    def release(self):

        rn = random.uniform(0.9, 1.1)
        vx = random.choice([-BALL_VELOCITY * rn, BALL_VELOCITY * rn])
        vy = -BALL_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)
    