import pyautogui as pgui
import time
import random
import threading

class MouseJiggler(threading.Thread):
    def __init__(self, seconds: float = float('inf')):
        super(MouseJiggler, self).__init__()
        self.seconds = seconds
        self.stopped = False

    def get_random_coords(self):
        screen_width, screen_height = pgui.size()
        return (random.randint(100, screen_width - 100), random.randint(100, screen_height - 100))
    
    def run(self):
        startTime = time.time()

        while time.time() - startTime < self.seconds and not self.stopped:
            pgui.moveTo(*self.get_random_coords(), 1, _pause=False)
    
    def stop(self):
        self.stopped = True
