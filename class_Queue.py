class Queue:

    def __init__(self):
        self.__items=[]

    def add(self,item):
        self.__items.insert(0,item)

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

    def get_queue(self):
        return self.__items
    
    
if __name__ == '__main__':
    queue = Queue()
    queue.add(11)
    queue.add(22)
    queue.add(33)
    queue.add(44)
    queue.pop()
    for i in queue:
        print(i)