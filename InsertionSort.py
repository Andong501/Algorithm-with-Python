#!/usr/bin/env python
# -*- coding: utf-8 -*-
# insertion sort

def insertionSort(alist):
	for cur in range(1, len(alist)):
		fetch = alist[cur]
		for i in range(cur-1, -2, -1):
			if i >= 0:
				if fetch < alist[i]:
					alist[i+1] = alist[i]
				else:
					alist[i+1] = fetch
					break
			else:
				alist[i+1] = fetch
	return alist

def main():
	alist = [1, 4, 2, 6, 3]
	insertionSort(alist)

if __name__ == '__main__':
	main()


#conclusion:
#best: O(n)
#worst: O(n^2)
#averagy: O(n^2)
#稳定性：好