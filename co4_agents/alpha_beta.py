class AlphaBetaAgent:

    def __init__(self, state):

        self.state = state

        self.pruned_nodes = 0

    def evaluate(self, lane):

        return self.state.queues[lane]

    def alpha_beta(
            self,
            lanes,
            depth,
            alpha,
            beta,
            maximizing):

        if depth == 0:

            scores = {
                lane: self.evaluate(lane)
                for lane in lanes
            }

            best_lane = max(
                scores,
                key=scores.get
            )

            return scores[best_lane], best_lane

        if maximizing:

            best_score = float("-inf")
            best_lane = None

            for lane in lanes:

                score = self.evaluate(lane)

                if score > best_score:

                    best_score = score
                    best_lane = lane

                alpha = max(
                    alpha,
                    best_score
                )

                if beta <= alpha:

                    self.pruned_nodes += 1
                    break

            return best_score, best_lane

        else:

            best_score = float("inf")
            best_lane = None

            for lane in lanes:

                score = self.evaluate(lane)

                if score < best_score:

                    best_score = score
                    best_lane = lane

                beta = min(
                    beta,
                    best_score
                )

                if beta <= alpha:

                    self.pruned_nodes += 1
                    break

            return best_score, best_lane

    def choose_action(self):

        lanes = list(
            self.state.queues.keys()
        )

        score, lane = self.alpha_beta(
            lanes,
            depth=2,
            alpha=float("-inf"),
            beta=float("inf"),
            maximizing=True
        )

        return (
            lane,
            score,
            self.pruned_nodes
        )