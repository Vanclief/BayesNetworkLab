import fileinput
import re

# Import Node Class
Node = __import__('node')

# Serialize Input into lines


def process_input(lines):
    for line in lines[:]:
        if line.startswith("[Nodes]"):
            lines.pop(0)
            return lines
        lines.pop(0)


def parse_input(lines):
    sections = {}
    current_section = None
    # pattern = re.compile("/\[(?<value>.*)\]/")
    pattern = re.compile(r"\[([A-Za-z0-9_]+)\]")
    # pattern = re.compile("^([A-Z][0-9]+)+$")

    for line in lines[:]:
        section = pattern.match(line)
        if section:
            current_section = section.group(0)
            sections[current_section] = []
        elif current_section and line != '':
            sections[current_section].append(line)
    return sections

# def input_to_nodes(lines):
    # nodes = {}
    # for node in lines[0].split(', '):
    # nodes[node] = ()
    # for line in lines[:]:
    # if line.startswith("[Probabilities]"):
    # lines.pop(0)
    # return lines, nodes
    # lines.pop(0)

# def input_to_probs(lines, nodes):
    # for line in lines[:]:
    # if line.startswith("\n"):
    # lines.pop(0)
    # lines.pop(0)
    # return lines, nodes
    # statement = line.split(' = ')
    # posterior = statement[0].split('|')
    # if len(posterior) > 1:
    # posterior[1] = posterior[1].split(', ')
    # probability = statement[1][:-1]
    # print(posterior)
    # print(nodes)
    # print(probability)

    # print(nodes[statement[0][1:]])
    # for s in statement:
    # 	print(s)
    # print("\n")

    # lines.pop(0)


# def input_to_queries():

def main():

    lines = []
    nodes = {}

    for line in fileinput.input():
        lines.append(line)

    lines = list(map(lambda x: x.strip('').rstrip(
        '\n').rstrip('\r').replace(' ', ''), lines))

    sections = parse_input(lines)


if __name__ == '__main__':
    main()
