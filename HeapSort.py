#!/usr/bin/env python
# -*- coding: utf-8 -*-
# heap sort(max heap)

#对每个非叶子节点进行堆调整
def MAX_Heapify(heap, heapsize, root):
	left = 2 * root + 1
	right = left + 1
	larger = root
	if (left < heapsize) and (heap[larger] < heap[left]):
		larger = left
	if (right < heapsize) and (heap[larger] < heap[right]):
		larger = right
	if root != larger:
		heap[larger], heap[root] = heap[root], heap[larger]
		MAX_Heapify(heap, heapsize, larger)

#构建初始堆
def Build_MAX_Heap(heap):
	heapsize = len(heap)
	for i in xrange((heapsize//2)-1, -1, -1):
		MAX_Heapify(heap, heapsize, i)

#堆排序
def HeapSort(heap):
	Build_MAX_Heap(heap)
	for i in xrange(len(heap)-1, -1, -1):
		heap[0], heap[i] = heap[i], heap[0]
		MAX_Heapify(heap, i, 0)
	return heap

def main():
	alist = [30,50,57,77,62,78,94,80,84]
	HeapSort(alist)

if __name__ == '__main__':
	main()

#conclusion
#best: O(nlog(n))
#worst: O(nlog(n))
#averagy: O(nlog(n))
#稳定性：好
#details:
#从无序数组建立初始堆：O(n), 知乎答案有证明
#堆排序：要选出n次根节点值，每次要进行一次堆重调、O(logn)次下降，即只有被交换到根节点的元素要最终下降到叶子节点