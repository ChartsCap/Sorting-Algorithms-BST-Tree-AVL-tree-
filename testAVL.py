"""Test program for AVL Tree implementation"""

import random
import sys
import pylint.lint

from AVL import AVL

LIST_SIZE = 50
LINT_THRESHOLD = 8.0

TEST_LIST = [0, 5, 3, 41, 61, -6, -1, -71, -12, -51, 1, 51, -15]
TEST1 = [3, 2, 1, 4, 5, 6, 7]
TEST2 = [16, 15, 14, 13, 12, 11, 10, 8, 9]


FUNC_LIST = ['insert', 'remove', 'find', 'pre_order_walk', 'in_order_walk',
             'post_order_walk', 'get_tree_height', 'get_min', 'get_max']


def check_functions(the_tree):
    """Checks if required methods are implemented in class AVL"""

    print(f"\nTesting if the class has the required methods. \n{FUNC_LIST}\n")

    for func in FUNC_LIST:
        if not hasattr(the_tree, func):
            print(f"The class does not have a {func}() method.")
            sys.exit(1)
    print("The class has the required methods.\n")
    return True


def create_test_list():
    return random.sample(range(-5*LIST_SIZE, 5*LIST_SIZE), LIST_SIZE)


def test_basic_rotation():
    DATA1 = [3, 2, 1]
    DATA2 = [3, 1, 2]
    IN = [1, 2, 3]
    POST = [1, 3, 2]
    PRE = [2, 1, 3]
    TESTS = [DATA1, IN, POST, DATA2]

    print('Testing that all basic rotations are correct')
    for test in TESTS:
        tree = AVL()
        for number in test:
            tree.insert(number)
        if tree.pre_order_walk() != PRE:
            print(
                f'Error: Preorder walk after inserting {test} is not correct, it gives {tree.pre_order_walk()}, but should be{PRE}')
            sys.exit(1)
        if tree.in_order_walk() != IN:
            print(
                f'Error: Inorder walk after inserting {test} is not correct, it gives {tree.in_order_walk()}, but should be{IN}')
            sys.exit(1)
        if tree.post_order_walk() != POST:
            print(
                f'Error: Postorder walk after inserting {test} is not correct, it gives {tree.post_order_walk()}, but should be{POST}')
            sys.exit(1)
    print("All basic rotations seem correct\n")


def test_find():
    print('Test find() method')
    print(f'The test inserts numbers from {TEST_LIST}')
    tree = AVL()
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
    tree = AVL()
    height = tree.get_tree_height()
    if height != -1:
        print(
            f'Error: Your method get_tree_height returns {height} for en empty tree, ',
            'but it should be -1')
        sys.exit(1)
    print(f'The test inserts numbers from {TEST1}')
    for number in TEST1:
        tree.insert(number)
    height = tree.get_tree_height()
    if height != 2:
        print(
            f'Error: Your method get_tree_height returns {height} after inserting',
            f' the elements {TEST1} but it should be 2')
        sys.exit(1)
    for number in TEST2:
        tree.insert(number)
    height = tree.get_tree_height()
    if height != 4:
        print(
            f'Error: Your method get_tree_height returns {height} after inserting',
            f' additional elements from {TEST2} but it should be 4')
        sys.exit(1)
    print("Your get_tree_height() method seems to work correctly.\n")


def test_pre_order_walk():
    STEP1 = [4, 2, 1, 3, 6, 5, 7]
    STEP2 = [7, 4, 2, 1, 3, 6, 5, 13, 11, 9, 8, 10, 12, 15, 14, 16]
    print('Testing method pre_order_walk() ...')
    tree = AVL()
    walk = tree.pre_order_walk()
    if walk != []:
        print(
            f'Error: Your method pre_order_walk returns {walk} for an empty tree, ',
            'but it should be an empty list.')
        sys.exit(1)
    print(f'Inserting elements {TEST1}')
    for number in TEST1:
        tree.insert(number)
    walk = tree.pre_order_walk()
    if walk != STEP1:
        print(
            f'Error: Your method pre_order_walk returns {walk}, but it should be {STEP1}')
        sys.exit(1)
    print('Walk order is OK')
    print(f'Inserting elements additional elements {TEST2}')
    for number in TEST2:
        tree.insert(number)
    walk = tree.pre_order_walk()
    if walk != STEP2:
        print(
            f'Error: Your method pre_order_walk returns {walk}, but it should be {STEP2}')
        sys.exit(1)
    print('Your method pre_order_walk seems to be correct!\n')


