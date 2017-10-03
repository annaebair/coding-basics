import pytest

import radix_sort

class TestRadixSort:

	def test_basic(self):
		unsorted = [3, 2, 1]
		actual = radix_sort.radix_sort(unsorted)
		expected = [1, 2, 3]
		assert actual == expected

	def test_one_item(self):
		unsorted = [1]
		actual = radix_sort.radix_sort(unsorted)
		expected = [1]
		assert actual == expected

	def test_odd_number(self):
		unsorted = [5, 2, 4, 11, 3, 9, 10]
		actual = radix_sort.radix_sort(unsorted)
		expected = [2, 3, 4, 5, 9, 10, 11]
		assert actual == expected

	def test_multiples(self):
		unsorted = [5, 2, 3, 8, 8, 1, 1, 1, 9]
		actual = radix_sort.radix_sort(unsorted)
		expected = [1, 1, 1, 2, 3, 5, 8, 8, 9]
		assert actual == expected