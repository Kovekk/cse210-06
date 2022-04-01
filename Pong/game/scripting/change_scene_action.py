from constants import *
from game.scripting.action import Action


class ChangeSceneAction(Action):

    def __init__(self, keyboard_service, scene):
        self._keyboard_service = keyboard_service
        self._next_scene = scene
        
    def execute(self, cast, script, callback):
        if self._keyboard_service.is_key_pressed("backspace"):
            callback.change_scene(self._next_scene, cast, script)