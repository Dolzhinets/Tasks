class Stack:

    def __init__(self):
        self.__items=[]

    def push(self,items):
        self.__items.append(items)

    def pop(self):
        if len(self.__items) == 0:
            return None
        return self.__items.pop()

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.__items) > 0:
            return self.pop()
        else:
            raise StopIteration

    def get_stack(self):
        return self.__items
    
    
if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(25)
    stack.push(33)
    stack.push(48)
    stack.pop()
    for i in stack:
        print(i)

        