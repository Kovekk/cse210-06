from constants import *

from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.ball import Ball
from game.casting.paddles import Paddle
from game.casting.body import Body

from game.scripting.script import Script
from game.scripting.action import Action
from game.scripting.control_actors_action_p1 import ControlActorsAction
from game.scripting.control_actors_action_p2 import ControlActorsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.control_menu_action import ControlMenuAction
from game.scripting.draw_menu_action import DrawMenuAction
from game.scripting.draw_paddle_action import DrawPaddleAction
from game.scripting.start_drawing_action import StartDrawingAction

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.point import Point

class SceneManager:

    def __init__(self):
        self._video_service = VideoService()


    def prepare_scene(self, scene, cast, script):
        if scene == "menu":
            self.reset_scene(cast, script)
            self._prepare_menu_screen(cast, script)
        if scene == "original_pong":
            self.reset_scene(cast, script)
            self._prepare_original_pong(cast, script)

    def _prepare_menu_screen(self, cast, script):
        keyboard_service = KeyboardService()

        banner = Actor()
        banner.set_text("Press 1 for original pong")
        cast.add_actor("banners", banner)

        script.add_action("input", ControlMenuAction(keyboard_service))
        script.add_action("update", Action())
        script.add_action("output", DrawMenuAction(self._video_service))


    def _prepare_original_pong(self, cast, script):

        left_paddle = Paddle(Body(position= Point(25, CENTER_Y - (75 / 2)), size= Point(10, 75)))
        cast.add_actor(PADDLE_GROUP, left_paddle)

        right_paddle = Paddle(Body(position= Point(MAX_X - 35, CENTER_Y - (75 / 2)), size = Point(10, 75)))
        cast.add_actor(PADDLE_GROUP, right_paddle)

        ball = Ball(Body(position = Point(CENTER_X, CENTER_Y), size = Point(10, 10)))
        cast.add_actor(BALL_GROUP, ball)

        script.add_action("input", Action())
        script.add_action("update", Action())
        script.add_action("output", DrawPaddleAction(self._video_service))

        


    def reset_scene(self, cast, script):
        cast.remove_all_actors()
        script.remove_all_actions()
        cast_list = cast.get_all_actors()
        print(cast_list)