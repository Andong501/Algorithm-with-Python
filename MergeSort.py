#!/usr/bin/env python
# -*- coding: utf-8 -*-
# merge sort
# low/mid/high all mean the indices of list
def mergeSort(alist, low, high):
	if low < high:
		mid = (low + high) / 2
		mergeSort(alist, low, mid)
		mergeSort(alist, mid+1, high)
		merge(alist, low, mid, high)
	return alist

def merge(alist, low, mid, high):    #merge two sorted lists to a new sorted list
	i = low
	j = mid + 1
	p = 0
	templist = [0] * (high - low + 1)
	for p in range(0, len(templist)):
		if i <= mid and j <= high:
			if alist[i] <= alist[j]:
				templist[p] = alist[i]
				i += 1
			# if alist[i] > alist[j]
			else:
				templist[p] = alist[j]
				j += 1
		else:
			if i > mid:
				templist[p] = alist[j]
				j += 1
			# if j > high
			else:
				templist[p] = alist[i]
				i += 1
	alist[low : high+1] = templist
	return alist

def main():
	alist = [1, 4, 2, 6, 3, 20, 12, 15, 12.0]
	low = 0
	high = len(alist) - 1
	mergeSort(alist, low, high)

if __name__ == '__main__':
	main()

#conclusion:
#best:O(nlog(n))
#worst:O(nlog(n))
#averagy: O(nlog(n))
#稳定性：好