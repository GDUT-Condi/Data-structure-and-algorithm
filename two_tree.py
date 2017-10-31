class Node():
    def __init__(self,elem=None,lchild=None,rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree():
    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur.lchild == None:
                cur.lchild = node
                return
            else:
                queue.append(cur.lchild)
            if cur.rchild == None:
                cur.rchild = node
                return
            else:
                queue.append(cur.rchild)

    def pre_travel(self,item):
        if item is None:
            return
        print(item.elem,end=' ')
        self.pre_travel(item.lchild)
        self.pre_travel(item.rchild)

    def middule_travel(self,item):
        if item is None:
            return
        self.middule_travel(item.lchild)
        print(item.elem,end=' ')
        self.middule_travel(item.rchild)

    def last_travel(self,item):
        if item is None:
            return
        self.last_travel(item.lchild)
        self.last_travel(item.rchild)
        print(item.elem, end=' ')

    def breath_travel(self,item):
        if item is None:
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            print(cur.elem,end=' ')
            if cur.lchild is not None:
                queue.append(cur.lchild)
            if cur.rchild is not None:
                queue.append(cur.rchild)

if __name__ == '__main__':
    ll = Tree()
    ll.add(0)
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    ll.add(6)
    ll.add(7)
    ll.add(8)
    ll.add(9)
    ll.breath_travel(ll.root)
    print('\n')
    ll.pre_travel(ll.root)
    print('\n')
    ll.middule_travel(ll.root)
    print('\n')
    ll.last_travel(ll.root)


