from co5_uncertainty.inference import (
    TrafficInference
)


def run_demo():

    inference = TrafficInference()

    inference.print_prediction(
        rush_hour=True,
        rain=True,
        accident=False
    )

    inference.print_prediction(
        rush_hour=False,
        rain=False,
        accident=False
    )