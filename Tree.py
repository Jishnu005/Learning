class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def insert_child(self, child):
        self.children.append(child)
        child.parent = self

    def level(self):
        c = 0
        p = self.parent
        while p:
            c+=1
            p = p.parent
        return c
    
    def print(self):
        p = " "*self.level()*2
        print(p+"-->" if self.parent else "", end="")
        print(self.data)
        for c in self.children:
            if c is None:
                return
            c.print()

mobile = TreeNode("Mobile")

samsung = TreeNode("Samsung")
mobile.insert_child(samsung)

s22 = TreeNode("S22 Ultra")
samsung.insert_child(s22)

a2 = TreeNode("Galaxy A2")
samsung.insert_child(a2)


apple = TreeNode("Apple")
mobile.insert_child(apple)

iphone15 = TreeNode("Iphone 15 Pro")
apple.insert_child(iphone15)

iphonex = TreeNode("Iphone X")
apple.insert_child(iphonex)


oppo = TreeNode("Oppo")
mobile.insert_child(oppo)

mobile.print()