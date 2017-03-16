import fileinput
import re

# Node Class


class Node:
    def __init__(self, name, parents, probabilities_table):
        self.name = name
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

# Remove + or - from string


def get_nodes_from_query(query):
    nodes = []
    for elements in query:
        for element in elements:
            nodes.append(element[1:])

    return nodes

# Create the nodes for the Bayesian Network


def create_nodes(sections):
    bayesian_network = {}
    nodes = sections['[Nodes]']

    for node in nodes[0].split(','):
        parents = get_parents(node, sections)
        probabilities = get_probabilities(node, sections)
        probabilities_table = get_probabilities_table(node, probabilities)
        bayesian_network[node] = Node(node, parents, probabilities_table)

    return bayesian_network

# Prints a Bayesian Network


def print_network(bayesian_network):
    for node in bayesian_network:
        print(node)
        print(bayesian_network[node].parents)
        for prob in bayesian_network[node].probabilities_table:
            print(
                prob,
                bayesian_network[node].probabilities_table[prob]
            )

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
    prob_table = {}
    for line in probabilities[:]:
        given, prob = line.split('=')
        prob = float(prob)
        given = given.split(",")
        given.sort(key=lambda x: x[1:])
        key = ""
        for item in given:
        	if not item[1:] == node:
        		key += (item)
        true_key = "+" + node + key
        false_key = "-" + node + key
        prob_table[true_key] = prob
        prob_table[false_key] = 1 - prob
    return prob_table

# Return a list with list of queries, which are dictionaries with
# "queried" and "given" elements each


def create_queries(sections):
    queries_list = []
    queries = sections['[Queries]']
    for line in queries:
        query_elements = []
        element = []
        query = line.split('|')
        for i in query:
            element = i.split(',')
            element.sort(key=lambda x: x[1:])
            query_elements.append(element)
        queries_list.append(query_elements)
    return queries_list

# Process queries and get their probabilities


def process_queries(bayesian_network, queries):
    # print_network(bayesian_network)
    for query in queries:
        if len(query) == 1:
            prob = get_probability_from_node(bayesian_network, query)
            print(prob)
        else:
            q = filter_query(bayesian_network, query)
            print(q)


def get_probability_from_node(bayesian_network, query):
    node_name = get_nodes_from_query(query)
    node = bayesian_network[node_name[0]]
    return node.probabilities_table[query[0][0]]

# Remove independent nodes


def filter_query(bayesian_network, query):
    left = query[0]
    right = query[1]

    queried = list()
    queried_parents = list()
    given = list()
    print(query)

    for l in left:
        node = bayesian_network[l[1:]]
        queried.append(node)
        if len(node.parents) > 0:
            for parent in node.parents:
                queried_parents.append(parent)

    for r in right:
        given.append(r[1:])

    filtered_query = [i for e in queried_parents for i in given if e in i]

    print('Debug:')
    print(queried)
    print(given)
    print(filtered_query)

    # return filtered_query
    return ''


# Normalize the probabiity so it adds up 1
def normalize(distribution):
    return tuple(x * 1 / (sum(distribution)) for x in distribution)


def sort_query():
    print("TODO")

# Calculate the distribution using enumeration


def enumeration_ask(query, evidence):
    result = []
    for x in [False, True]:
        evidence = copy.deepcopy(evidence)
        evidence[query] = x
         # variables = sort_query(query) THIS NEEDS TO BE DONE
        result.append(enumeration_all(variables, evidence))
    return normalize(result)


def enumeration_all(variables, evidence):
    if len(variables) == 0:
        return 1.0

    Left = variables[0]
    if Left in evidence:
        # probability = parse_query(Left, evidence) * \
            # enumeration_all.enum_all(variables[1:], evidence)
        print('This prints')
    else:
        probs = []
        evidence_copy = copy.deepcopy(evidence)
        for y in [True, False]:
            evidence_copy[Left] = y
            probs.append(parse_query(Left, evidence_copy) *
                         enumeration_all(variables[1:], evidence_copy))
        probability = sum(probs)

    return probability


def main():

    lines = process_input()
    sections = parse_input(lines)
    bayesian_network = create_nodes(sections)
    queries = create_queries(sections)
    # print_network(bayesian_network)
    process_queries(bayesian_network, queries)


if __name__ == '__main__':
    main()
