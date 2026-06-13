class MRV:

    @staticmethod
    def select_variable(domains):

        return min(
            domains,
            key=lambda var: len(domains[var])
        )