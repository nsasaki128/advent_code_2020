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

    contain_bag_num = dict()
    def solve(bag_name: str) -> int:
        if bag_name in contain_bag_num:
            return contain_bag_num[bag_name]
        cur_bag = bag_names[bag_name]
        if not cur_bag.contain_bags:
            contain_bag_num[bag_name] = 0
            return 0
        ans = 0
        for child in cur_bag.contain_bags:
            ans += child.num * (1 + solve(child.bag.name))
        contain_bag_num[bag_name] = ans
        return ans

    print(solve(count_bag_name))
#    for _, bag in bag_names.items():
#        bag.print_contain_bags()
#        bag.print_parent_bags()


if __name__ == '__main__':
	main()
