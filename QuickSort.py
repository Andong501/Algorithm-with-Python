#!/usr/bin/env python
# -*- coding: utf-8 -*-
# quick sort

def quickSort(alist):
	quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, start, end):
	if start < end:
		i = start
		j = end
		pivot = alist[i]
		while (i < j):
			while (i < j) and (pivot <= alist[j]):
				j -= 1
			alist[i] = alist[j]

			while (i < j) and (alist[i] <= pivot):
				i += 1
			alist[j] = alist[i]
		alist[i] = pivot

		quickSortHelper(alist, start, i-1)
		quickSortHelper(alist, j+1, end)
	return alist


def quickSortMe(alist):
	quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelperMe(alist, first, last):
	if first < last:
		pivot = first
		compair = last
		direction = 1

		while (pivot < compair):
			if direction == 1:
				if alist[pivot] <= alist[compair]:
					compair -= 1
				else:
					alist[pivot], alist[compair] = alist[compair], alist[pivot]
					pivot, compair = compair, pivot
					direction = -1
					compair += 1
			if direction == -1:
				if alist[pivot] >= alist[compair]:
					compair += 1
				else:
					alist[pivot], alist[compair] = alist[compair], alist[pivot]
					pivot, compair = compair, pivot
					direction = 1
					compair -= 1
		splitpoint = pivot

		quickSortHelperMe(alist, first, splitpoint-1)
		quickSortHelperMe(alist, splitpoint+1, last)
	return alist

def main():
	alist = [1, 4, 2, 6, 3]
	quickSort(alist)

if __name__ == '__main__':
	main()

#conclusion:
#best: O(nlog(n))
#worst: O(n^2)
#avergy: O(nlog(n))
#稳定性：不好