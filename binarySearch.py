#!/usr/bin/env python
# -*- coding: utf-8 -*-
# binary search

def binarySearch(alist, key):
	low = 0
	high = len(alist) - 1
	time = 0
	while low <= high:
		time += 1
		mid = (low + high) / 2
		if key < alist[mid]:
			high = mid - 1
		elif key > alist[mid]:
			low = mid + 1
		else: #if key == alist[mid]
			return time,mid
	if low > high:
		return time,False

def binarySearchRecursion(alist, key, low, high): #recursion version
	if low <= high:
		mid = (high + low) / 2
		if key < alist[mid]:
			return interpolationSearch(alist, key, low, mid-1)
		elif key > alist[mid]:
			return interpolationSearch(alist, key, mid+1, high)
		else:
			return mid
	else:
		return -1

def binarySearchPro(alist, key): #pro version: search all duplicated keys
	low = 0
	high = len(alist) - 1
	time = 0
	result = []
	while low <= high:
		time += 1
		mid = (low + high) / 2
		if key < alist[mid]:
			high = mid - 1
		elif key > alist[mid]:
			low = mid + 1
		else: #if key == alist[mid]
			result.append(mid)
			for i in range(mid-1, -1, -1): #find the former ones
				if key == alist[i]:
					result.insert(0, i)
				else:
					break
			for j in range(mid+1, len(alist)-1): #find the after ones
				if key == alist[j]:
					result.append(j)
				else:
					break
			break
	return result

if __name__ = '__main__':
	alist = [1, 2, 5, 7, 12, 16, 22, 29, 32]
	key = 7
	binarySearch(alist, key)
	alistpro = [1, 1, 2, 5, 7, 7, 7, 7, 11, 12, 22, 25, 29]
	key = 7
	binarySearchPro(alistpro, key)

#conclusion:
#best: O(log(n))
#worst:O(log(n))
#averagy: O(log(n))