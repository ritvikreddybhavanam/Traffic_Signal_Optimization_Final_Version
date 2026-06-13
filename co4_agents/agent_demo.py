from core.traffic_state import TrafficState

from co4_agents.utility_agent import UtilityAgent
from co4_agents.minimax import MinimaxAgent
from co4_agents.alpha_beta import AlphaBetaAgent


def run_demo():

    state = TrafficState()

    print("\n===================================")
    print("CO4 DECISION MAKING AGENTS")
    print("===================================")

    print("\nCurrent Traffic")

    for lane, count in state.queues.items():

        print(
            f"{lane.upper():<10} : {count}"
        )

    utility_agent = UtilityAgent(state)

    lane, utilities = (
        utility_agent.choose_action()
    )

    print("\nUTILITY AGENT")

    for k, v in utilities.items():

        print(
            f"{k.upper():<10} : {v}"
        )

    print(
        f"\nSelected Lane : "
        f"{lane.upper()}"
    )

    minimax_agent = MinimaxAgent(state)

    lane, score = (
        minimax_agent.choose_action()
    )

    print("\nMINIMAX")

    print(
        f"Best Lane : {lane.upper()}"
    )

    print(
        f"Score     : {score}"
    )

    alpha_agent = AlphaBetaAgent(state)

    lane, score, pruned = (
        alpha_agent.choose_action()
    )

    print("\nALPHA-BETA")

    print(
        f"Best Lane     : {lane.upper()}"
    )

    print(
        f"Score         : {score}"
    )

    print(
        f"Pruned Nodes  : {pruned}"
    )