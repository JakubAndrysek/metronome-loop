from time import time

# current version number
__version__ = "0.1.0"

class metronome:
    def __init__(self, interval_ms, callback=None):
        self.interval_ms = interval_ms / 1000
        self.callback = callback
        self.time_last = time()

    def loop(self):
        time_now = time()
        if time_now >= self.time_last + self.interval_ms:
            if self.callback:
                self.callback()
                self.time_last = time_now
                return True
            else:
                self.time_last = time_now
                return True

        else:
            return False

    def set_interval_ms(self, interval_ms):
        self.interval_ms = interval_ms / 1000

    def set_interval_s(self, set_interval):
        self.interval_ms = set_interval

    def get_interval_ms(self):
        return self.interval_ms

    def get_interval_s(self):
        return self.interval_ms * 1000
