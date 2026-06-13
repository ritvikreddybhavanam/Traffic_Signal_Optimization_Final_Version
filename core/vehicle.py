class Vehicle:
    def __init__(self, vehicle_id, lane):
        self.vehicle_id = vehicle_id
        self.lane = lane
        self.waiting_time = 0

    def increment_wait(self):
        self.waiting_time += 1

    def __str__(self):
        return f"Vehicle({self.vehicle_id}, Lane={self.lane}, Wait={self.waiting_time})"