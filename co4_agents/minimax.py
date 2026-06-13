class MinimaxAgent:

    def __init__(self, state):

        self.state = state

    def evaluate(self, lane):

        queue = self.state.queues[lane]

        return queue

    def minimax(
            self,
            lanes,
            depth,
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

            return best_score, best_lane

        else:

            best_score = float("inf")
            best_lane = None

            for lane in lanes:

                score = self.evaluate(lane)

                if score < best_score:

                    best_score = score
                    best_lane = lane

            return best_score, best_lane

    def choose_action(self):

        lanes = list(
            self.state.queues.keys()
        )

        score, lane = self.minimax(
            lanes,
            depth=2,
            maximizing=True
        )

        return lane, score