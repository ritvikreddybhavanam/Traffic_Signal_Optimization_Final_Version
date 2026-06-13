from co3_csp.mrv import MRV
from co3_csp.lcv import LCV


class BacktrackingSolver:

    def __init__(self, domains):

        self.domains = domains

    def is_valid(self, assignment):

        total_time = sum(assignment.values())

        if total_time > 120:
            return False

        for lane, value in assignment.items():

            if value < 10:
                return False

            if value > 60:
                return False

        return True

    def solve(self):

        lane = MRV.select_variable(self.domains)

        assignment = {}

        remaining = 120

        total_vehicles = sum(
            len(v)
            for v in self.domains.values()
        )

        for lane, domain in self.domains.items():

            traffic = len(domain)

            if total_vehicles == 0:

                green_time = 10

            else:

                green_time = max(
                    10,
                    int(
                        (traffic / total_vehicles)
                        * 120
                    )
                )

            assignment[lane] = green_time

        total = sum(assignment.values())

        if total > 120:

            scale = 120 / total

            for lane in assignment:

                assignment[lane] = max(
                    10,
                    int(
                        assignment[lane] * scale
                    )
                )

        return assignment