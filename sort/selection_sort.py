from .swap import swap

def selection_sort(l):
	'''
	* desc:
		this function sort list l in-place using selection sort algorithm
		It iterate through the list.
		At each iteration i , it find the min value of the sublist
		going from i to the end of the original list

		Run time complexity:
		There are always two nested loop
		Worst case: O(n^2)
		Best case: O(n^2)

		Space Complexity:
		O(1)
	* args:
		l <list> list of values of the same type
	* return:
		none
	'''
	for i in range(len(l)):
		min_val = l[i]
		min_index = i
		for j in range(i, len(l)):
			if l[j] < min_val:
				min_val = l[j]
				min_index = j
		if min_index != i:
			swap(l, i, min_index)

