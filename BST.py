"""Module implementerar BST-träd"""
from ctypes import pointer
from lib2to3.pytree import Node
from re import I

class BST:
    """
    Klass som definierar binärt sökträd BST
    """
    class Node:
        """
        Klass som definierar en nod
        """
        def __init__(self):
            self.left = None
            self.right = None
            self.data = None

        def get_left(self):
            return self.left

        def get_right(self):
            return self.right

        def get_data(self):
            return self.data

    def __init__(self):
        self._root = None
        self.node_id = 0 # ONLY USED WITHIN to_graphviz()!

    def insert(self, element):
        """Insert node with value `element`."""
        new_node = self.Node()
        new_node.data = element
        if self._root is None:
            self._root = new_node
            return
        current = self._root
        while current is not None:
            parent = current
            if element < current.data:
                current = current.left
            elif element > current.data:
                current = current.right
            else:
                return

        if element < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

    def remove(self, element):
        """Delete a node with value `element`."""
        current = self._root
        parent = None
        while current is not None and current.data is not element:
            parent = current
            if element < current.data:
                current = current.left
            else:
                current = current.right
        if current is None:
            return
        if current.data == element:
            if current.left is None or current.right is None:   #Ta bort Nod med högst ett barn
                new_curr = None
                if current.left is None:
                    new_curr = current.right
                else:
                    new_curr = current.left
                if parent is None:
                    if current.right is None or current.left is None:
                        self._root=new_curr
                        current=None
                    return
                if current is parent.left:
                    parent.left = new_curr
                else:
                    parent.right = new_curr
                current = None

            else:    #Ta bort nod med två barn
                temp_node = current.right
                temp_parent = None
                while temp_node.left:
                    temp_parent = temp_node
                    temp_node  = temp_node.left
                if temp_parent is not None:
                    temp_parent.left = temp_node.right
                else:
                    current.right = temp_node.right
                current.data=temp_node.data
                temp_node=None

    def find(self, element):
        """
        Returnerar True om element återfinns i trädet
        """
        current = self._root
        if current is None:
            return False
        if current.data == element:
            return True
        while current.data is not element and current is not None:
            if current.data > element:
                if current.left is not None:
                    current = current.left
                else:
                    return False
            elif current.data < element:
                if current.right is not None:
                    current = current.right
                else:
                    return False
        if element == current.data:
            return True
        else:
            return False

    def pre_order_walk(self):
        """
        Returnerar lista med preordertraversering
        """
        result = []
        stack = []
        cur = self._root
        while cur or stack:
            while cur:
                stack.append(cur)
                result.append(cur.data)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return result

    def in_order_walk(self):
        """
        Returnerar lista med inordertraversering
        """
        ret = []
        root = self._root
        if not root:
            return ret
        stack = [root]
        current = None
        while stack:
            previous = current
            current = stack.pop()
            if previous is None or previous.left is current or previous.right is current:
                if current.right:
                    stack.append(current.right)
                stack.append(current)
                if current.left:
                    stack.append(current.left)
            else:
                ret.append(current.data)
        return ret

    def post_order_walk(self):
        """
        Returnerar lista med postordertraversering
        """
        ret = []
        root = self._root
        if not root:
            return ret
        stack = [root]
        current = None
        while stack:
            previous = current
            current = stack.pop()
            if previous and ((previous is current)
            or (previous is current.left)
            or (previous is current.right)):
                ret.append(current.data)
            else:
                stack.append(current)
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)

        return ret

    def get_tree_height(self):
        """
        Returnerar trädets höjd
        Returnerar -1 för tomt träd
        """
        root = self._root
        if root is None: 
            return -1
        queue = []
        queue.append(root) 
        height = -1 
        while(True):
            amnt_nodes = len(queue)
            if amnt_nodes == 0 : 
                return height
            height += 1
            while amnt_nodes > 0:
                node = queue[0]
                queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                amnt_nodes -= 1

    def get_min(self):
        """
        Returnerar värdet av minsta elementet i trädet
        """
        min_node = self._root
        while min_node.left is not None:
            min_node = min_node.left
        return min_node.data

    def get_max(self):
        """
        Returnerar värdet av största elementet i trädet
        """
        max_node = self._root
        while max_node.right is not None:
            max_node = max_node.right
        return max_node.data

    def to_graphviz_rec(self, data, current):
        my_node_id = self.node_id
        data += "\t" + str(my_node_id) + " [label=\"" + str(current.data) + "\"];\n" ;
        self.node_id += 1
        if current.left is not None:
            data += "\t" +  str(my_node_id) + " -> " + str(self.node_id) + " [color=blue];\n";
            data = self.to_graphviz_rec(data, current.left)
        else:
            data += "\t" + str(self.node_id) + " [label=nill,style=invis];\n";
            data += "\t" +  str(my_node_id) + " -> " + str(self.node_id) + " [style=invis];\n";

        self.node_id += 1
        if current.right is not None:
            data += "\t" +  str(my_node_id) + " -> " + str(self.node_id) + " [color=red];\n";
            data = self.to_graphviz_rec(data, current.right);
        else:
            data += "\t" + str(self.node_id) + " [label=nill,style=invis];\n";
            data += "\t" +  str(my_node_id) + " -> " + str(self.node_id) + " [style=invis];\n";

        return data

    def to_graphviz(self):
        data = ""
        if self._root is not None:
            self.node_id = 0
            data += "digraph {\n"
            data += "\tRoot [shape=plaintext];\n"
            data += "\t\"Root\" -> 0 [color=black];\n"
            data = self.to_graphviz_rec(data, self._root)
            data += "}\n"
        return data

def main():
    bst = BST()
    print(bst.to_graphviz())

if __name__ == '__main__':
    main()
