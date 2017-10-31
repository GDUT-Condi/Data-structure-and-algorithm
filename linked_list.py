class Node():
    def __init__(self,item):
        self.item = item
        self.next = None

class linked_list():
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.item,end=',')
            cur = cur.next

    def length(self):
        count = 0
        cur = self.__head
        while cur != None :
            count += 1
            cur = cur.next
        return count

if __name__ == '__main__':
    ll = linked_list()
    print(ll.is_empty())
    ll.append(1)
    ll.append(2)
    print(ll.is_empty())
    print(ll.travel())
    print(ll.length())