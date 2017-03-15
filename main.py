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


def parse_nodes(sections):
    nodes = sections['[Nodes]']
    for node in nodes[0].split(','):
        print(get_parents(node, sections))




def get_parents(node, sections):
    result = list()
    nodes = sections['[Nodes]']
    probabilities = sections['[Probabilities]']

    print('--' + node + '--')
    parents = list(
        filter(lambda x: (x[1:x.find('|')]).count(node) > 0, probabilities))

    if len(parents) > 1:
        for i in parents:
            for n in nodes[0].split(','):
                if n in i and n != node and n not in result:
                    result.append(n)

    return result

def main():

    lines = process_input()
    sections = parse_input(lines)
    parse_nodes(sections)


if __name__ == '__main__':
    main()
