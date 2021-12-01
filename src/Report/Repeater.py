from threading import Timer
from typing import Any


class Repeater(object):
    timer: Timer = None
    interval: int
    function: Any
    args: tuple
    kwargs: dict
    is_running: bool = False

    def repeat(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.run()

    def run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self.timer = Timer(self.interval, self.run)
            self.timer.start()
            self.is_running = True
