class My_Stack:
    def __init__(self, *args):
        self.stack = [*args]

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self, index=-1):
        if not self.isEmpty():
            return self.stack.pop(index)

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)

    def isBalance(self):
        open = ['[', '{', '(']
        close = [']', '}', ')']
        if len(set(self.stack) - set(open) - set(close)) != 0:
            return False
        while self.size() > 1:
            if self.stack[0] in close:
                return False
            for index in range(0, self.size() - 1):
                if self.stack[index + 1] in open:
                    continue
                if open.index(self.stack[index]) == close.index(self.stack[index + 1]):
                    self.pop(index + 1)
                    self.pop(index)
                    break
                return False
        if self.isEmpty():
            return True
        else:
            return False

def isBalance2(string:str) -> bool:
    open = ['[', '{', '(']
    close = [']', '}', ')']
    stack = My_Stack()
    if len(set(tuple(string)) - set(open) - set(close)) != 0:
        return False # Если что-то кроме скобок
    for item in string:
        if item in open:
            stack.push(item)
            continue
        if (item in close) and (not stack.isEmpty()):
            index_c = close.index(item)
            index_o = open.index(stack.peek())
            if index_o == index_c:
                stack.pop()
            else:
                return False
        else:
            return False
    return stack.isEmpty()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stack1 = My_Stack()
    for i in input('Строка из скобок: '):
        stack1.push(i)
    print(stack1.isBalance())

    print(isBalance2(input('Строка из скобок: ')))

