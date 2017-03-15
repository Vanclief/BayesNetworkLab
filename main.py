import fileinput
import re

class Node:
	parents = []
	probability_table = {}

	def add_parent(parent):
		parents.append(parent)

	def add_probability(given_probs):
		for prob in given_probs:
			print(prob)

def process_input(lines):
	for line in lines[:]:
		if line.startswith("[Nodes]"):
			lines.pop(0)
			return lines
		lines.pop(0)

def input_to_nodes(lines):
	nodes = {}
	for node in lines[0].split(', '):
		nodes[node] = Node()
	for line in lines[:]:
		if line.startswith("[Probabilities]"):
			lines.pop(0)
			return lines, nodes
		lines.pop(0)

def input_to_probs(lines, nodes):
	for line in lines[:]:
		if line.startswith("\n"):
			lines.pop(0)
			lines.pop(0)
			return lines, nodes
		statement = line.split(' = ')
		posterior = statement[0].split('|')
		if len(posterior) > 1:
			posterior[1] = posterior[1].split(', ')
		probability = statement[1][:-1]
		print(posterior)
		print(probability)

		
		# print(nodes[statement[0][1:]])
		# for s in statement:
		# 	print(s)
		# print("\n")

		lines.pop(0)


# def input_to_queries():

def main():
	lines = []
	nodes = {}	

	for line in fileinput.input():
	    lines.append(line)
	lines = list(map(lambda x: x.strip(''), lines))

	lines = process_input(lines)
	lines, nodes = input_to_nodes(lines)
	lines, nodes = input_to_probs(lines, nodes)

if __name__ == '__main__':
	main()