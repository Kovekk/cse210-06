from constants import *

from game.scripting.action import Action
from game.casting.ball import Ball
from game.shared.point import Point
from game.casting.body import Body
from game.scripting.start_ball_action import StartBallAction
from game.services.keyboard_service import KeyboardService


class CollideBordersAction(Action):

    def __init__(self, physics_service):
        self._physics_service = physics_service
        self.player1_score = 0
        self.player2_score = 0
        self._timer = 0
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()

                
        if x < FIELD_LEFT:
            self.player2_score += 1
            cast.reset_actor_group(BALL_GROUP)
            ball = Ball((Body(position= Point(CENTER_X + 10, CENTER_Y), size= Point(10, 10))))
            cast.add_actor(BALL_GROUP, ball)
            script.add_action("input", StartBallAction(KeyboardService()))

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            self.player1_score += 1
            cast.reset_actor_group(BALL_GROUP)
            ball = Ball((Body(position= Point(CENTER_X + 10, CENTER_Y), size= Point(10, 10))))
            cast.add_actor(BALL_GROUP, ball)
            script.add_action("input", StartBallAction(KeyboardService()))

        if self._timer < 1:

            self._timer = 3

            if y < FIELD_TOP:
                ball.bounce_y()

            elif y >= (FIELD_BOTTOM - BALL_WIDTH):
                ball.bounce_y()
        elif self._timer > 0:
            self._timer += -1


            # stats = cast.get_first_actor(STATS_GROUP)
            # stats.lose_life()
            
            # if stats.get_lives() > 0:
            #     callback.on_next(TRY_AGAIN) 
            # else:
            #     callback.on_next(GAME_OVER)
            #     self._audio_service.play_sound(over_sound)

        banner = cast.get_first_actor("banners")
        banner.set_text(f"{self.player1_score} | {self.player2_score}")