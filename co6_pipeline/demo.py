from core.traffic_state import TrafficState

from co6_pipeline.integrated_reasoner import (
    IntegratedReasoner
)


def run_demo():

    state = TrafficState()

    print("\nCURRENT TRAFFIC")

    for lane, count in state.queues.items():

        print(
            f"{lane.upper():<10} : {count}"
        )

    ai = IntegratedReasoner(
        state
    )

    ai.run()