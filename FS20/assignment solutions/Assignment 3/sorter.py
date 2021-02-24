# -*- coding: utf-8 -*-
"""
sorter.py
Janick Spirig
15-538-085
"""
from sys import maxsize
from time import time
### Other imports for your tasks ###

import random as rndm

####################################


class Sorter():
    """Sorter implements several algorithms to sort a list.

    `unsorted_tuple`: A tuple of random integers to be sorted.

    `algorithm`: A string contains name of the algorithm to be used for sorting.
                 Valid valus are 'bubble', 'default', 'insert', and 'merge'.

    Each sorting method make a list copy of `unsorted_tuple` and maintains the original order.

    """
    
    def __init__(self):
        """Sorter constructor.

        By default, the `algorithm` is set as 'default' to use the built-in sort()

        """
        self.unsorted_tuple = tuple([])
        self.algorithm = 'default'


    def generate_new_tuple(self, n):
        """Generate a n-length tuple of random integers for `unsorted_tuple`

        `n` is an integer indicates the length of the list.

        Random integers are in a range from 0 to 9223372036854775807 (sys.maxsize)

        The method generate_new_tuple() first generates a new list of `n` length
        containing random integers, converts the newly generated list to a tuple,
        assigns the tuple to `self.unsorted_tuple`, and returns None.

        """
        ###   Task 1(a)   ###
        
        # create empty list to store random numbers
        randomlist = []

        # execute random method n times -> n numbers in total
        for i in range(n):
            # generate random number between 0 and sys.maxsize
            x = rndm.randint(0,maxsize)
            # add random number to list
            randomlist.append(x)
        
        # convert list to tuple format 
        self.unsorted_tuple = tuple(randomlist)

        return None
        ### Task 1(a) END ###


    def set_algorithm(self, algo):
        """Set the attribute to select which algorithm to be used for sort()."""
        # Check if the given algorithm is valid
        if algo not in ['default', 'merge', 'insertion', 'bubble']:
            raise AlgorithmNotImplementedError
        self.algorithm = algo


    def time_trials(self, n):
        """Time sorting `self.unsorted_tuple` with a specific algorithm for n times.

        `n` is an integer value. The sorting will be performed `n` times.

        The method time_trials() returns a float value for how long it took in seconds.

        """
        start_time = time() # current time

        for i in range(n):
            is_reverse = (i%2 == 0)
            if self.algorithm == 'merge':
                self._merge_sort(is_reverse)
            elif self.algorithm == 'insertion':
                self._insertion_sort(is_reverse)
            elif self.algorithm == 'bubble':
                self._bubble_sort(is_reverse)
            else:
                self._default_sort(is_reverse)

        return time() - start_time # time elapsed


    def _bubble_sort(self, reverse=False):
        """Sort `self.unsorted_tuple` with Bubble Sort algorithm.

        `reverse` is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

        The bubble_sort() method returns the sorted list while it keeps `self.unsorted_tuple` unsorted. The returned value MUST be List data type.

        """
        lst = list(self.unsorted_tuple)
        ###   Task 4   ###
        
        length = len(lst)-1                
        
        # execute algorithm for 'length' times
        for i in range(length, 0, -1):
        # iterate over all index positions
            for j in range(i):
                # check if list should be sorted reversed and if value after is bigger than value before
                if (reverse == True) and (lst[j+1] > lst[j]):
                    # exchange values
                    lst[j],lst[j+1] = lst[j+1],lst[j]
                # check if list should not be sorted reversed and if value after is smaller than value before
                if (reverse == False) and (lst[j+1] < lst[j]):
                    lst[j],lst[j+1] = lst[j+1],lst[j]

        ### Task 4 END ###
        return lst


    def _default_sort(self, reverse=False):
        """Sort `self.unsorted_tuple` with the Python built-in list sorting function.

        `reverse` is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

        The default_sort() method returns the sorted list while it keeps `self.unsorted_tuple` unsorted. The returned value MUST be List data type.

        """
        # Make a list copy of self.unsorted_tuple
        lst = list(self.unsorted_tuple)
        # sort the list by the Python built-in list.sort()
        # https://docs.python.org/3/library/stdtypes.html#list.sort
        lst.sort(reverse=reverse)
        return lst

    def _insertion_sort(self, reverse=False):
        """Sort `self.unsorted_tuple` with Insertion Sort algorithm.

        `reverse` is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

        The insertion_sort() method returns the sorted list while it keeps `self.unsorted_tuple` unsorted. The returned value MUST be List data type.

        """
        lst = list(self.unsorted_tuple)
        ###   Task 3   ###
        
        # length of list
        n = len(lst)
        
        # iterate over each index position oflist
        for i in range(n):
            j = i
            while (j > 0):
                # check if sorting should be done reversed
                if (reverse == True):
                    if (lst[j] > lst[j-1]):
                        # exchange values
                        lst[j], lst[j-1] = lst[j-1], lst[j]
                        # check next element
                        j -= 1
                    else:
                        # exit current while loop execution as no elements should be changed
                        break
                if (reverse == False):
                    if (lst[j] < lst[j-1]):
                        lst[j], lst[j-1] = lst[j-1], lst[j]
                        j -= 1
                    else:
                        break

        ### Task 3 END ###
        return lst

    def _merge_sort(self, reverse=False):
        """Sort `self.unsorted_tuple` with Merge Sort algorithm.

        `reverse` is a boolean value. If set to True, then the list elements are sorted as if each comparison were reversed.

        The merge_sort() method returns the sorted list while it keeps `self.unsorted_tuple` unsorted. The returned value MUST be List data type.

        """
        lst = list(self.unsorted_tuple)
        ###   Task 5   ###
        
        def split(input_list):
            """
            Splits a list into two pieces
            :param input_list: list
            :return: left and right lists (list, list)
            """
            input_list_len = len(input_list)
            midpoint = input_list_len // 2
            return input_list[:midpoint], input_list[midpoint:]

        def merge_sorted_lists(list_left, list_right):
            """
            Merge two sorted lists
            This is a linear operation
            O(len(list_right) + len(list_right))
            :param left_list: list
            :param right_list: list
            :return merged list
            """
            # Special case: one or both of lists are empty
            if len(list_left) == 0:
                return list_right
            elif len(list_right) == 0:
                return list_left
            
            # check if reverse sorting should be done
            def check_reverse():
                
                if reverse == True:
                    # check if left value bigger than right
                    if list_left[index_left] >= list_right[index_right]:
                        return True
                    else:
                        return False
                else:
                    # check if right value bigger than right
                    if list_left[index_left] <= list_right[index_right]:
                        return True
                    else:
                        return False
            
            # General case
            index_left = index_right = 0
            list_merged = []  # list to build and return
            list_len_target = len(list_left) + len(list_right)
            while len(list_merged) < list_len_target:
                # check condition under consideration of reverse parameter
                if check_reverse() == True:
                    # Value on the left list is smaller (or equal so it should be selected)
                    list_merged.append(list_left[index_left])
                    index_left += 1
                else:
                    # Right value bigger
                    list_merged.append(list_right[index_right])
                    index_right += 1
                    
                # If we are at the end of one of the lists we can take a shortcut
                if index_right == len(list_right):
                    # Reached the end of right
                    # Append the remainder of left and break
                    list_merged += list_left[index_left:]
                    break
                elif index_left == len(list_left):
                    # Reached the end of left
                    # Append the remainder of right and break
                    list_merged += list_right[index_right:]
                    break
                
            return list_merged

        def merge_sort(input_list):
            if len(input_list) <= 1:
                return input_list
            else:
                left, right = split(input_list)
                # The following line is the most important piece in this whole thing
                return merge_sorted_lists(merge_sort(left), merge_sort(right))
            
        left, right = split(lst)
        result_list = merge_sorted_lists(left, right)
        lst = merge_sort(result_list)

        ### Task 5 END ###
        return lst

class AlgorithmNotImplementedError(Exception):
    """Raised when an nknown algorithm was selected"""
    pass
