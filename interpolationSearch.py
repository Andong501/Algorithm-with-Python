#!/usr/bin/env python
# -*- coding: utf-8 -*-
# interpolation search

from __future__ import division #精确除法

def interpolationSearch(alist, key):
	low = 0
	high = len(alist) - 1
	while low < high:
		mid = low + int((key - alist[low]) / (alist[high] - alist[low]) * (high - low)) #interpolation formula
		if key < alist[mid]:
			high = mid - 1
		elif key > alist[mid]:
			low = mid + 1
		else: #if key == alist[mid]
			return mid
	if low == high:
		mid = low
		if key == alist[mid]:
			return mid
		else: #if key != alist[mid]
			return -1
	elif low > high:
		return -1

def interpolationSearchRecursion(alist, key, low, high): #recursion version
	if low < high:
		mid = low + int((key - alist[low]) / (alist[high] - alist[low]) * (high - low)) #interpolation formula
		if key < alist[mid]:
			return interpolationSearch(alist, key, low, mid-1)
		elif key > alist[mid]:
			return interpolationSearch(alist, key, mid+1, high)
		else: #if key == alist[mid]
			return mid
	elif low == high:
		mid = low
		if key == alist[mid]:
			return mid
		else: #if key != alist[mid]
			return -1
	else: #if low > high
		return -1

if __name__ = '__main__':
	alist = [1, 2, 5, 7, 12, 16, 22, 29, 32]
	key = 10
	interpolationSearch(alist, key)

#conclusion:
#averagy: O(log(log(n)))
#适用情况：有序，数据量大，分布均匀