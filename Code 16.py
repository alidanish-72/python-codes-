def is_valid(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for ch in s:
        if ch in "([{":
            stack.append(ch)

        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False

            stack.pop()

    return len(stack) == 0


print(is_valid("({[]})"))  # True
print(is_valid("([)]"))    # False