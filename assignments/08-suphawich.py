class Node:
    def __init__(self, val):
        self.p = None
        self.l = None
        self.r = None
        self.v = val

    def __str__(self):
        l = self.l.v if self.l else 'None'
        r = self.r.v if self.r else 'None'
        p = self.p.v if self.p else 'None'
        return f"Node: {self.v}, left: {l}, right: {r}, parent: {p}"

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        child = Node(val)
        child.p = node
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = child
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = child

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)

    def deleteTree(self):
        self.root = None

    def delete(self, v):
        z = self.find(v)
        if z.l is None:
            self.transplant(z, z.r)
        elif z.r is None:
            self.transplant(z, z.l)
        else:
            y = self.minimum(z.r)
            if y.p != z:
                self.transplant(y, y.r)
                y.r = z.r
                y.r.p = y
            self.transplant(z, y)
            y.l = z.l
            y.l.p = y

    def transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u == u.p.l:
            u.p.l = v
        else:
            u.p.r = v
        if v is not None:
            v.p = u.p
    
    def minimum(self, node=None):
        if node is None:
            node = self.root
        if node.l is None:
            return node
        return self.minimum(node.l)

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
            print('\r') # <-- prevent % after end of printing

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(node.v, end=" ")
            self._printTree(node.r)


"""
        3
    0       4
      2       8
"""
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print(tree.find(4))
tree.delete(4)
tree.printTree()
print(tree.find(4))
print(tree.find(8))
# tree.printTree()