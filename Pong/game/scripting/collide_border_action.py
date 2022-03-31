from constants import *

from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service):
        self._physics_service = physics_service 
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()

                
        if x < FIELD_LEFT:
            callback.change_scene("menu", cast, script)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            callback.change_scene("menu", cast, script)

        if y < FIELD_TOP:
            ball.bounce_y()

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            ball.bounce_y()
            # stats = cast.get_first_actor(STATS_GROUP)
            # stats.lose_life()
            
            # if stats.get_lives() > 0:
            #     callback.on_next(TRY_AGAIN) 
            # else:
            #     callback.on_next(GAME_OVER)
            #     self._audio_service.play_sound(over_sound)