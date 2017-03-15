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

# Check if the node has parents

def is_parent(sections):
    nodes = sections['[Nodes]']
    probabilities = sections['[Probabilities]']
    for node in nodes[0].split(','):
        for probability in probabilities:
            print(node)
            print(probability)


def main():

    lines = process_input()
    sections = parse_input(lines)
    is_parent(sections)


if __name__ == '__main__':
    main()
