from .swap import swap

def bubble_sort(l):
	'''
	* desc:
		this function sort list l with bubble sort algorithm.
		Iterate through the list, compare every element with
		the succeeding one. Swap the two if the succeeding element is smaller.
		Repeat until there is no more swapping

		Run time complexity: 
		Worst case: O(n^2) sorted but reversed
		Best Case: O(n) already sorted
		Average:  O(n^2)
	* args:
		l <list> list of values of the same type
	* return:
		none
	'''
	is_sorted = False
	last_unsorted_index = len(l) - 1
	while not is_sorted:
		is_sorted = True
		for i in range(last_unsorted_index):
			if l[i] > l[i+1]:
				swap(l, i, i+1)
				is_sorted = False
		last_unsorted_index -= 1