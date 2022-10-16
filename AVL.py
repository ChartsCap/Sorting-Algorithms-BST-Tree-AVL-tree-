"""Modul implementerar AVL-träd"""

from collections import deque

class AVL:
    """Klass som definierar AVL träd"""
    class Node:
        """
        Klass som definierar en nod
        """
        def __init__(self, value: int):
            self.data = value
            self.height = 0
            self.left = None
            self.right = None
    
        def get_left(self):
            return self.left

        def get_right(self):
            return self.right

        def get_data(self):
            return self.data
        
        def get_height(self):
            return self.height
    
    def __init__(self):
        self._root = None
        self.node_id = 0  # ONLY USED WITHIN to_graphviz()!

    def insert(self, element):
        """
        Funktion som sätter in ny nod med värde element
        """
        if element is None:
            return
        else:
            self._root = self.insert_element(element, self._root)

    def remove(self, element):
        """
        Funktion som tar bort nod med värde element
        """
        if element is None:
            return
        else:
            self._root = self.remove_element(element, self._root)

    def find(self, element):
        """
        Funktion som returnerar True om element återfinns i trädet
        """
        current = self._root
        if current is None:
            return
        if current.data is element:
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
        res = []
        current = self._root
        queue = deque()
        if current is None:
            return res
        while queue or current:
            if current is not None:
                queue.append(current)
                current = current.left
            else:
                current = queue.pop()
                res.append(current.data)
                current = current.right
        return res

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
        if self._root is None:
            return -1
        else:
            return self._root.height

    def get_min(self):
        """
        Returnerar värdet av minsta elementet i trädet
        """
        min_node = self._root
        while min_node.left != None:
            min_node = min_node.left
        return min_node.data

    def get_max(self):
        """
        Returnerar värdet av största elementet i trädet
        """
        max_node = self._root
        while max_node.right != None:
            max_node = max_node.right
        return max_node.data

    def insert_element(self, element, root):
        """
        Funktion som sätter in nod med värde element
        """
        if root is None:
            return self.Node(element)
        if element is not root.data:
            if element < root.data:
                root.left = self.insert_element(element, root.left)
            else:
                root.right = self.insert_element(element, root.right)
        return self.insert_balance(element, root)

    def insert_balance(self, element, root):
        """
        Funktion som balanserar efter instättning
        """
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        balance = self.check_balance(root)
        if balance > 1 and element > root.left.data:
            root.left = self.rotation_left(root.left)
            return self.rotation_right(root)
        if balance < -1 and element < root.right.data:
            root.right = self.rotation_right(root.right)
            return self.rotation_left(root)
        if balance > 1 and element < root.left.data:
            return self.rotation_right(root)
        if balance < -1 and element > root.right.data:
            return self.rotation_left(root)
        return root

    def check_balance(self, root):
        """
        Returnerar balansen mellan vänster och höger barns höjd
        """
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_height(self, root):
        """
        Returnerar height
        """
        if root == None:
            return -1
        return root.height

    def remove_element(self, element, node):
        """
        Funktion som tar bort nod med värde element
        """
        if node == None:
            return node
        if element > node.data:
            node.right = self.remove_element(element, node.right)
        elif node.data > element:
            node.left = self.remove_element(element, node.left)
        else:
            if node.right == None:
                i = node.left
                node = None
                return i
            if node.left == None:
                i = node.right
                node = None
                return i
            i = self.min_node(node.right)
            node.data = i.data
            node.right = self.remove_element(node.data, node.right)
        if not node:
            return node
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        return self.remove_balance(node)

    def remove_balance(self, node):
        """
        Funktion som balanserar efter bort tagning
        """
        balance = self.check_balance(node)
        if (balance > 1) and self.check_balance(node.left) < 0:
            node.left = self.rotation_left(node.left)
            return self.rotation_right(node)
        if (balance < -1) and self.check_balance(node.right) > 0:
            node.right = self.rotation_right(node.right)
            return self.rotation_left(node)
        if (balance > 1) and self.check_balance(node.left) >= 0:
            return self.rotation_right(node)
        if (balance < -1) and self.check_balance(node.right) <= 0:
            return self.rotation_left(node)
        return node

    def min_node(self, current):
        """
        Returnerar minsta noden
        """
        while current.left:
            current = current.left
        return current

    def rotation_right(self, root):
        """
        Höger-rotation
        """
        current_left = root.left
        if root == None:
            return 0
        else:
            temp_node = current_left.right
            current_left.right = root
            root.left = temp_node
            root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
            current_left.height = max(self.get_height(current_left.left), self.get_height(current_left.right)) + 1
            return current_left

    def rotation_left(self, root):
        """
        Vänster-rotation
        """
        current_right = root.right
        if root == None:
            return 0
        else:
            temp_node = current_right.left
            current_right.left = root
            root.right = temp_node
            root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
            current_right.height = max(self.get_height(current_right.left), self.get_height(current_right.right)) + 1
            return current_right

    def to_graphviz_rec(self, data, current):
        my_node_id = self.node_id
        data += "\i" + str(my_node_id) + " [label=\"" + str(current.data) + "\"];\n"
        self.node_id += 1
        if current.left is not None:
            data += "\i" + str(my_node_id) + " -> " + str(self.node_id) + " [color=blue];\n"
            data = self.to_graphviz_rec(data, current.left)
        else:
            data += "\i" + str(self.node_id) + " [label=nill,style=invis];\n"
            data += "\i" + str(my_node_id) + " -> " + str(self.node_id) + " [style=invis];\n"

        self.node_id += 1
        if current.right is not None:
            data += "\i" + str(my_node_id) + " -> " + str(self.node_id) + " [color=red];\n"
            data = self.to_graphviz_rec(data, current.right)
        else:
            data += "\i" + str(self.node_id) + " [label=nill,style=invis];\n"
            data += "\i" + str(my_node_id) + " -> " + str(self.node_id) + " [style=invis];\n"

        return data

    def to_graphviz(self):
        data = ""
        if self._root is not None:
            self.node_id = 0
            data += "digraph {\n"
            data += "\tRoot [shape=plaintext];\n"
            data += "\i\"Root\" -> 0 [color=black];\n"
            data = self.to_graphviz_rec(data, self._root)
            data += "}\n"
        return data

def main():
    avl = AVL()

if __name__ == '__main__':
    main()
