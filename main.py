import fileinput

# class Node:
# 	# Node class
# 	parents = []
# 	probability_table = {}

# 	def add_parent():


# 	def add_prob(nodes, probability):
# 		nodes.

def process_input(lines):
	for line in lines[:]:
		if line.startswith("[Nodes]"):
			lines.remove(line)
			return lines
		lines.remove(line)

def input_to_nodes(lines):
	nodes = {}
	for node in lines[0].split(', '):
		nodes[node] = "Node here"
	lines.remove(lines[0])
	lines.remove(lines[1])
	return lines, nodes



# def input_to_probs():

# def input_to_queries():

def main():
	lines = []
	network = {}	

	for line in fileinput.input():
	    lines.append(line)
	lines = list(map(lambda x: x.strip(), lines))

	lines = process_input(lines)
	lines, network = input_to_nodes(lines)

	for k, v in network.items():
		print(k, v);


if __name__ == '__main__':
	main()