class UtilityAgent:

    def __init__(self, state):
        self.state = state

    def calculate_utility(self, lane):

        queue = self.state.queues[lane]
        wait = self.state.waiting_time[lane]

        utility = (
            (queue * 2)
            - wait
        )

        if self.state.emergency_lane == lane:
            utility += 100

        return utility

    def choose_action(self):

        utilities = {}

        for lane in self.state.queues:

            utilities[lane] = self.calculate_utility(
                lane
            )

        best_lane = max(
            utilities,
            key=utilities.get
        )

        return best_lane, utilities