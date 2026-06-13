class RoadNetwork:

    def __init__(self):

        self.graph = {
            "A": {
                "B": 4,
                "D": 3
            },

            "B": {
                "A": 4,
                "C": 5,
                "E": 2
            },

            "C": {
                "B": 5,
                "F": 4
            },

            "D": {
                "A": 3,
                "E": 6
            },

            "E": {
                "B": 2,
                "D": 6,
                "F": 3
            },

            "F": {
                "C": 4,
                "E": 3
            }
        }

        self.heuristic = {
            "A": 10,
            "B": 7,
            "C": 5,
            "D": 8,
            "E": 3,
            "F": 0
        }

    def get_graph(self):
        return self.graph

    def get_heuristic(self):
        return self.heuristic