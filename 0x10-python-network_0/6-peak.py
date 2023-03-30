#!/usr/bin/python3
'''
    Algorithm for finding the peak integer.
'''


def find_peak(list_of_integers):
    '''
        Finds peak in list of unsorted ints.
    '''
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
