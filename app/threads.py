import datetime
import time
import threading


class ClockThread(threading.Thread):
    DAY_NAMES = [
        "poniedziałek",
        "wtorek",
        "środa",
        "czwartek",
        "piątek",
        "sobota",
        "niedziela"]

    def __init__(self, callback, interval=1/10):
        super().__init__(daemon=True)
        self._callback = callback
        self._interval = interval
        self._running = False
        self._last_time = None

    def run(self):
        self._running = True
        self._last_time = datetime.datetime.today()
        self._callback(self.time_to_str(self._last_time))
        while self._running:
            now = datetime.datetime.now()
            if now.second != self._last_time.second:
                self._callback(self.time_to_str(now))
            time.sleep(self._interval)

    def stop(self):
        self._running = False

    @classmethod
    def time_to_str(cls, time):
        return "{}, ".format(cls.DAY_NAMES[time.weekday()]) \
               + time.strftime("%Y-%m-%d %H:%M:%S")
