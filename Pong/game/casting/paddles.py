from game.casting.actor import Actor
from constants import *
from game.shared.point import Point

class Paddle():

    def __init__(self, body):

        self._body = body

    def get_body(self):
        
        return self._body
        
    def move_next(self):

        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self.set_position(new_position)

    def swing_up(self):

        velocity = Point(0, -PADDLE_VELOCITY)
        self._body.set_velocity(velocity)

    def swing_down(self):

        velocity = Point(0, PADDLE_VELOCITY)
        self._body.set_velocity(velocity)

    def swing_left(self):

        velocity = Point(0, PADDLE_VELOCITY)
        self._body.set_velocity(velocity)

    def swing_right(self):

        velocity = Point(0, PADDLE_VELOCITY)
        self._body.set_velocity(velocity)

    def stop_moving(self):

        velocity = Point(0, 0)
        self._body.set_velocity(velocity)