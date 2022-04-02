from game.scripting.action import Action

class ControlMenuAction(Action):
    """stuff"""

    def __init__(self, keyboard_service):
        """Constructs a new ControlMenuAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service

    def execute(self, cast, script, callback):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('1'):
            callback.change_scene("instructions", cast, script)
        
        if self._keyboard_service.is_key_down('2'):
            callback.change_scene("original_pong", cast, script)
        
        if self._keyboard_service.is_key_down('3'):
            callback.change_scene("three_player_pong", cast, script)

        if self._keyboard_service.is_key_down('4'):
            pass

    def _start_original_pong(self, cast, script):
        pass