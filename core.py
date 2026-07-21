import time

class PerformanceTracker:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        if self.start_time is None:
            raise ValueError("Timer has not been started.")
        elapsed_time = time.perf_counter() - self.start_time
        self.start_time = None
        return elapsed_time

def optimized_function(data):
    processed_data = [d * 2 for d in data]
    return processed_data

def main():
    tracker = PerformanceTracker()
    data = range(1000000)
    tracker.start()
    result = optimized_function(data)
    elapsed = tracker.stop()
    print(f'Processed {len(result)} items in {elapsed:.4f} seconds.')  

if __name__ == '__main__':
    main()