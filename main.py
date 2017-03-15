import fileinput
import re

# Import Node Class
Node = __import__('node')

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


def parse_nodes(sections):
    nodes = sections['[Nodes]']
    for node in nodes[0].split(','):
        get_parents(node, sections)
        get_probabilities(node, sections)

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


def main():

    lines = process_input()
    sections = parse_input(lines)
    parse_nodes(sections)


if __name__ == '__main__':
    main()
