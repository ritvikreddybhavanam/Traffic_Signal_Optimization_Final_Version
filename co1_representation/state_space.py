class StateSpace:

    def __init__(self, traffic_state):

        self.state = traffic_state

        self.actions = [
            "GREEN_NORTH",
            "GREEN_SOUTH",
            "GREEN_EAST",
            "GREEN_WEST"
        ]

    def get_state(self):

        return self.state.get_state()

    def get_actions(self):

        return self.actions

    def get_goal(self):

        return (
            "Minimize Waiting Time | "
            "Minimize Queue Length | "
            "Maximize Throughput"
        )

    def calculate_cost(self):

        queues = self.state.queues
        waits = self.state.waiting_time

        queue_cost = sum(queues.values())
        wait_cost = sum(waits.values())

        return queue_cost + wait_cost

    def get_highest_density_lane(self):

        return max(
            self.state.queues,
            key=self.state.queues.get
        )

    def is_congested(self):

        return self.calculate_cost() > 80

    def display(self):

        print("\n================================================")
        print("CO1 : STATE SPACE REPRESENTATION")
        print("================================================")

        print("\nCurrent State")

        for lane, count in self.state.queues.items():
            print(f"{lane.upper():<10} : {count}")

        print("\nPossible Actions")

        for action in self.actions:
            print(action)

        print("\nGoal")

        print(self.get_goal())

        print("\nCost")

        print(self.calculate_cost())

        print("================================================")