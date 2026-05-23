import time


class CodeTimer:
    """
    A simple timer class for measuring how long part of a program takes to run.
    """

    def __init__(self, name="Code segment"):
        self.name = name
        self._start_time_ns = None
        self.last_elapsed_microseconds = None

    def start(self):
        """
        Start the timer.

        If the timer is already running, stop the previous timing first,
        then start a new one.
        """
        if self._start_time_ns is not None:
            print("Warning: start() was called while the timer was already running.")
            print("Stopping the previous timing before starting a new one.")
            self.stop()

        self._start_time_ns = time.perf_counter_ns()
        self.last_elapsed_microseconds = None

    def stop(self):
        """
        Stop the timer, print the elapsed time, reset the timer,
        and return the elapsed time in microseconds.
        """
        if self._start_time_ns is None:
            print("Warning: stop() was called, but the timer was not running.")
            return None

        end_time_ns = time.perf_counter_ns()
        elapsed_ns = end_time_ns - self._start_time_ns
        elapsed_microseconds = elapsed_ns / 1000

        self.last_elapsed_microseconds = elapsed_microseconds

        print(f"{self.name} took {elapsed_microseconds:.2f} microseconds.")

        self._start_time_ns = None

        return elapsed_microseconds

    def is_running(self):
        return self._start_time_ns is not None
