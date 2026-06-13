class ExplanationEngine:

    @staticmethod
    def generate(
            state,
            search_result,
            csp_lane,
            utility_lane,
            congestion_level):

        reasons = []

        highest_lane = max(
            state.queues,
            key=state.queues.get
        )

        reasons.append(
            f"Highest traffic density detected in "
            f"{highest_lane.upper()} lane."
        )

        reasons.append(
            f"Search algorithm selected route "
            f"{' -> '.join(search_result)}."
        )

        reasons.append(
            f"CSP scheduler recommended "
            f"{csp_lane.upper()} lane."
        )

        reasons.append(
            f"Utility agent selected "
            f"{utility_lane.upper()} lane."
        )

        reasons.append(
            f"Predicted congestion level: "
            f"{congestion_level}."
        )

        if state.emergency_lane:

            reasons.append(
                f"Emergency vehicle detected in "
                f"{state.emergency_lane.upper()} lane."
            )

        return reasons