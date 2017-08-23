import math


def quicksort(array):

	if len(array) <= 1:
		return array

	if len(array) == 2:
		max_elt = get_max(array)
		min_elt = get_min(array, max_elt)
		return [min_elt, max_elt]

	pivot = array.pop()
	smaller_array = []
	larger_array = []

	for item in array:
		if item <=pivot:
			smaller_array.append(item)
	for item in array:
		if item > pivot:
			larger_array.append(item)

	sorted_lower_half = quicksort(smaller_array)
	sorted_upper_half = quicksort(larger_array)

	final_list = []
	final_list.extend(sorted_lower_half)
	final_list.append(pivot)
	final_list.extend(sorted_upper_half)

	return final_list


def get_max(array):

	maximum = 0

	for item in array:
		if item > maximum:
			maximum = item

	return maximum


def get_min(array, start):

	minimum = start

	for item in array:
		if item < minimum:
			minimum = item

	return minimum
