def process_rules(raw):
    output = {}
    for row in raw:
        parent, children = row.split(" contain ")
        parent = parent.replace("bags", "bag")
        children = process_children(children)
        output[parent] = children
    return output
def process_children(children):
    output = []
    for child in children.split(", "):
        child = child.strip().replace("bags", "bag")
        if child == "no other bag.":
            return []
        num = child.split(" ")[0]
        if num == "no":
            num_val = 0
        else:
            num_val = int(num)
        child = child.replace(num, "").strip()
        output.append({"name": child.replace(".",""), "n": num_val})
    return output

def traverse_children(children, current_node, matching_nodes, tree):
    for child in children:
        children_of_children = tree[child["name"]]
        if len(children_of_children) == 0 or bag_found(children_of_children, matching_nodes, current_node):
            continue
        traverse_children(children_of_children, current_node, matching_nodes, tree)

def bag_found(children, matching_nodes, current_node):
    bags = [child["name"] for child in children]
    if "shiny gold bag" in bags:
        matching_nodes.append(current_node)
        return True
    return False

def search_tree(tree):
    matching_nodes = []
    for node, children in tree.items():
        if bag_found(children, matching_nodes, node):
            continue
        traverse_children(children, node, matching_nodes, tree)
    
    return matching_nodes

inputs = open("inputs/07_test_2.txt").readlines()
data = process_rules(inputs)
def part1():
    matches = search_tree(data)
    print(matches)
    
def count_bags(list_of_bags, tree):
    if list_of_bags == []:
        return 1
    total = 1
    for bag in list_of_bags:
        next_bag = tree[bag["name"]]
        this_bag_count = bag["n"]
        total += this_bag_count * count_bags(next_bag, tree)
    return total

def part2():
    head = data["shiny gold bag"]
    bags = count_bags(head, data)
    print(bags)
part2()

