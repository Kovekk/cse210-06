class Actor:
    
    def __init__(self, debug = False):
        
        self._debug = debug
        
    def is_debug(self):
        
        return self._debug