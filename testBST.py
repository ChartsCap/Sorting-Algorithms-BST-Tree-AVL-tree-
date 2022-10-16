"""Test program for Binary Search Tree implementation"""

import random
import sys
import pylint.lint

from BST import BST

LIST_SIZE = 50
LINT_THRESHOLD = 8.0

TEST_LIST = [0, 5, 3, 41, 61, -6, -1, -71, -12, -51, 1, 51, -15]
TEST1 = [3, 2, 1, 4, 5, 6, 7]
TEST2 = [16, 15, 14, 13, 12, 11, 10, 8, 9]
DESC_DATA = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
MIN_MAX_DATA = [45, 20, 36, 88, 10, 100, 50, 90, 96, 120, 25]


FUNC_LIST = ['insert', 'remove', 'find', 'pre_order_walk', 'in_order_walk',
             'post_order_walk', 'get_tree_height', 'get_min', 'get_max']


def check_functions():
    """Checks if required methods are implemented in class BST"""
    the_tree = BST()
    print(f"\nTesting if the class has the required methods. \n{FUNC_LIST}\n")

    for func in FUNC_LIST:
        if not hasattr(the_tree, func):
            print(f"The class does not have a {func}() method.")
            sys.exit(1)
    print("The class has the required methods.\n")
    return True


def create_test_list():
    return random.sample(range(-5*LIST_SIZE, 5*LIST_SIZE), LIST_SIZE)


def test_one_leg():
    print('Test to insert descending data')
    print(f'The test inserts numbers from {DESC_DATA}')
    tree = BST()
    for number in DESC_DATA:
        tree.insert(number)
    height = tree.get_tree_height()
    correct_height = len(DESC_DATA) - 1
    if height != correct_height:
        print(
            f'Error: After inserting the data tree height is {height} but it should be {correct_height}')
        sys.exit(1)
    print('Test to insert ascending data')
    asc_data = list(reversed(DESC_DATA))
    print(f'The test inserts numbers from {asc_data}')
    tree = BST()
    for number in asc_data:
        tree.insert(number)
    height = tree.get_tree_height()
    if height != correct_height:
        print(
            f'Error: After inserting the data tree height is {height} but it should be {correct_height}')
        sys.exit(1)
    print("Your BST handles sorted data data correctly\n")


def test_find():
    print('Test find() method')
    print(f'The test inserts numbers from {TEST_LIST}')
    tree = BST()
    for number in TEST_LIST:
        tree.insert(number)
    for number in TEST_LIST:
        if not tree.find(number):
            print(f'Error: Could not find the number {number} in your tree')
            sys.exit(1)
    if tree.find(-72):
        print('Error: Found the number (-72) in your tree, but it should not be there')
        sys.exit(1)
    print('Your method find() seems to work correctly!\n')


def test_get_height():
    print('Testing method get_tree_height')

    print('Creating empty tree')
    tree = BST()
    height = tree.get_tree_height()
    if height != -1:
        print(
            f'Error: Your method get_tree_height returns {height} for an empty tree, ',
            'but it should be -1')
        sys.exit(1)
    tree.insert(1)
    height = tree.get_tree_height()
    if height != 0:
        print(
            f'Error: Your method get_tree_height returns {height} for a tree with one node, ',
            'but it should be 0')
        sys.exit(1)
    del tree
    tree = BST()
    print(f'The test inserts numbers from {TEST1}')
    for number in TEST1:
        tree.insert(number)
    height = tree.get_tree_height()
    if height != 4:
        print(
            f'Error: Your method get_tree_height returns {height} after inserting',
            f' the elements {TEST1} but it should be 4')
        sys.exit(1)
    for number in TEST2:
        tree.insert(number)
    height = tree.get_tree_height()
    if height != 13:
        print(
            f'Error: Your method get_tree_height returns {height} after inserting',
            f' additional elements from {TEST2} but it should be 13')
        sys.exit(1)
    print("Your get_tree_height() method seems to work correctly.\n")


