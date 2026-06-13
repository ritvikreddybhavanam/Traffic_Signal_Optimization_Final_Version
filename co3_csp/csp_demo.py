from core.traffic_state import TrafficState
from co3_csp.scheduler import TrafficCSP


def run_demo():

    state = TrafficState()

    print("\n====================================")
    print("CO3 CONSTRAINT SATISFACTION")
    print("====================================")

    print("\nTraffic State")

    for lane, count in state.queues.items():

        print(
            f"{lane.upper():<10} : {count}"
        )

    csp = TrafficCSP(state)

    schedule = csp.get_full_schedule()

    print("\nSignal Allocation")

    for lane, duration in schedule.items():

        print(
            f"{lane.upper():<10} : "
            f"{duration} sec"
        )

    best = csp.schedule()

    print(
        f"\nRecommended Green Lane : "
        f"{best.upper()}"
    )