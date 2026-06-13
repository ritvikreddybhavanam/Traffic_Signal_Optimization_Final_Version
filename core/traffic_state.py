import random


class TrafficState:

    def __init__(self):

        self.queues = {
            "north": random.randint(10, 40),
            "south": random.randint(10, 40),
            "east": random.randint(10, 40),
            "west": random.randint(10, 40)
        }

        self.waiting_time = {
            lane: 0 for lane in self.queues
        }

        self.emergency_lane = None

        if random.random() < 0.2:
            self.emergency_lane = random.choice(
                ["north", "south", "east", "west"]
            )

    def get_state(self):
        return self.queues.copy()

    def get_total_vehicles(self):
        return sum(self.queues.values())

    def get_highest_density_lane(self):
        return max(self.queues, key=self.queues.get)

    def update_waiting(self):

        for lane in self.waiting_time:

            if self.queues[lane] > 0:
                self.waiting_time[lane] += 1

    def apply_green(self, lane):

        vehicles_passed = min(
            self.queues[lane],
            random.randint(5, 15)
        )

        self.queues[lane] -= vehicles_passed

        return vehicles_passed

    def add_new_traffic(self):

        for lane in self.queues:
            self.queues[lane] += random.randint(0, 5)

    def get_cost(self):

        return (
            sum(self.queues.values()) +
            sum(self.waiting_time.values())
        )

    def __str__(self):
        return str(self.queues)