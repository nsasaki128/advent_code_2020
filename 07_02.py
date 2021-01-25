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

    containBagNum = dict()
    def solve(bagName: str) -> int:
        if bagName in containBagNum:
            return containBagNum[bagName]
        curBag = bagNames[bagName]
        if not curBag.containBags:
            containBagNum[bagName] = 0
            return 0
        ans = 0
        for child in curBag.containBags:
            ans += child.num * (1 + solve(child.bag.name))
        containBagNum[bagName] = ans
        return ans

    print(solve(countBagName))
#    for _, bag in bagNames.items():
#        bag.printContainBags()
#        bag.printParentBags()


if __name__ == '__main__':
	main()
