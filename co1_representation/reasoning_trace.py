from datetime import datetime


class ReasoningTrace:

    def __init__(self):

        self.trace = []

    def add(self, message):

        timestamp = datetime.now().strftime("%H:%M:%S")

        self.trace.append(
            f"[{timestamp}] {message}"
        )

    def display(self):

        print("\n================================================")
        print("CO1 : REASONING TRACE")
        print("================================================")

        if not self.trace:
            print("No reasoning available.")
            return

        for step, msg in enumerate(self.trace, start=1):

            print(f"{step}. {msg}")

        print("================================================")

    def clear(self):

        self.trace.clear()

    def export(self, filename="reasoning_trace.txt"):

        with open(filename, "w", encoding="utf-8") as file:

            for line in self.trace:
                file.write(line + "\n")

    def generate_state_reasoning(self, state):

        highest_lane = max(
            state.queues,
            key=state.queues.get
        )

        highest_count = state.queues[highest_lane]

        self.add(
            f"Highest density lane detected: "
            f"{highest_lane.upper()} "
            f"({highest_count} vehicles)"
        )

        total = sum(state.queues.values())

        self.add(
            f"Total vehicles in intersection: {total}"
        )

        if state.emergency_lane:

            self.add(
                f"Emergency vehicle detected in "
                f"{state.emergency_lane.upper()} lane"
            )

        else:

            self.add(
                "No emergency vehicle detected"
            )

        cost = (
            sum(state.queues.values()) +
            sum(state.waiting_time.values())
        )

        self.add(
            f"Current traffic cost = {cost}"
        )