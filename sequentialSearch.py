#!/usr/bin/env python
# -*- coding: utf-8 -*-

# sequential search

def sequentialSearch(alist, key):
	result = []
	for i in range(len(alist)):
		if alist[i] == key:
			result.append(i)
	return result

if __name__ == '__main__':
	alist = [23, 45, 78, 22, 123, 236, 123, 999]
	key = 123
	sequentialSearch(alist, key)

#conclusion:
#best: O(1)
#worst: O(n)
#averagy: O(n)