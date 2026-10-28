class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(
                min(val, self.min_stack[-1])
            )

    def pop(self):
        if not self.stack:
            return None

        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]


s = MinStack()
s.push(5)
s.push(2)
s.push(8)

print(s.get_min())  # 2
s.pop()
print(s.top())      # 2
print(s.get_min())  # 2