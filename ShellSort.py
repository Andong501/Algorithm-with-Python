#!/usr/bin/env python
# -*- coding: utf-8 -*-
# shell sort

def shellSort(alist):
	n = len(alist)
	gap = n // 2

	while gap >= 1:
		for i in range(gap, n):
			tempi = i
			while tempi >=gap:
				if alist[tempi] < alist[tempi-gap]:
					alist[tempi], alist[tempi-gap] = alist[tempi-gap], alist[tempi]
					tempi -= gap
				else:
					break
		gap //= 2
	return alist

if __name__ == '__main__':
	alist = [1, 4, 2, 6, 3, 20, 12, 15, 12.0]
	shellSort(alist)

#conclusion:
#best: depends on gap, perform well on long list
#worst: O(n^2)
#averagy: depends on gap
#稳定性：不好