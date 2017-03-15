class Node:
    parents = []
    probability_table = {}

    def add_parent(
            parent
    ):
        parents.append(
            parent
        )

    def add_probability(
            given_probs
    ):
        for prob in given_probs:
            print(
                prob
            )
