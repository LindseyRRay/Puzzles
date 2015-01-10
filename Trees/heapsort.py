#Q: implement heapsort 
from heap import Heap 
from random import randint



def heapsort(sort_array):
	built_heap = Heap(sort_array)
	while built_heap.heapsize >= 1:
		temp = built_heap.heap[built_heap.heapsize]
		built_heap.heap[built_heap.heapsize] = built_heap.heap[0]
		built_heap.heap[0] = temp
		built_heap.max_heapify(built_heap.heapsize, built_heap.heap)
		built_heap.heapsize -= 1
	return built_heap.heap


if __name__ == '__main__':
	array = [randint(-100, 100) for i in range(5)]
	print("original")
	print(array)
	array = heapsort(array)
	print("sorted")
	print(array)

