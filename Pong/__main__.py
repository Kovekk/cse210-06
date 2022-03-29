from game.director.director import Director
from game.services.video_service import VideoService
from game.services.keyboard_service import KeyboardService
from game.casting.cast import Cast
from game.scripting.script import Script
from game.casting.paddles import Paddle
from game.casting.ball import Ball
from game.scripting.control_actors_action_p1 import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from constants import *

def main():
    # create the cast
    cast = Cast()
    cast.add_actor("paddles", Paddle(PADDLE_GROUP))
    cast.add_actor("balls", Ball(BALL_GROUP))
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()