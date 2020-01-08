def binary_search(l, left, right, key):
	'''
	* desc:
		this function RECURSIVELY search for a value in sorted list
		It compares the current value at mid index,
		and adjust the lef and right index appropriately
		
		Best Case: O(1) the key is at the mid index of the list
		Worst case: O(log(n)) the key is at the two ends
		Average: O(log(n))
	* args:
		l <list>: sorted list of values
		left <int>: left index
		right <int>: right index
		key <data type of list element>: the searched value
	* return:
		mid <int>: index of key if found. -1 otherwise
	'''

	# base case
	if left > right:
		return(-1)

	# recursion case
	mid = int((left + right)/2)
	if l[mid] == key:
		return(mid)
	elif l[mid] < key:
		left = mid + 1
	else:
		right = mid - 1
	return(binary_search(l, left, right, key))


def binary_search_iteration(l, key):
	'''
	* desc:
		this function ITERATIVELY search for a value in sorted list
		It compares the current value at mid index,
		and adjust the lef and right index appropriately
		
		Best Case: O(1) the key is at the mid index of the list
		Worst case: O(log(n)) the key is at the two ends
		Average: O(log(n))
	* args:
		l <list>: sorted list of values
		key <data type of list element>: the searched value
	* return:
		mid <int>: index of key if found. -1 otherwise
	'''
	left = 0
	right = len(l) - 1
	while left <= right:
		mid = int((left+right)/2)
		if l[mid] == key:
			return(mid)
		elif l[mid] < key:
			left = mid + 1
		else:
			right = mid - 1
	return(-1)








	