#!/usr/bin/env python
# -*- coding: utf-8 -*-
# selection sort

def selectionSort(alist):
	for i in range(len(alist)-1):
		smallest = i
		for j in range(i, len(alist)):
			if alist[j] < alist[smallest]:
				smallest = j
		if i != smallest:
			alist[i], alist[smallest] = alist[smallest], alist[i]
	return alist

def main():
	alist = [1, 4, 2, 6, 3]
	selectionSort(alist)

if __name__ == '__main__':
	main()

#conclusion:
#best: O(n^2)
#worst: O(n^2)
#averagy: O(n^2)
#稳定性：不好