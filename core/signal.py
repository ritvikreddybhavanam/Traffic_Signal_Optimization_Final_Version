class TrafficSignal:

    RED = "RED"
    GREEN = "GREEN"

    def __init__(self):
        self.current_lane = None
        self.green_duration = 0

    def set_green(self, lane, duration):
        self.current_lane = lane
        self.green_duration = duration

    def get_status(self):
        return {
            "green_lane": self.current_lane,
            "duration": self.green_duration
        }

    def __str__(self):
        return f"GREEN -> {self.current_lane} ({self.green_duration}s)"