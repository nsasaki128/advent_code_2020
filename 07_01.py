import copy

class Bag:
    def __init__(self, name: str):
        self.name = name
        self.contain_bags = list()
        self.parents = list()

    def add_child_bag(self, bag, num: int):
        self.contain_bags.append(Contain_bag(bag, num))

    def add_parent_bag(self, bag, num: int):
        self.parents.append(Contain_bag(bag, num))

    def print_contain_bags(self):
        print("-------------------------------------------------")
        print(self.name)
        for child in self.contain_bags:
            print(f"|-name: {child.bag.name}, num: {child.num}")
        print("|________________________________________________")

    def print_parent_bags(self):
        print("-------------------------------------------------")
        for parent in self.parents:
            print(f"|-name: {parent.bag.name}, num: {parent.num}")
        print(f"|_{self.name}")
        print("-------------------------------------------------")

class Contain_bag:
    def __init__(self, bag, num: int):
        self.bag = bag
        self.num = num

def extract_color(bag_name: str):
    bag_name = bag_name.removesuffix("bags")
    bag_name = bag_name.removesuffix("bag")
    return bag_name.strip()

def main():
    bag_names = dict()

    count = 594
    count_bag_name = "shiny gold"

    for _ in range(count):
        p = input()
        parent, inside = p.split("contain")
        parent = parent[:-1]
        inside = inside[1:-1]

        parent = extract_color(parent)
        if parent not in bag_names:
            bag_names[parent] = Bag(parent)

        children = inside.split(",")
        for child in children:
            child = extract_color(child)
            if child == "no other":
                continue
            num, child = int(child[0]), child[1:].strip()
            if child not in bag_names:
                bag_names[child] = Bag(child)

            bag_names[child].add_parent_bag(bag_names[parent], num)
            bag_names[parent].add_child_bag(bag_names[child], num)

    ans_parents = {count_bag_name}
    parents_list = list()
    parents_list.append(count_bag_name)
    while parents_list:
        cur = parents_list.pop()
        for p in bag_names[cur].parents:
            if p.bag.name in ans_parents:
                continue
            parents_list.append(p.bag.name)
            ans_parents.add(p.bag.name)

    print(len(ans_parents)-1)
#    for _, bag in bag_names.items():
#        bag.print_contain_bags()
#        bag.print_parent_bags()


if __name__ == '__main__':
	main()
