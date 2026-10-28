def subsequences(s, i=0, current=""):
    if i == len(s):
        print(current if current else '""')
        return

    # Include the character
    subsequences(s, i + 1, current + s[i])

    # Exclude the character
    subsequences(s, i + 1, current)

subsequences("ab")