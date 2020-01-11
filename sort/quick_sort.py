def partition(arr, low, high):
	# set pivot to be the last element
	pivot = arr[high]
	# keep track of the current index in arr to be swapped
	i = low 
	# iterate and swap to make sure that all element < pivot
	# is on the left of pivot
	# notice: we might have to keep sorting those elements
	for j in range(low, high):
		if arr[j] < pivot:
			arr[j], arr[i] = arr[i], arr[j]
			i += 1
	# swap current index with pivot
	# notice: don't swap arr[i], pivot, since we need
	# to chang arr
	arr[i], arr[high] = arr[high], arr[i]
	return(i)