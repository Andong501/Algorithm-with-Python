#!/usr/bin/env python
# -*- coding: utf-8 -*-
# bubble sort

import time

def bubbleSort(alist):
	tik = time.time()
	for passnum in range(len(alist)-1, 0, -1):
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
	tok = time.time();
	jetlag = 1000*(tok - tik)
	return alist, jetlag


alist = [54,26,93,17,77,31,44,55,20];
print(bubbleSort(alist));

# optimized bubble sort

def opBubbleSort(alist):
	tik = time.time()
	exchange = True
	passnum = len(alist) - 1
	while passnum >= 1 and exchange:
		exchange = False
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
				exchange = True
		passnum -= 1
	tok = time.time()
	jetlag = 1000*(tok - tik)
	return alist, jetlag

def opBubbleSortMe(alist):
	tik = time.time()
	exchange = True
	passnum = len(alist) - 1
	for passnum in range(len(alist)-1, 0, -1):
		while(exchange):
		    exchange = False
		    for i in range(passnum):
			    if alist[i] > alist[i+1]:
				    alist[i], alist[i+1] = alist[i+1], alist[i]
				    exchange = True
	tok = time.time()
	jetlag = 1000*(tok - tik)
	return alist, jetlag

def main():
	alist = [1, 4, 2, 6, 3, 20, 12, 15, 12.0]
	opBubbleSort(alist)

if __name__ == '__main__':
	main()

#conclusion:
#best：O(n)
#worst:O(n^2)
#averagy:O(n^2)
#稳定性：好