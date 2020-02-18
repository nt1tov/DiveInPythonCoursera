import time

class timer:
    def __init__(self):
        self.start_time = time.time()

    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        print(f"Runtime: {self.runtime()}")

    def runtime(self):
        return time.time() - self.start_time

    