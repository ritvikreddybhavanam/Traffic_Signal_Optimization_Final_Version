from co1_representation.state_space import StateSpace
from co1_representation.reasoning_trace import ReasoningTrace

from co2_search.road_network import RoadNetwork
from co2_search.astar import astar

from co3_csp.scheduler import TrafficCSP

from co4_agents.utility_agent import UtilityAgent

from co5_uncertainty.inference import TrafficInference

from co6_pipeline.explanation_engine import (
    ExplanationEngine
)


class IntegratedReasoner:

    def __init__(self, state):

        self.state = state

    def run(self):

        print("\n")
        print("=" * 60)
        print("CO6 INTEGRATED AI PIPELINE")
        print("=" * 60)

        # ----------------------------------
        # CO1
        # ----------------------------------

        state_space = StateSpace(
            self.state
        )

        trace = ReasoningTrace()

        trace.generate_state_reasoning(
            self.state
        )

        print("\n[CO1 COMPLETED]")
        print(
            f"Traffic Cost = "
            f"{state_space.calculate_cost()}"
        )

        # ----------------------------------
        # CO2
        # ----------------------------------

        network = RoadNetwork()

        graph = network.get_graph()

        heuristic = network.get_heuristic()

        path, route_cost = astar(
            graph,
            heuristic,
            "A",
            "F"
        )

        print("\n[CO2 COMPLETED]")

        print(
            f"Route = "
            f"{' -> '.join(path)}"
        )

        print(
            f"Route Cost = "
            f"{route_cost}"
        )

        # ----------------------------------
        # CO3
        # ----------------------------------

        csp = TrafficCSP(self.state)

        schedule = csp.get_full_schedule()

        recommended_lane = csp.schedule()

        print("\n[CO3 COMPLETED]")

        print(
            f"Recommended Lane = "
            f"{recommended_lane.upper()}"
        )

        # ----------------------------------
        # CO4
        # ----------------------------------

        utility_agent = UtilityAgent(
            self.state
        )

        utility_lane, utilities = (
            utility_agent.choose_action()
        )

        print("\n[CO4 COMPLETED]")

        print(
            f"Utility Lane = "
            f"{utility_lane.upper()}"
        )

        # ----------------------------------
        # CO5
        # ----------------------------------

        inference = TrafficInference()

        result = inference.predict(
            rush_hour=True,
            rain=False,
            accident=False
        )

        print("\n[CO5 COMPLETED]")

        print(
            f"Congestion = "
            f"{result['level']}"
        )

        print(
            f"Probability = "
            f"{result['probability']:.2f}"
        )

        # ----------------------------------
        # FINAL DECISION
        # ----------------------------------

        final_lane = utility_lane

        if self.state.emergency_lane:

            final_lane = (
                self.state.emergency_lane
            )

        print("\n")
        print("=" * 60)
        print("FINAL DECISION")
        print("=" * 60)

        print(
            f"Selected Green Signal : "
            f"{final_lane.upper()}"
        )

        print("\nReasoning")

        reasons = (
            ExplanationEngine.generate(
                self.state,
                path,
                recommended_lane,
                utility_lane,
                result["level"]
            )
        )

        for index, reason in enumerate(
                reasons,
                start=1):

            print(
                f"{index}. {reason}"
            )

        print("=" * 60)

        return final_lane