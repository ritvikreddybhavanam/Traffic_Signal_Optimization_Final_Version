from co3_csp.backtracking import BacktrackingSolver


class TrafficCSP:

    def __init__(self, state):

        self.state = state

    def build_domains(self):

        domains = {}

        for lane, vehicles in self.state.queues.items():

            domains[lane] = list(
                range(vehicles)
            )

        return domains

    def schedule(self):

        domains = self.build_domains()

        solver = BacktrackingSolver(
            domains
        )

        assignment = solver.solve()

        best_lane = max(
            assignment,
            key=assignment.get
        )

        return best_lane

    def get_full_schedule(self):

        domains = self.build_domains()

        solver = BacktrackingSolver(
            domains
        )

        return solver.solve()