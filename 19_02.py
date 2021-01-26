import re
def main():
    count = 135#6
    check_count = 616-count-1
    rules = dict()
    in_dict = dict()
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
                if not x in in_dict:
                    in_dict[x] = set()
                in_dict[x].add(i)
            rules[i].append(cur)

    sorted_list = topological_sort(in_dict, values)
    head, tail = create_regex_rules(sorted_list, rules)
    pattern_head = re.compile(head)
    pattern_tail = re.compile(tail)
    input()
    ans = 0
    matches = list()
    for _ in range(check_count):
        rest = input()
        head_num = 0
        while rest:
            m = pattern_head.match(rest)
            if not m:
                break
            rest = rest[m.end():]
            head_num += 1
        if head_num < 1:
            continue
        tail_num = 0
        while rest:
            m = pattern_tail.match(rest)
            if not m:
                break
            rest = rest[m.end():]
            tail_num += 1
        if head_num > tail_num and tail_num != 0 and not rest:
            ans += 1

    print(ans)

def topological_sort(in_dict, values):
    sorted_set = set()
    sorted_list = list()
    while in_dict:
        cur_in = set()
        remove_set = set()
        for k in in_dict.keys():
            cur_in.add(k)
        for v in values:
            if v not in cur_in:
                remove_set.add(v)
        for v in remove_set:
            values.discard(v)
            if v not in sorted_set:
                sorted_list.append(v)
                sorted_set.add(v)
            for k, vs in in_dict.items():
                if v in vs:
                    in_dict[k].discard(v)
        for k in cur_in:
            if len(in_dict[k]) == 0:
                in_dict.pop(k)
                if k not in sorted_set:
                    sorted_list.append(k)
                    sorted_set.add(k)
    return sorted_list

def create_regex_rules(sorted_list, rules):
    regex_rules = dict()
    for v in reversed(sorted_list):
        # _actually ignore these rules
        if v == "8":
            regex_rules[v] = "(" + regex_rules["42"] + ")+"
            continue
        if v == "11":
            regex_rules[v] = "(" + regex_rules["42"] +  regex_rules["31"] + ")+"
            continue

        # terminal symbol
        if type(rules[v][0]) is str:
            regex_rules[v] = rules[v][0]
            continue
        # no _o_r
        if len(rules[v]) == 1:
            cur = ""
            for k in rules[v][0]:
                cur += regex_rules[k]
            regex_rules[v] = cur
            continue

        cur = "("
        for i in range(len(rules[v])):
            if i != 0:
                cur += "|"
            for k in rules[v][i]:
                cur += regex_rules[k]
        cur += ")"
        regex_rules[v] = cur
    return "^"+regex_rules["42"], "^"+regex_rules["31"]

if __name__ == '__main__':
	main()