def test_in_order_walk():
    STEP1 = [1, 2, 3, 4, 5, 6, 7]
    STEP2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    print('Testing method in_order_walk() ...')
    tree = AVL()
    walk = tree.in_order_walk()
    if walk != []:
        print(
            f'Error: Your method in_order_walk returns {walk} for an empty tree, ',
            'but it should be an empty list.')
        sys.exit(1)
    print(f'Inserting elements {TEST1}')
    for number in TEST1:
        tree.insert(number)
    walk = tree.in_order_walk()
    if walk != STEP1:
        print(
            f'Error: Your method in_order_walk returns {walk}, but it should be {STEP1}')
        sys.exit(1)
    print('Walk order is OK')
    print(f'Inserting elements additional elements {TEST2}')
    for number in TEST2:
        tree.insert(number)
    walk = tree.in_order_walk()
    if walk != STEP2:
        print(
            f'Error: Your method in_order_walk returns {walk}, but it should be {STEP2}')
        sys.exit(1)
    print('Your method in_order_walk seems to be correct!\n')


def test_post_order_walk():
    STEP1 = [1, 3, 2, 5, 7, 6, 4]
    STEP2 = [1, 3, 2, 5, 6, 4, 8, 10, 9, 12, 11, 14, 16, 15, 13, 7]
    print('Testing method post_order_walk() ...')
    tree = AVL()
    walk = tree.post_order_walk()
    if walk != []:
        print(
            f'Error: Your method post_order_walk returns {walk} for an empty tree, ',
            'but it should be an empty list.')
        sys.exit(1)
    print(f'Inserting elements {TEST1}')
    for number in TEST1:
        tree.insert(number)
    walk = tree.post_order_walk()
    if walk != STEP1:
        print(
            f'Error: Your method post_order_walk returns {walk}, but it should be {STEP1}')
        sys.exit(1)
    print('Walk order is OK')
    print(f'Inserting elements additional elements {TEST2}')
    for number in TEST2:
        tree.insert(number)
    walk = tree.post_order_walk()
    if walk != STEP2:
        print(
            f'Error: Your method post_order_walk returns {walk}, but it should be {STEP2}')
        sys.exit(1)
    print('Your method post_order_walk seems to be correct!\n')


def test_duplicates(tree, item_list):
    print(f'Inserts {len(item_list)} random numbers.')
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
    print('Your tree handles duplicates correctly, all duplicates are ignored!')


def specific_min_max_test():
    test_tree = AVL()
    print(f'The test inserts numbers from {TEST_LIST}')
    for number in TEST_LIST:
        test_tree.insert(number)
    the_min = test_tree.get_min()
    the_max = test_tree.get_max()
    if the_min != min(TEST_LIST):
        print(f'Error: The get_min() method returns {the_min}, ',
              'while it should be {min(TEST_LIST)}')
        sys.exit(1)
    if the_max != max(TEST_LIST):
        print(f'Error: The get_max() method returns {the_max}, ',
              'while it should be {max(TEST_LIST)}')
        sys.exit(1)
    print('Metods get_min() and get_max() works for the tested list')


def test_min_max(tree, base_list):
    print('\nTesting get_min() and get_max() on values from large random list')

    try:
        the_min = tree.get_min()
        if the_min == min(base_list):
            print(f'Correct min ({the_min})')
        else:
            print(
                f'Error: Calculated Min is {the_min}, while it should be {min(base_list)}')
            sys.exit(1)
    except:
        print('Error: in calculating min value')
        sys.exit(1)

    try:
        the_max = tree.get_max()
        if the_max == max(base_list):
            print(f'Correct max ({the_max})')
        else:
            print(
                f'Error: Calculated Max is {the_max}, while it should be {max(base_list)}')
            sys.exit(1)
    except:
        print('Error: in calculating max value')
        sys.exit(1)
    return [the_min, the_max]


