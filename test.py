import unittest
from sorting import insertionSort
from sorting import mergeSort

class SortingTestCase(unittest.TestCase):
	def test_insertion_sort(self):
		arr=[6,1,0,3,8,2,4,7,5,9]
		sortedArr = [0,1,2,3,4,5,6,7,8,9]
		insertionSort(arr)
		self.assertListEqual(arr,sortedArr)

	def test_merge_sort(self):
		arr=[6,1,0,3,8,2,4,7,5,9]
		sortedArr = [0,1,2,3,4,5,6,7,8,9]
		mergeSort(arr)
		self.assertListEqual(arr,sortedArr)


if __name__ == '__main__':
	unittest.main()
