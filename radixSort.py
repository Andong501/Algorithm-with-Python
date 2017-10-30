#!/usr/bin/env python
# -*- coding: utf-8 -*-

#radix sort
#use the idea of bucket sotr
#k means the value scope of each place: 0-9
#m means the max place of number

def radixSort(alist):
	m = len(str((max(alist))))
	for p in range(0, m):    #for each place
		s = [[] for i in range(10)]    #build buckets for each place
		for i in alist:
			s[i/(10**p)%10].append(i)    #divede buckets
		alist = [a for b in s for a in b]    #merge buckets
	return alist

def main():
	alist = [1, 4, 2, 6, 3, 20, 12, 15, 12]
	radixSort(alist)

if __name__ == '__main__':
	main()


#conclusion:
#best: O(mn)
#worst: O(mn)
#averagy: O(mn)
#稳定性：好