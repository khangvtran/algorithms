def merge(arr, left, right):


	i, j, k = 0, 0, 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1

	while i < len(left):
		arr[k] = left[i]
		i += 1
		k += 1

	while j < len(right):
		arr[k] = right[j]
		j += 1
		k += 1


def merge_sort(l):
	'''
	* desc:
		This function sort a list using merge sort algorithm
		DIVIDE AND CONQUER: keep recursively splitting the array
		 	in half until getting an array of length 1, 
		 	then merge the splitted array back on

		Runtime complexity: O(nlog(n)) for each of the n elements, 
		only compare them with log(n) other elements

		Space complexity: (n)
	* args:
		l <list> list of values of the same type
	* return:
		none
	'''
	# crucial: for recursive: IF, not WHILE
	if len(l) > 1:
		mid = int(len(l)/2)
		left = l[ : mid]
		right = l[mid : ]

		merge_sort(left)
		merge_sort(right)

		merge(l, left, right)




