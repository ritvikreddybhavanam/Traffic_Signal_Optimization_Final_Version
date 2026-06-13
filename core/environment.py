from core.traffic_state import TrafficState


class TrafficEnvironment:

    def __init__(self):
        self.state = TrafficState()

    def get_state(self):
        return self.state

    def next_step(self):

        self.state.add_new_traffic()
        self.state.update_waiting()

        return self.state

    def reset(self):

        self.state = TrafficState()