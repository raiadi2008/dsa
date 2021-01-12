class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, elm):
        self.stack.append((elm, elm)) if len(self.stack) == 0 else self.stack.append(
            (elm, min(self.stack[-1][1], elm)))

    def min_val(self):
        try:
            return self.stack[-1][0]
        except IndexError:
            print("opps! stack seems to be empty")
            return -1

    def pop(self):
        try:
            return self.stack.pop()[1]
        except IndexError:
            print("the arr is already empty and cannnot be poped")
            return -1

    def print_list(self):
        print(self.stack)
        print(len(self.stack))


if __name__ == "__main__":
    pass
