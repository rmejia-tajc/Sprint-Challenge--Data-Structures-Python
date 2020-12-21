# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

# Questions:
# Only ints?
# Negative numbers?

# Observations
# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent


class BinarySearchTree:
    def __init__(self, value):  # We're just using value, so key is value
        self.value = value
        self.left = None
        self.right = None

    # * `insert` adds the input value to the binary search tree, adhering to the
    # rules of the ordering of elements in a binary search tree.
    # Need to traverse to find spot to insert
    def insert(self, value):  # current node is self

        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

###########  from lecture #############

        # #check if self.value is bigger or smaller than new value - left or right
        # if value > self.value:
        #   # we go right, then check if node exist
        #   if self.right == None:
        #     # if node does exist use recursion! call insert  on that node
        #     self.right = BinarySearchTree(value)
        #   else:
        #     #if node does not exist, then create a node there
        #     self.right.insert(value)
        # else:
        #   if self.left == None:
        #     self.left = BinarySearchTree(value)
        #   else:
        #     self.left.insert(value)

    # * `contains` searches the binary search tree for the input value,
    # returning a boolean indicating whether the value exists in the tree or not.
    # Start from root and traverse the tree
    # We can stop at the first instance of a value
    # We know it's not found if we get to a node that doesn't have children
    def contains(self, target):

        # if the target value is the same as the current node...
        if self.value == target:
            # then the target value does exists in the tree. Return True and it's done searching
            return True

        # if the target value is less than the current node...
        elif self.value > target:

            # if you can't go left - you're at the leaf (end of that branch)...
            if self.left == None:
                # then the target value does NOT exists in the tree. Return False and it's done searching
                return False
            # if you can go left...
            else:
                # then run the search over starting from the node left of the current node (recursion)
                return self.left.contains(target)

        # if the target value is more than the current node...
        else:
            # if you can't go right - you're at the leaf (end of that branch)...
            if self.right == None:
                # then the target value does NOT exists in the tree. Return False and it's done searching
                return False
            # if you can go right...
            else:
                # then run the search over starting from the node right of the current node (recursion)
                return self.right.contains(target)

###########  from lecture #############

        # if self.value == target:
        #   return True
        # else:
        #   if target < self.value:
        #     if not self.left:
        #       return False
        #     else:
        #       return self.left.contains(target)
        #   else:
        #     if not self.right:
        #       return False
        #     else:
        #       return self.right.contains(target)

    # * `get_max` returns the maximum value in the binary search tree.
    def get_max(self):

        # if you can't go right, you've reached the largest value...
        if self.right == None:
            # then return current node value. The search is over
            return self.value
        # if you can go right, there is a larger value...
        else:
            # then run the get_max search on the right child of the current node to continue to look for the maximum value (recursion)
            return self.right.get_max()

###########  from lecture recursion #############

        # if not self.right:
        #   return self.value
        # return self.right.get_max()

########## from lecture iterative #########

        # max_value = self.value
        # current = self

        # while current:
        #   max_value = current.value
        #   current = current.right

        # return max_value

    # * `for_each` performs a traversal of _every_ node in the tree, executing
    # the passed-in callback function on each tree node value. There is a myriad of ways to
    # perform tree traversal; in this case any of them should work.
    def for_each(self, cb):

        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
            


# DAY 2 Project -----------------------



    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_dft(self, node):
        # create an empty list to store the values
        items = []

        def traverse(n):
            # add current node's value to the list
            items.append(n.value)
            # if left child exists...
            if n.left:
                # run traverse function on the left child (recursion)
                traverse(n.left)
            # if right child exists...
            if n.right:
                # run traverse function on the right child (recursion)
                traverse(n.right)

        # run traverse function on the passed in node (starting point)
        traverse(node)

        # sort the list
        items.sort()
        # loop through the items in the list...
        for i in items:
            # print an item each pass
            print(i)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
