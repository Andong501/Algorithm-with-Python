#!/usr/bin/env python
# -*- coding: utf-8 -*-
# fibonacci search

def fibonacciBuilder(max_len): #build a fibonacci list
	F = [0] * max_len
	F[0] = 1
	F[1] = 1
	for i in range(2, max_len):
		F[i] = F[i-1] + F[i-2]
	return F

def listFill(alist, high, F): #make len of alist to be F[k]-1
	k = 0
	while high > F[k] - 1:
		k += 1
	for i in range(F[k]-1-(high+1)):
		alist.append(alist[high])
	return k, alist

def fibonacciSearch(alist, key):
	F = fibonacciBuilder(20)
	k, alist = listFill(alist, len(alist)-1, F)
	low = 0
	high = len(alist) - 1
	
	while low <= high:
		if k < 2:
			mid = low
		else:
			mid = low + F[k-1] - 1
		
		if key < alist[mid]:
			high = mid - 1
			k -= 1
		elif key > alist[mid]:
			low = mid + 1
			k -= 2
		else:
			return mid
	if low > high:
		return -1

if __name__ = '__main__':
	alist = [1, 2, 5, 7, 12, 16, 22, 29, 32]
	key = 22
	fibonacciSearch(alist, key)

#conclusion:
#best: O(log(n))
#worst:O(log(n))
#averagy:O(log(n))