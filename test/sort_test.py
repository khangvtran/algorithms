
# Method 1 and 2 are applied for DIRECT directory.
# Meaning: the test file is contained in the direct parent of the pacakge

'''
### 1. Import packages WITHOUT import in init ###
import sort.bubble_sort
from sort.selection_sort import selection_sort

if __name__ == '__main__':
	sort.bubble_sort.bubble_sort()
	selection_sort()
'''

'''
### 3. import WITH import code in init ###
from sort import *

if __name__ == '__main__':
	bubble_sort()
	selection_sort()
	insertion_sort()
'''

### 3. Import from an INDIRECT directory
import sys
sys.path.insert(0, '..')
from sort import *

if __name__ == '__main__':

	print('### Test swap ###')
	l = [9, 3, 7, 8, 5, 4, 6]
	print(f'list: {l}:')
	swap(l, 2, 4)
	print(f'swap the 3rd and the 5th elements: {l}')


	print('\n### Test bubble sort ###')
	l = [9, 3, 7, 8, 5, 4, 6]
	print(f'list: {l}')
	bubble_sort(l)
	print(f'sorted list: {l}')

	l = [9]
	print(f'list: {l}')
	bubble_sort(l)
	print(f'sorted list: {l}')

	l = [9, 3]
	print(f'list: {l}')
	bubble_sort(l)
	print(f'sorted list: {l}')

	l = []
	print(f'list: {l}')
	bubble_sort(l)
	print(f'sorted list: {l}')


	print('\n### Test selection sort ###')
	l = [9, 3, 7, 8, 5, 4, 6]
	print(f'list: {l}')
	selection_sort(l)
	print(f'sorted list: {l}')

	l = [9]
	print(f'list: {l}')
	selection_sort(l)
	print(f'sorted list: {l}')

	l = [9, 3]
	print(f'list: {l}')
	selection_sort(l)
	print(f'sorted list: {l}')

	l = []
	print(f'list: {l}')
	selection_sort(l)
	print(f'sorted list: {l}')


	print('\n### Test insertion sort ###')
	l = [9, 3, 7, 8, 5, 4, 6]
	print(f'list: {l}')
	insertion_sort(l)
	print(f'sorted list: {l}')

	l = [9]
	print(f'list: {l}')
	insertion_sort(l)
	print(f'sorted list: {l}')

	l = [9, 3]
	print(f'list: {l}')
	insertion_sort(l)
	print(f'sorted list: {l}')

	l = []
	print(f'list: {l}')
	insertion_sort(l)
	print(f'sorted list: {l}')


	print('\n### Test merge ###')
	arr = []
	left = []
	right = []
	print(f'arr = {arr}, left = {left}, right = {right}')
	merge(arr, left, right)
	print(f'after merge: {arr}')

	arr = [9, 3]
	left = [3]
	right = [9]
	print(f'arr = {arr}, left = {left}, right = {right}')
	merge(arr, left, right)
	print(f'after merge: {arr}')

	arr = [3, 9, 7]
	left = [3, 9]
	right = [7]
	print(f'arr = {arr}, left = {left}, right = {right}')
	merge(arr, left, right)
	print(f'after merge: {arr}')

	arr = [3, 4, 5, 6, 7]
	left = [3, 5, 7]
	right = [4, 6]
	print(f'arr = {arr}, left = {left}, right = {right}')
	merge(arr, left, right)
	print(f'after merge: {arr}')


	print('\n### Test merge_sort ###')
	l = [9, 3, 7, 8, 5, 4, 6]
	print(f'list: {l}')
	merge_sort(l)
	print(f'sorted list: {l}')

	l = [9]
	print(f'list: {l}')
	merge_sort(l)
	print(f'sorted list: {l}')

	l = [9, 3]
	print(f'list: {l}')
	merge_sort(l)
	print(f'sorted list: {l}')

	l = []
	print(f'list: {l}')
	merge_sort(l)
	print(f'sorted list: {l}')


	print('\n### Test partition ###')
	l = [9, 3, 7, 8, 5, 4, 6]
	print(f'* list: {l}')
	i =partition(l, 0, len(l) - 1)
	print(f'sorted list: {l}')
	print(f'current i: {i}')

	l = [9, 3]
	print(f'* list: {l}')
	i =partition(l, 0, len(l) - 1)
	print(f'sorted list: {l}')
	print(f'current i: {i}')

	l = [9]
	print(f'* list: {l}')
	i =partition(l, 0, len(l) - 1)
	print(f'sorted list: {l}')
	print(f'current i: {i}')

	l = []
	print(f'* list: {l}')
	i =partition(l, 0, len(l) - 1)
	print(f'sorted list: {l}')
	print(f'current i: {i}')


	print('\n### Test quick sort ###')
	l = [9, 3, 7, 8, 5, 4, 6]
	print(f'list: {l}')
	quick_sort(l, 0, len(l)-1)
	print(f'sorted list: {l}')

	l = [9, 3]
	print(f'list: {l}')
	quick_sort(l, 0, len(l)-1)
	print(f'sorted list: {l}')

	l = [9]
	print(f'list: {l}')
	quick_sort(l, 0, len(l)-1)
	print(f'sorted list: {l}')

	l = []
	print(f'list: {l}')
	quick_sort(l, 0, len(l)-1)
	print(f'sorted list: {l}')


