def walk_tests():
    PRE_LIST = [45, 20, 10, 36, 25, 88, 50, 100, 90, 96, 120]
    IN_LIST = [10, 20, 25, 36, 45, 50, 88, 90, 96, 100, 120]
    POST_LIST = [10, 25, 36, 20, 50, 96, 90, 120, 100, 88, 45]
    print('Basic testing on walk methods ...')
    tree = BST()
    walk = tree.pre_order_walk()
    if walk != []:
        print(
            f'Error: Your method pre_order_walk returns {walk} for an empty tree, ',
            'but it should be an empty list.')
        sys.exit(1)
    walk = tree.in_order_walk()
    if walk != []:
        print(
            f'Error: Your method in_order_walk returns {walk} for an empty tree, ',
            'but it should be an empty list.')
        sys.exit(1)
    walk = tree.post_order_walk()
    if walk != []:
        print(
            f'Error: Your method post_order_walk returns {walk} for an empty tree, ',
            'but it should be an empty list.')
        sys.exit(1)
    print(f'Inserting elements {MIN_MAX_DATA}')
    for number in MIN_MAX_DATA:
        tree.insert(number)
    walk = tree.pre_order_walk()
    if walk != PRE_LIST:
        print(
            f'Error: Your method pre_order_walk returns {walk}, but it should be {PRE_LIST}')
        sys.exit(1)
    walk = tree.in_order_walk()
    if walk != IN_LIST:
        print(
            f'Error: Your method post_order_walk returns {walk}, but it should be {IN_LIST}')
        sys.exit(1)
    walk = tree.post_order_walk()
    if walk != POST_LIST:
        print(
            f'Error: Your method post_order_walk returns {walk}, but it should be {POST_LIST}')
        sys.exit(1)
    print('Walk orders are OK\n')


def test_duplicates():
    print('Try to insert the same number multiple times in empty tree')
    tree = BST()
    for i in range(10):
        tree.insert(1)
    tree_size = len(tree.in_order_walk())
    if tree_size != 1:
        print('Error: Not handles correctly. Tree should only have one node')
    del tree

    item_list = create_test_list()
    print(f'Inserts {len(item_list)} random numbers.')
    tree = BST()

    for item in item_list:
        tree.insert(item)
    dup_list = random.sample(item_list, 5)
    print(f'\nTrying to insert {len(dup_list)} duplicates')
    tree_size = len(tree.in_order_walk())
    for item in dup_list:
        tree.insert(item)
        if len(tree.in_order_walk()) != tree_size:
            print(
                f'The element {item} is already in the tree, duplicate values not handled correctly!')
            sys.exit(1)
    print('Your tree handles duplicates correctly, all duplicates are ignored!\n')


def min_max_test():
    test_tree = BST()
    print(f'The test inserts numbers from {MIN_MAX_DATA}')
    for number in MIN_MAX_DATA:
        test_tree.insert(number)
    the_min = test_tree.get_min()
    the_max = test_tree.get_max()
    if the_min != min(MIN_MAX_DATA):
        print(f'Error: The get_min() method returns {the_min}, ',
              f'while it should be {min(MIN_MAX_DATA)}')
        sys.exit(1)
    if the_max != max(MIN_MAX_DATA):
        print(f'Error: The get_max() method returns {the_max}, ',
              f'while it should be {max(MIN_MAX_DATA)}')
        sys.exit(1)
    print('Metods get_min() and get_max() works for the tested list')


