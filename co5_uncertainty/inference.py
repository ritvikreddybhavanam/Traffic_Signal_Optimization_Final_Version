from co5_uncertainty.bayesian_network import (
    BayesianNetwork
)


class TrafficInference:

    def __init__(self):

        self.network = BayesianNetwork()

    def predict(
            self,
            rush_hour,
            rain,
            accident):

        probability = (
            self.network
            .congestion_probability(
                rush_hour,
                rain,
                accident
            )
        )

        level = (
            self.network
            .classify_congestion(
                probability
            )
        )

        return {
            "probability": probability,
            "level": level
        }

    def print_prediction(
            self,
            rush_hour,
            rain,
            accident):

        result = self.predict(
            rush_hour,
            rain,
            accident
        )

        print("\n===================================")
        print("CO5 BAYESIAN INFERENCE")
        print("===================================")

        print("\nEvidence")

        print(
            f"Rush Hour : "
            f"{rush_hour}"
        )

        print(
            f"Rain      : "
            f"{rain}"
        )

        print(
            f"Accident  : "
            f"{accident}"
        )

        print("\nPrediction")

        print(
            f"Congestion Level : "
            f"{result['level']}"
        )

        print(
            f"Probability      : "
            f"{result['probability']:.2f}"
        )

        print("===================================")