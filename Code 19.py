def insert_at_bottom(stack, value):
    if not stack:
        stack.append(value)
        return

    top = stack.pop()
    insert_at_bottom(stack, value)
    stack.append(top)


def reverse_stack(stack):
    if not stack:
        return

    top = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)


stack = [1, 2, 3, 4, 5]
reverse_stack(stack)

print(stack)  # [5, 4, 3, 2, 1]