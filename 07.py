import re
import sys
import networkx as nx

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
        graph.add_edge(next_bag, bag_name, weight=count)

my_bag = "shiny gold"
print(len(list(nx.dfs_predecessors(graph, my_bag))))
