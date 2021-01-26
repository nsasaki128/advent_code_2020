from collections import defaultdict
def main():
    count = 33
    unknown_sentences = list()
    known_words = list()
    guess = defaultdict(set)
    ans = 0

    for _ in range(count):
        p = input()
        l, r = p.split(" (contains ")
        unknowns = l.split()
        unknown_sentences.append(unknowns)
        knowns = r.split(", ")
        knowns[-1] = knowns[-1][:-1]
        known_words.append(knowns)
        cur_guess = defaultdict(set)
        for known in knowns:
            for unknown in unknowns:
                cur_guess[known].add(unknown)
        for known in knowns:
            if known in guess:
                guess[known] &= cur_guess[known]
            else:
                guess[known] = cur_guess[known]

    determine_words = dict()
    determine_unknown_words = dict()
    is_changed = True
    while is_changed:
        is_changed = False
        cur_knowns = set()
        cur_unknowns = set()
        for known_word, possible_unknowns in guess.items():
            if len(possible_unknowns) == 1:
                unknown_word = possible_unknowns.pop()
                cur_knowns.add(known_word)
                cur_unknowns.add(unknown_word)
                determine_words[unknown_word] = known_word
                determine_unknown_words[known_word] = unknown_word
                is_changed = True

        for word in cur_knowns:
            guess.pop(word)

        for possible_unknowns in guess.values():
            for word in cur_unknowns:
                if word in possible_unknowns:
                    possible_unknowns.discard(word)

    # Part One
    ans_one = 0
    for unknown_words in unknown_sentences:
        for word in unknown_words:
            ans_one += 1 if word not in determine_words else 0
    print(ans_one)

    ans_keys = list(determine_unknown_words)
    ans_keys.sort()

    ans_two = list()
    for k in ans_keys:
        ans_two.append(determine_unknown_words[k])

    print(",".join(ans_two))



if __name__ == '__main__':
	main()
