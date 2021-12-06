from threading import Timer


class Repeater:
    def __init__(self, interval, function, *args, **kwargs) -> None:
        self.kwargs = kwargs
        self.args = args
        self.function = function
        self.interval = interval
        self.is_running = False
        self.timer = None

    def repeat(self) -> None:
        self.run()

    def run(self) -> None:
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self) -> None:
        if not self.is_running:
            self.timer = Timer(self.interval, self.run)
            self.timer.start()
            self.is_running = True
