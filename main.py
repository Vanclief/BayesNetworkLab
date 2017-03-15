import fileinput
import re

# Node Class
class Node:
    def __init__(self, parents, probabilities_table):
        self.parents = parents
        self.probabilities_table = probabilities_table

    def __repr__(self):
        return "Node(%s %s)" % (self.parents, self.probabilities_table)

# Serialize Input into lines


def process_input():
    lines = []

    for line in fileinput.input():
        lines.append(line)

    lines = list(map(lambda x: x.strip('').rstrip(
        '\n').rstrip('\r').replace(' ', ''), lines))

    return lines

# Parse the input lines into a dictionary of lists containing Nodes,
# Probabilities and Queries


def parse_input(lines):
    sections = {}
    current_section = None
    pattern = re.compile(r"\[([A-Za-z0-9_]+)\]")

    for line in lines[:]:
        section = pattern.match(line)
        if section:
            current_section = section.group(0)
            sections[current_section] = []
        elif current_section and line != '':
            sections[current_section].append(line)
    return sections

# Create the nodes for the Bayesian Network


def create_nodes(sections):

    bayesian_network = {}
    nodes = sections['[Nodes]']
    for node in nodes[0].split(','):
        parents = get_parents(node, sections)
        probabilities = get_probabilities(node, sections)
        probabilities_table = get_probabilities_table(node, probabilities)
        bayesian_network[node] = Node(parents, probabilities_table)

    print(bayesian_network)
    return bayesian_network

# Return a list with the name of the parents of the node


def get_parents(node, sections):

    nodes = sections['[Nodes]']
    probabilities = sections['[Probabilities]']
    parents = list()

    filtered = list(
        filter(
            lambda x: (x[1:x.find('|')]).count(node) > 0, probabilities)
    )

    if len(filtered) > 1:
        for i in filtered:
            for n in nodes[0].split(','):
                if n in i and n != node and n not in parents:
                    parents.append(n)

    return parents


# Returns a list with the probabilities of each node

def get_probabilities(node, sections):
    probabilities_list = list()
    nodes = sections['[Nodes]']
    probabilities = sections['[Probabilities]']

    filtered = list(
        filter(
            lambda x: (x[1:x.find('|')]).count(node) > 0, probabilities)
    )

    for i in filtered:
        if '|' in i:
            probs = i.split('|', 1)[-1]
            probabilities_list.append(probs)
        else:
            probabilities_list.append(i)

    return probabilities_list

# Return a dictionary with the probabilities table of a node
def get_probabilities_table(node, probabilities):
    return probabilities


def main():

    lines = process_input()
    sections = parse_input(lines)
    create_nodes(sections)


if __name__ == '__main__':
    main()
