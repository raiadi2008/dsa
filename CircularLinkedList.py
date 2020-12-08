class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_next_node(self, next_node):
        self.next_node = next_node


class CircularLinkedList:
    def __init__(self, node=None):
        self.head_node = node
        self.tail_node = None
        if self.head_node == None:
            return
        cur_node = self.head_node
        while cur_node.get_next_node():
            cur_node = cur_node.get_next_node()
        self.tail_node = cur_node
        self.tail_node.set_next_node(self.head_node)

    def traverse_list(self):
        cur_node = self.head_node
        while cur_node:
            print(cur_node.get_value())
            cur_node = cur_node.get_next_node()
            if cur_node is self.head_node:
                break

    def insert_beginning(self, value):
        if self.head_node == None:
            self.head_node = Node(value)
            self.tail_node = self.head_node
            self.tail_node.set_next_node(self.head_node)
        else:
            self.head_node = Node(value, self.head_node)
            self.tail_node.set_next_node(self.head_node)

    def insert_after(self, key, value):
        if self.head_node != None:
            cur_node = self.head_node
            while cur_node:
                if cur_node.get_value() == key:
                    cur_node.set_next_node(
                        Node(value, cur_node.get_next_node()))
                    if cur_node is self.tail_node:
                        self.tail_node = cur_node.get_next_node()
                    break
                else:
                    cur_node = cur_node.get_next_node()
                if cur_node is self.head_node:
                    break

    def insert_before(self, key, value):
        if self.head_node == None:
            # since there is no node in the list you can't add after
            return
        if self.head_node.get_value() == key:
            self.head_node = Node(value, self.head_node)
            self.tail_node.set_next_node(self.head_node)
        else:
            cur_node = self.head_node
            while cur_node:
                if cur_node.get_next_node() is self.head_node:
                    break
                if cur_node.get_next_node().get_value() == key:
                    cur_node.set_next_node(
                        Node(value, cur_node.get_next_node()))
                    break
                else:
                    cur_node = cur_node.get_next_node()

    def delete_node(self, key):
        if self.head_node:
            if self.head_node.get_value() == key:
                if self.head_node is self.head_node.get_next_node():
                    self.head_node = None
                    self.tail_node = None
                else:
                    self.head_node = self.head_node.get_next_node()
                    self.tail_node.set_next_node(self.head_node)
            else:
                cur_node = self.head_node
                while cur_node:
                    if cur_node.get_next_node().get_value() == key:
                        cur_node.set_next_node(
                            cur_node.get_next_node().get_next_node())
                        break
                    else:
                        cur_node = cur_node.get_next_node()
                    if cur_node.get_next_node() is self.head_node:
                        break


if __name__ == "__main__":
    pass

    '''
    a = Node(4)
    b = Node(5,a)
    c = Node(12,b)
    lst = CircularLinkedList(c)
    lst.delete_node(5)
    lst.delete_node(4)
    lst.delete_node(12)
    lst.insert_after(11,55)
    lst.insert_before(33,51)
    lst.insert_beginning(7)
    lst.insert_after(7,54)
    lst.delete_node(7)
    lst.insert_before(54,34)
    lst.insert_before(54,11)
    lst.insert_after(54,200)
    lst.insert_after(34,4)
    lst.insert_before(34,1)
    lst.insert_before(200,111)
    lst.traverse_list()
    '''
