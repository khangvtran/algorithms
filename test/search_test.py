import sys
sys.path.insert(0, '..')
from search import *

if __name__ == '__main__':
	print('### Test Recursion ###')

	l = [4, 5, 8, 9, 10, 15, 17]
	print(f'list: {l}')

	key = 15
	print(f'search for {key}: ', end = '')
	print(binary_search(l, 0, len(l)-1, key))

	key = 4
	print(f'search for {key}: ', end = '')
	print(binary_search(l, 0, len(l)-1, key))

	key = 17
	print(f'search for {key}: ', end = '')
	print(binary_search(l, 0, len(l)-1, key))

	key = 6
	print(f'search for {key}: ', end = '')
	print(binary_search(l, 0, len(l)-1, key))


	print('\n### Test Recursion Iteration ###')

	l = [4, 5, 8, 9, 10, 15, 17]
	print(f'list: {l}')

	key = 15
	print(f'search for {key}: ', end = '')
	print(binary_search_iteration(l, key))

	key = 4
	print(f'search for {key}: ', end = '')
	print(binary_search_iteration(l, key))

	key = 17
	print(f'search for {key}: ', end = '')
	print(binary_search_iteration(l, key))

	key = 6
	print(f'search for {key}: ', end = '')
	print(binary_search_iteration(l, key))
