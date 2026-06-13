from co5_uncertainty.probabilities import ProbabilityTables


class BayesianNetwork:

    def __init__(self):

        self.probabilities = ProbabilityTables()

    def congestion_probability(
            self,
            rush_hour,
            rain,
            accident):

        key = (
            rush_hour,
            rain,
            accident
        )

        return (
            self.probabilities
            .CONGESTION_TABLE[key]
        )

    def classify_congestion(self, probability):

        if probability >= 0.80:
            return "HIGH"

        elif probability >= 0.50:
            return "MEDIUM"

        else:
            return "LOW"