import sys
sys.stdout.reconfigure(encoding="utf-8")

from core.traffic_state import TrafficState
from core.environment import TrafficEnvironment

from utils.logger import get_logger

# CO1
from co1_representation.state_space import StateSpace
from co1_representation.reasoning_trace import ReasoningTrace

# CO2
from co2_search.road_network import RoadNetwork
from co2_search.bfs import bfs
from co2_search.dfs import dfs
from co2_search.ucs import ucs
from co2_search.greedy import greedy_search
from co2_search.astar import astar

# CO3
from co3_csp.scheduler import TrafficCSP

# CO4
from co4_agents.utility_agent import UtilityAgent
from co4_agents.minimax import MinimaxAgent
from co4_agents.alpha_beta import AlphaBetaAgent

# CO5
from co5_uncertainty.inference import TrafficInference

# CO6
from co6_pipeline.integrated_reasoner import IntegratedReasoner


def display_state(state):

    print("\nCurrent Traffic State")
    print("-" * 40)

    for lane, count in state.queues.items():

        print(
            f"{lane.upper():<10} : {count:>3} Vehicles"
        )

    print("-" * 40)


def run_simulation(steps=3):

    logger = get_logger()

    print("\n")
    print("╔════════════════════════════════════════════════════╗")
    print("║     INTELLIGENT TRAFFIC SIGNAL AI SYSTEM          ║")
    print("║              CO1 → CO6 IMPLEMENTATION            ║")
    print("╚════════════════════════════════════════════════════╝")

    env = TrafficEnvironment()

    state = env.get_state()

    logger.info("Simulation Started")

    display_state(state)

    for step in range(steps):

        print("\n")
        print("=" * 60)
        print(f"SIMULATION STEP {step + 1}")
        print("=" * 60)

        # ==================================================
        # CO1
        # ==================================================

        print("\n")
        print("=" * 60)
        print("CO1 : STATE SPACE REPRESENTATION")
        print("=" * 60)

        state_space = StateSpace(state)

        state_space.display()

        trace = ReasoningTrace()

        trace.generate_state_reasoning(state)

        trace.display()

        logger.info("CO1 Completed")

        # ==================================================
        # CO2
        # ==================================================

        print("\n")
        print("=" * 60)
        print("CO2 : SEARCH ALGORITHMS")
        print("=" * 60)

        network = RoadNetwork()

        graph = network.get_graph()

        heuristic = network.get_heuristic()

        bfs_path = bfs(graph, "A", "F")

        dfs_path = dfs(graph, "A", "F")

        ucs_path, ucs_cost = ucs(
            graph,
            "A",
            "F"
        )

        greedy_path = greedy_search(
            graph,
            heuristic,
            "A",
            "F"
        )

        astar_path, astar_cost = astar(
            graph,
            heuristic,
            "A",
            "F"
        )

        print("\nBFS")
        print("Path:", " -> ".join(bfs_path))

        print("\nDFS")
        print("Path:", " -> ".join(dfs_path))

        print("\nUCS")
        print("Path:", " -> ".join(ucs_path))
        print("Cost:", ucs_cost)

        print("\nGREEDY")
        print("Path:", " -> ".join(greedy_path))

        print("\nA*")
        print("Path:", " -> ".join(astar_path))
        print("Cost:", astar_cost)

        logger.info("CO2 Completed")

        # ==================================================
        # CO3
        # ==================================================

        print("\n")
        print("=" * 60)
        print("CO3 : CSP SIGNAL SCHEDULING")
        print("=" * 60)

        csp = TrafficCSP(state)

        schedule = csp.get_full_schedule()

        for lane, duration in schedule.items():

            print(
                f"{lane.upper():<10} : "
                f"{duration} sec"
            )

        csp_lane = csp.schedule()

        print(
            f"\nRecommended Lane : "
            f"{csp_lane.upper()}"
        )

        logger.info("CO3 Completed")

        # ==================================================
        # CO4
        # ==================================================

        print("\n")
        print("=" * 60)
        print("CO4 : INTELLIGENT AGENTS")
        print("=" * 60)

        utility_agent = UtilityAgent(state)

        utility_lane, utilities = (
            utility_agent.choose_action()
        )

        print("\nUtility Agent")

        for lane, score in utilities.items():

            print(
                f"{lane.upper():<10} : {score}"
            )

        print(
            f"\nSelected Lane : "
            f"{utility_lane.upper()}"
        )

        minimax_agent = MinimaxAgent(state)

        mini_lane, mini_score = (
            minimax_agent.choose_action()
        )

        print("\nMinimax")

        print(
            f"Best Lane : {mini_lane.upper()}"
        )

        print(
            f"Score     : {mini_score}"
        )

        alpha_agent = AlphaBetaAgent(state)

        alpha_lane, alpha_score, pruned = (
            alpha_agent.choose_action()
        )

        print("\nAlpha-Beta")

        print(
            f"Best Lane     : {alpha_lane.upper()}"
        )

        print(
            f"Score         : {alpha_score}"
        )

        print(
            f"Pruned Nodes  : {pruned}"
        )

        logger.info("CO4 Completed")

        # ==================================================
        # CO5
        # ==================================================

        print("\n")
        print("=" * 60)
        print("CO5 : BAYESIAN REASONING")
        print("=" * 60)

        inference = TrafficInference()

        result = inference.predict(
            rush_hour=True,
            rain=False,
            accident=False
        )

        print(
            f"Congestion Level : "
            f"{result['level']}"
        )

        print(
            f"Probability      : "
            f"{result['probability']:.2f}"
        )

        logger.info("CO5 Completed")

        # ==================================================
        # CO6
        # ==================================================

        print("\n")
        print("=" * 60)
        print("CO6 : INTEGRATED REASONING")
        print("=" * 60)

        ai = IntegratedReasoner(state)

        final_lane = ai.run()

        logger.info(
            f"Final Decision: {final_lane}"
        )

        # ==================================================
        # APPLY SIGNAL
        # ==================================================

        print("\n")
        print("=" * 60)
        print("SIGNAL EXECUTION")
        print("=" * 60)

        before = state.queues[final_lane]

        vehicles_passed = state.apply_green(
            final_lane
        )

        state.update_waiting()

        state.add_new_traffic()

        after = state.queues[final_lane]

        print(
            f"Green Signal : "
            f"{final_lane.upper()}"
        )

        print(
            f"Vehicles Passed : "
            f"{vehicles_passed}"
        )

        print(
            f"Queue Reduced : "
            f"{before} -> {after}"
        )

        display_state(state)

        logger.info(
            f"Step {step + 1} Completed"
        )

    print("\n")
    print("=" * 60)
    print("FINAL TRAFFIC STATE")
    print("=" * 60)

    display_state(state)

    logger.info("Simulation Completed")

    print("\n✅ PROJECT EXECUTION COMPLETED")


if __name__ == "__main__":

    run_simulation(steps=3)