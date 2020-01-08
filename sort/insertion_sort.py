def insertion_sort(l):
	'''
	* desc:
		This function sort list l using insertion sort algorithm
		It iterates through the list.
		At each of the iteration, it traverse back and check if the 
		element that preceed the current key, than assign that value one index foreard.
		Finally, assign the key to the current index

		Run time complexity:
		Worst case: O(n^2) (reverse sorted)
		Bestcase : O(n) (already sorted)

		Space complexity:
		O(1)
	* args:
		l <list> list of values of the same type
	* return:
		none
	'''
	for i in range(len(l)):
		key = l[i]
		while (i-1) >= 0 and key < l[i-1]:
			l[i] = l[i-1]
			i -= 1
		l[i] = key
