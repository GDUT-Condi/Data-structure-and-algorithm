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

    def pre_travel(self,node):
        if node is None:
            return
        print(node.elem)
        self.pre_travel(node.lchild)
        self.pre_travel(node.rchild)

if __name__ == '__main__':
    ll = Tree()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    ll.pre_travel(ll.root)
