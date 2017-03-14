require 'active_support/core_ext/object/blank'
require './nodes.rb'

def read_input()
  input_lines = $stdin.readlines
  input_lines.reject!(&:blank?)
  input_lines
end

def parse_input(input_lines)

  sections = {}
  current_section = nil

  input_lines.each do |line|
    section = line.match(/\[(?<value>.*)\]/)
    parsed_line = line.downcase.gsub(/[\s^"]/ ,"")
    if section
      current_section = section['value']
      sections[current_section] = []
    else
      sections[current_section] << parsed_line
    end
  end
  sections
end

def initialize_nodes(sections)

  nodes = sections["Nodes"].first
  nodes = nodes.split(',')

  nodes.each do |node|
    node = Node.new(node)
    puts node.print_name
  end
end

# Read the input
input = read_input()

# Create the sections based from the input
sections = parse_input(input)

# Initialize nodes
initialize_nodes(sections)
