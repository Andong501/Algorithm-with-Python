#!/usr/bin/env python
# -*- coding: utf-8 -*-

#count sort
#k means the max integer(value scope) in list
def countSort(alist, k):
	b = []
	c = [0 for i in xrange(k+1)]
	for i in alist:
		c[i] += 1    #count the value i of alist to c[i]
	c_index = 0    #current index of c
	for i in c:
		for dup in range(0, i):    #dup means num of duplicated i in current index
			b.append(c_index)
		c_index += 1
	return 

def main():
	alist = [1, 4, 2, 6, 3, 20, 12, 15, 12]
	countSort(alist, 20)

if __name__ == '__main__':
	main()

#conclusion:
#best: O(n+k)
#worst: O(n+k)
#averagy: O(n+k)
#稳定性：好