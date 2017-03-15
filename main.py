import fileinput

class Node:
	# Node class
	parents = []
	probability_table = {}

	def add_parent 

	def add_prob(nodes, probability):
		nodes.
# end Node

def process_input(input):
	nodes = []
	for line in input:
		if line.startswith("[Nodes]"):
			print(line)

def input_to_nodes(lines):
	nodes = {}

	while (line in lines):
		if line.startswith("[Probabilities]"):
			return lines, nodes
		

# def input_to_probs():

# def input_to_queries():

def main():
	lines = []
	for line in fileinput.input():
	    lines.append(line)
	lines = list(map(lambda x: x.strip(), lines))
	network = {}	

	lines, network = input_to_nodes(lines)




if __name__ == '__main__':
	main()