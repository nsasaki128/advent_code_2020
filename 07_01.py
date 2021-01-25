import copy

class Bag:
    def __init__(self, name: str):
        self.name = name
        self.containBags = list()
        self.parents = list()

    def addChildBag(self, bag, num: int):
        self.containBags.append(ContainBag(bag, num))

    def addParentBag(self, bag, num: int):
        self.parents.append(ContainBag(bag, num))

    def printContainBags(self):
        print("-------------------------------------------------")
        print(self.name)
        for child in self.containBags:
            print(f"|-name: {child.bag.name}, num: {child.num}")
        print("|________________________________________________")

    def printParentBags(self):
        print("-------------------------------------------------")
        for parent in self.parents:
            print(f"|-name: {parent.bag.name}, num: {parent.num}")
        print(f"|_{self.name}")
        print("-------------------------------------------------")

class ContainBag:
    def __init__(self, bag, num: int):
        self.bag = bag
        self.num = num

def extractColor(bagName: str):
    bagName = bagName.removesuffix("bags")
    bagName = bagName.removesuffix("bag")
    return bagName.strip()

def main():
    bagNames = dict()

    count = 594
    countBagName = "shiny gold"

    for _ in range(count):
        p = input()
        parent, inside = p.split("contain")
        parent = parent[:-1]
        inside = inside[1:-1]

        parent = extractColor(parent)
        if parent not in bagNames:
            bagNames[parent] = Bag(parent)

        children = inside.split(",")
        for child in children:
            child = extractColor(child)
            if child == "no other":
                continue
            num, child = int(child[0]), child[1:].strip()
            if child not in bagNames:
                bagNames[child] = Bag(child)

            bagNames[child].addParentBag(bagNames[parent], num)
            bagNames[parent].addChildBag(bagNames[child], num)

    ansParents = {countBagName}
    parentsList = list()
    parentsList.append(countBagName)
    while parentsList:
        cur = parentsList.pop()
        for p in bagNames[cur].parents:
            if p.bag.name in ansParents:
                continue
            parentsList.append(p.bag.name)
            ansParents.add(p.bag.name)

    print(len(ansParents)-1)
#    for _, bag in bagNames.items():
#        bag.printContainBags()
#        bag.printParentBags()


if __name__ == '__main__':
	main()
