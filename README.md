# Welcome to GitHub Desktop!

This is your README. READMEs are where you can communicate what your project is and how to use it.

Write your name on line 6, save it, and then head back to GitHub Desktop.
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Linkedlist:
    def __init__(self):
        self.head = None

    def at_beginning(self, data):
        if self.head is None:
            self.head = Node(data, self.head, None)

        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None, itr)

    def print_forward(self):
        itr = self.head
        s = ''
        while itr:
            s+=str(itr.data)+'-->'
            itr = itr.next
        print(s)

    def last_itr(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
    
    def print_backward(self):
        itr = self.last_itr()
        s = ''
        while itr:
            s+=str(itr.data)+'-->'
            itr = itr.prev
        print(s)

    def insert_list(self, datalist):
        if self.head is None:
            for data in datalist:
                self.head = Node(data, None, None)
                break
        
            itr = self.last_itr()

            for data in datalist[1:]:
                itr.next = Node(data, None, itr)
                itr = itr.next
        else:
            itr = self.last_itr()

            for data in datalist:
                itr.next = Node(data, None, itr)
                itr = itr.next

    def find_using_index(self, index):
        count=0
        no_at_index = 0
        itr = self.head
        while itr.next:
            if count == index:
                no_at_index = str(itr.data)
                return no_at_index
            count+=1
            itr = itr.next

    def insert_at_index(self, index, data):
        if self.head is None:
            print("LinkedList is empty")
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next, itr)
                itr.next = node
                break
            count+=1
            itr = itr.next

    def remove_using_index(self, index):
        if self.head is None:
            print("LinkedList is empty")
            return
        
        count = 0
        itr = self.head
        while itr.next:
            if count == index-1:
                itr.next = itr.next.next
                itr.next.prev = itr
                break
            count += 1
            itr = itr.next

    def remove_value(self, data):
        if self.head is None:
            print("LinkedList is empty")
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                itr.next.prev = itr
                break
            itr = itr.next

    def length_of(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr = itr.next
        return count
    
    def check_value(self, data):
        itr = self.head
        while itr:
            if itr.data == data:
                print(True)
                break
            itr = itr.next
        else:
            print(False)
    
    def sort_linkedlist(self):
        itr = self.head
        while itr:
            itr2 = itr.next
            while itr2:
                if itr.data > itr2.data:
                    itr.data, itr2.data = itr2.data, itr.data
                itr2 = itr2.next
            itr = itr.next

l = Linkedlist()
# l.at_beginning(14)
l.insert_list([12,29, 53, 69])
l.insert_list([67, 46, 77, 99, 19])
# l.print_forward()
# l.print_backward()
# print(l.find_using_index(4))
# l.insert_at_index(6, 42)
# l.print_forward()
# l.remove_using_index(6)
# l.print_forward()
# l.remove_value(17)
# l.check_value(17)
l.print_forward()
# l.print_backward()
l.sort_linkedlist()
l.print_forward()