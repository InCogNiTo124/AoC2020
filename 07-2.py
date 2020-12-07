import re
import sys
import networkx as nx

def count_bags(graph, node):
    successors = graph.successors(node)
    successors = list(successors)
    if len(successors) == 0:
        return 0
    else:
        s = 0
        for succ in successors:
            w = graph.edges[node, succ]['weight']
            s += w * (1+count_bags(graph, succ))
        return s


node_regex = re.compile("(\w+ \w+) bags contain ")
bags_regex = re.compile("(\d) (\w+ \w+) bags?[,\.] ?")
graph = nx.DiGraph()

for line in sys.stdin:
    bag_name = node_regex.match(line).groups()[0]
    content = bags_regex.findall(line) if "no other bags" not in line else []

    graph.add_node(bag_name) # idempotent
    for count_str, next_bag in content:
        graph.add_node(next_bag) # still idempotent
        count = int(count_str)
        graph.add_edge(bag_name, next_bag, weight=count)

my_bag = "shiny gold"
print(count_bags(graph, my_bag))
