class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = node()

    def append(self, data):
        newNode = node(data)
        cur =  self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode

    def length(self):
        cur =  self.head
        count = 0
        while cur.next != None:
            count += 1
            cur = cur.next
        return count
    
    def display(self):
        elements = []
        cur = self.head
        while cur.next != None:
            elements.append(cur.data)
            cur = cur.next
        print(elements)


def userInput():
    isLoop = True

    while isLoop:
        ll = linkedlist()

        def display():
            ll.display()

        switch = {
            1: display
        }
        argument = int(input('Enter argumet'))
        executableFun = switch.get(argument, None)
        if argument == None:
            break
        executableFun()


userInput()
        
    