def first_remove_test():
    DATA = [45, 20, 36, 88, 10, 100, 50, 90, 96, 120, 25, 5, 60]
    print(
        f'Test with inserting from {DATA} to empty BST, thereafter removing certain nodes ...')
    tree = BST()
    for number in DATA:
        tree.insert(number)
    tree.remove(5)
    nr_of_nodes = len(DATA) - 1
    if len(tree.in_order_walk()) != nr_of_nodes:
        print('Not correct nr of nodes after removing a leaf node (5)')
        sys.exit(1)
    
    tree.remove(36)
    nr_of_nodes -= 1
    if len(tree.in_order_walk()) != nr_of_nodes:
        print('Not correct nr of nodes after removing a node with only left child (36)')
        sys.exit(1)
    
    tree.remove(50)
    nr_of_nodes -= 1
    if len(tree.in_order_walk()) != nr_of_nodes:
        print('Not correct nr of nodes after removing a node with only right child (50)')
        sys.exit(1)
    
    tree.remove(88)
    nr_of_nodes -= 1
    if len(tree.in_order_walk()) != nr_of_nodes:
        print('Not correct nr of nodes after removing a node with two children (88)')
        sys.exit(1)

    print('Try to remove a node that is not there (68), ...')
    tree.remove(68)
    if len(tree.in_order_walk()) != nr_of_nodes:
        print('remove() method does not handle nodes that are not in the tree correctly')
        sys.exit(1)


def second_remove_test():
    print(
        f'Test with inserting from {MIN_MAX_DATA} to empty BST, thereafter removing certain nodes ...')
    tree = BST()
    for number in MIN_MAX_DATA:
        tree.insert(number)
    remove_list = random.sample(MIN_MAX_DATA, len(MIN_MAX_DATA))
    for number in remove_list:
        tree.remove(number)
    nr_of_nodes = len(tree.in_order_walk())
    if nr_of_nodes != 0:
        print(
            f'Error: Tree not empty after removing all elements, nr of nodes = {nr_of_nodes} but should be 0 ')
        sys.exit(1)

    for number in MIN_MAX_DATA:
        tree.insert(number)
    tree.remove(96)
    height = tree.get_tree_height()
    if height != 3:
        print(
            f'Error: Not correct height after removing a leaf that effects the height, height = {height} but should be 3 ')
        sys.exit(1)

    tree.remove(50)
    tree.remove(45)
    tree.remove(88)
    tree.remove(20)
    height = tree.get_tree_height()
    if height != 2:
        print(
            f'Error: Not correct height after removing nodes (50), (45), (88), and (20), height = {height} but should be 2 ')
        sys.exit(1)

    print('Nodes seems to be removed correctly!\n')


def final_insert_and_height_tests(nr):
    try:
        file = open(f'Filer_och_Tester_LabB/Testpaket_LabB/unique{nr}.txt', 'r')
    except FileNotFoundError:
        print(f'Error: File {nr}.txt could not be found in current folder')
        sys.exit(1)
    data_list = []
    for line in file:
        if line != '':
            data_list.append(int(line))
    file.close()
    bst = BST()
    for item in data_list:
        bst.insert(item)
    if nr == 127 and bst.get_tree_height() != 14 or\
            nr == 147 and bst.get_tree_height() != 16 or\
            nr == 167 and bst.get_tree_height() != 14 or\
            nr == 187 and bst.get_tree_height() != 14 or\
            nr == 207 and bst.get_tree_height() != 13:
        print(
            f'Not correct height for {nr} elements, got {bst.get_tree_height()}\n')
        sys.exit(1)


def test_code_quality():
    print("\nTesting code quality by lint score .....\n")
    run = pylint.lint.Run(["BST.py"], do_exit=False)
    score = run.linter.stats["global_note"]
    if score < LINT_THRESHOLD:
        print(f"The pylint score is only {score}, at least 8.0 required")
        sys.exit(1)
    print("Lint score OK")


if __name__ == '__main__':
    check_functions()
    test_find()
    test_get_height()
    test_one_leg()
    print('Testing different walk strategies through the tree...\n',
          'NOTE: Errors can come from an incorrect insertion, ',
          'you can not be sure the walk methods are to blame')

    walk_tests()

    test_duplicates()
    min_max_test()

    first_remove_test()
    second_remove_test()
    print('Final tests with data from files...')
    for i in range(5):
        final_insert_and_height_tests(127 + i*20)
    print('\nAll behavioral tests passed successfully!')

    test_code_quality()
    print("\nCongratulations, all tests passed successfully!")