def test_remove():
    PRE_STEP1 = [7, 4, 2, 1, 3, 6, 5, 13, 9, 8, 11, 10, 15, 14, 16]
    POST_STEP1 = [1, 3, 2, 5, 6, 4, 8, 10, 11, 9, 14, 16, 15, 13, 7]
    PRE_STEP2 = [7, 4, 2, 1, 3, 6, 5, 13, 10, 9, 11, 15, 14, 16]
    POST_STEP2 = [1, 3, 2, 5, 6, 4, 9, 11, 10, 14, 16, 15, 13, 7]
    TO_REMOVE = [1, 3, 2, 5, 6, 4, 9, 11, 10, 14, 16, 15, 13, 7]
    HEIGHT_CHECK = [3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 0, -1]

    tree = AVL()
    print(f'Insert elements{TEST1 + TEST2} in empty tree.')
    for item in (TEST1 + TEST2):
        tree.insert(item)
    print('Removing item (12) ...')
    tree.remove(12)
    pre_walk = tree.pre_order_walk()
    if pre_walk != PRE_STEP1:
        print(
            f'Error: Pre-orderwalk after removing (12) is {pre_walk}, but should be {PRE_STEP1}')
        sys.exit(1)
    post_walk = tree.post_order_walk()
    if post_walk != POST_STEP1:
        print(
            f'Error: Post-orderwalk after removing (12) is {post_walk}, but should be {POST_STEP1}')
        sys.exit(1)
    print('Removing item (8) ...')
    tree.remove(8)
    pre_walk = tree.pre_order_walk()
    if pre_walk != PRE_STEP2:
        print(
            f'Error: Pre-orderwalk after removing (8) is {pre_walk}, but should be {PRE_STEP2}')
        sys.exit(1)
    post_walk = tree.post_order_walk()
    if post_walk != POST_STEP2:
        print(
            f'Error: Post-orderwalk after removing (8) is {post_walk}, but should be {POST_STEP2}')
        sys.exit(1)

    print('Try to remove non-existing element (8)')
    tree.remove(8)
    pre_walk = tree.pre_order_walk()
    if pre_walk != PRE_STEP2:
        print(
            f'Error: Pre-orderwalk after removing (8) again is {pre_walk}, but should be {PRE_STEP2}')
        sys.exit(1)
    post_walk = tree.post_order_walk()
    if post_walk != POST_STEP2:
        print(
            f'Error: Post-orderwalk after removing (8) again is {post_walk}, but should be {POST_STEP2}')
        sys.exit(1)

    print(
        f'Remove the rest of the elements in the following sequence {TO_REMOVE}')
    for i, item in enumerate(TO_REMOVE):
        tree.remove(item)
        if tree.find(item):
            print(f"Failed to remove {item}")
            sys.exit(1)
        height = tree.get_tree_height()
        if height != HEIGHT_CHECK[i]:
            print(f'Your tree is not properly balanced after removing {item}')
            sys.exit(1)

    print("All nodes removed correctly!")


def test_code_quality():
    print("\nTesting code quality by lint score .....\n")
    run = pylint.lint.Run(["AVL.py"], do_exit=False)
    score = run.linter.stats["global_note"]
    if score < LINT_THRESHOLD:
        print(f"The pylint score is only {score}, at least 8.0 required")
        sys.exit(1)
    print("Lint score OK")


if __name__ == '__main__':
    my_tree = AVL()
    check_functions(my_tree)
    my_list = create_test_list()
    test_duplicates(my_tree, my_list)
    test_min_max(my_tree, my_list)
    specific_min_max_test()
    test_find()
    test_get_height()
    print('Testing different walk strategies through the tree...\n',
          'NOTE: Errors can come from an incorrect insertion, ',
          'you can not be sure the walk methods are to blame')
    test_pre_order_walk()
    test_in_order_walk()
    test_post_order_walk()
    test_basic_rotation()
    # my_list = random.sample(my_list, len(my_list))
    test_remove()

    test_code_quality()
    print("\nCongratulations, all tests passed successfully!")
