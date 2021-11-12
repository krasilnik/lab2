#Task 4.
#Create a class BINARY TREE that contains background information of product prices (product code, price of 1 product).
#The tree is sorted by product codes. From the keyboard enter data on the number of products in the format:
#product code, number of products. Using a tree, find the cost of products (cost = quantity * price of one product).



class Node:

    def __init__(self, code, number, price, left=None, right=None):
        self.left = left
        self.right = right
        self.code = code
        self.number = number
        self.price = price

    def final_price(self, current):
        if not current.left and not current.right:
            return current.number * current.price
        elif current.left and current.right:
            return current.number * current.price + self.final_price(current.left) + self.final_price(current.right)
        elif current.left and not current.right:
            return current.number * current.price + self.final_price(current.left)
        elif current.right and not current.left:
            return current.number * current.price + self.final_price(current.right)


class BinaryTree:

    def __init__(self):
        self.root = None

    def insertion(self, code, number, price):
        if not isinstance(code, int):
            raise TypeError("Code has incorrect type for inserting!")
        if not isinstance(number, int):
            raise TypeError("Number has incorrect type for inserting!")
        if not isinstance(price, int):
            raise TypeError("Price has incorrect type for inserting!")
        if not self.root:
            self.root = Node(code, number, price)
        else:
            current = self.root
            while True:
                if code < current.code:
                    if not current.left:
                        current.left = Node(code, number, price)
                        return current.left
                    else:
                        current = current.left
                elif code > current.code:
                    if not current.right:
                        current.right = Node(code, number, price)
                        return current.right
                    else:
                        current = current.right
                else:
                    raise ValueError("Detected an incorrect code!")


tree = BinaryTree()
tree.insertion(3, 7, 4)
tree.insertion(8, 1, 2)
tree.insertion(2, 1, 5)
tree.insertion(5, 7, 2)
tree.insertion(1, 9, 7)
tree.insertion(4, 6, 2)
tree.insertion(6, 1, 2)
tree.insertion(7, 3, 1)
print('The cost of all products : ', tree.root.final_price(tree.root))
    