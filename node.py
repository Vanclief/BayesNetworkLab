class Node:
    def __init__(self, value, parents, probabilities_table):
        self.value = value
        self.parents = parents
        self.probabilities_table = probabilities_table

    def __repr__(self):
        return "Node(%s %s %s)" % (self.value, self.parents, self.probabilities_table)
