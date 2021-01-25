import re
def main():
    count = 135#6
    checkCount = 616-count-1
    rules = dict()
    inDict = dict()
    values = set()

    for _ in range(count):
        p = input().split(":")
        i = p[0]
        values.add(i)
        v = p[1].strip()
        if v[0] == "\"":
            rules[i] = list(v[1])
            continue
        v = v.split("|")
        rules[i] = list()
        for r in v:
            cur = list()
            rs = r.split()
            for x in rs:
                values.add(x)
                cur.append(x)
                if not x in inDict:
                    inDict[x] = set()
                inDict[x].add(i)
            rules[i].append(cur)

    sortedList = topologicalSort(inDict, values)
    regexRule = createRegexRule(sortedList, rules)
    pattern = re.compile(regexRule)
    input()
    ans = 0
    matches = list()
    for _ in range(checkCount):
        ans += 1 if pattern.fullmatch(input()) else 0
    print(ans)

def topologicalSort(inDict, values):
    sortedSet = set()
    sortedList = list()
    while inDict:
        curIn = set()
        removeSet = set()
        for k in inDict.keys():
            curIn.add(k)
        for v in values:
            if v not in curIn:
                removeSet.add(v)
        for v in removeSet:
            values.discard(v)
            if v not in sortedSet:
                sortedList.append(v)
                sortedSet.add(v)
            for k, vs in inDict.items():
                if v in vs:
                    inDict[k].discard(v)
        for k in curIn:
            if len(inDict[k]) == 0:
                inDict.pop(k)
                if k not in sortedSet:
                    sortedList.append(k)
                    sortedSet.add(k)
    return sortedList

def createRegexRule(sortedList, rules):
    regexRules = dict()
    for v in reversed(sortedList):
        # terminal symbol
        if type(rules[v][0]) is str:
            regexRules[v] = rules[v][0]
            continue
        # no OR
        if len(rules[v]) == 1:
            cur = ""
            for k in rules[v][0]:
                cur += regexRules[k]
            regexRules[v] = cur
            continue

        cur = "("
        for i in range(len(rules[v])):
            if i != 0:
                cur += "|"
            for k in rules[v][i]:
                cur += regexRules[k]
        cur += ")"
        regexRules[v] = cur
    return regexRules["0"]

if __name__ == '__main__':
	main()
