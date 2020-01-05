def binary_search(l, left, right, key):
	'''
	* desc:
		this function recursively search for a value in sorted list
		It compares the current value at mid index,
		and adjust the lef and right index appropriately
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