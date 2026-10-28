def permutations(s, index=0):
    if index == len(s):
        print("".join(s))
        return

    for i in range(index, len(s)):
        s[index], s[i] = s[i], s[index]

        permutations(s, index + 1)

        # Backtrack
        s[index], s[i] = s[i], s[index]

permutations(list("abc"))