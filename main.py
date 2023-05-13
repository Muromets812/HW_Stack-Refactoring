class Stack:

    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        if self.stack_list:
            return True
        else:
            return False

    def push(self, new_item):
        self.stack_list.append(new_item)
        return

    def pop(self):
        return self.stack_list.pop()

    def peek(self):
        try:
            up_item = self.stack_list[-1]
            return up_item
        except IndexError:
            return None

    def size(self):
        return len(self.stack_list)


if __name__ == "__main__":

    raw_str = input('Введите последовательность скобок: ')
    work_list = list(raw_str)
    my_stack = Stack()
    if len(work_list) % 2 != 0:
        print('Несбалансированно')
        exit()
    for item in work_list:
        if item == '{' or item == '(' or item == '[':
            my_stack.push(item)
        elif item == ')' and my_stack.peek() == '(':
            my_stack.pop()
        elif item == '}' and my_stack.peek() == '{':
            my_stack.pop()
        elif item == ']' and my_stack.peek() == '[':
            my_stack.pop()
        else:
            print('Несбалансированно')
            exit()
    if my_stack.size() > 0:
        print('Несбалансированно')
    else:
        print('Сбалансированно')
