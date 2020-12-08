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


class LinkedList:
    def __init__(self, value=None):
        self.head_node = value

    def insert_beginning(self, value=None):
        self.head_node = Node(value, self.head_node)

    def insert_end(self, value=None):
        cur_node = self.head_node
        while cur_node:
            if cur_node.get_next_node() == None:
                cur_node.set_next_node(Node(value))
                break
            else:
                cur_node = cur_node.get_next_node()

    def traverse_list(self):
        cur_node = self.head_node
        while cur_node:
            print(str(cur_node.get_value()))
            cur_node = cur_node.get_next_node()

    def insert_after(self, key, value):
        cur_node = self.head_node
        while cur_node:
            if cur_node.get_value() == key:
                cur_node.set_next_node(Node(value, cur_node.get_next_node()))
                break
            else:
                cur_node = cur_node.get_next_node()

    def insert_before(self, key, value):
        if self.head_node:
            if self.head_node.get_value() == key:
                self.head_node = Node(value, self.head_node)
            else:
                cur_node = self.head_node
                while cur_node.get_next_node():
                    if cur_node.get_next_node().get_value() == key:
                        cur_node.set_next_node(
                            Node(value, cur_node.get_next_node()))
                        break
                    else:
                        cur_node = cur_node.get_next_node()

    def delete_node(self, key):
        if self.head_node:
            if self.head_node.get_value() == key:
                self.head_node = self.head_node.get_next_node()
            else:
                cur_node = self.head_node
                while cur_node.get_next_node():
                    if cur_node.get_next_node().get_value() == key:
                        cur_node.set_next_node(
                            cur_node.get_next_node().get_next_node())
                        break
                    else:
                        cur_node = cur_node.get_next_node()

    def search_value(self, target_value):
        cur_node = self.head_node
        while cur_node:
            if cur_node.get_value() == target_value:
                return True
            else:
                cur_node = cur_node.get_next_node()
        return False


if __name__ == "__main__":
    a = Node(4)
    b = Node(6, a)
    c = Node(7, b)
    d = Node(13, c)
    ll = LinkedList(d)
    print("printing list")
    ll.traverse_list()
    ll.delete_node(4)
    print("deleting 4 and printing list")
    ll.traverse_list()
    ll.insert_beginning(5)
    ll.insert_end(9)
    print("inserted in begining and in end")
    ll.traverse_list()
    ll.insert_after(9, 16)
    ll.insert_after(13, 122)
    ll.insert_after(11, 124)
    print("traversing again")
    ll.traverse_list()
    ll.insert_before(5, 155)
    ll.insert_before(16, 95)
    ll.insert_before(0, 0)
    print("travesing again")
    ll.traverse_list()
    if ll.search_value(1111):
        print("found 1111 in list")
    else:
        print("did not found 1111 in list")

    if ll.search_value(9):
        print("found 9 in the list")

    ll.delete_node(155)
    ll.delete_node(5)
    ll.delete_node(13)
    ll.delete_node(122)
    ll.delete_node(7)
    ll.delete_node(6)
    ll.delete_node(9)
    ll.delete_node(95)
    ll.delete_node(16)
    print("printing list after deleting all the elements")
    ll.traverse_list()
    ll.delete_node(54)
    ll.traverse_list()
    ll.insert_after(145, 53)
    ll.insert_before(65, 55)
    ll.traverse_list()
