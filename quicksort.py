import math

test = [5, 3, 7, 8, 2, 6, 1, 9]

def quicksort(array):
	if len(array) <= 2:
		return array
	pivot = get_pivot(array)
	print(pivot)
	smaller_array = []
	larger_array = []
	index = 0
	for item in array:
		if item < pivot:
			smaller_array.append(item)
			index += 1
	for item in array:
		if item >= pivot:
			larger_array.append(item)
	print(smaller_array)
	print(larger_array)
	sorted_lower_half = quicksort(smaller_array)
	print("sorted lower: ", sorted_lower_half)
	sorted_upper_half = quicksort(larger_array)
	print("sorted upper: ", sorted_upper_half)
	# return sorted_lower_half.extend(sorted_upper_half)
	final_list = []
	final_list.extend(smaller_array)
	final_list.extend(larger_array)
	return final_list

def get_pivot(array):
	maximum = get_max(array)
	minimum = get_min(array, maximum)
	return math.floor((maximum+minimum)/2)
	
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

print(quicksort(test))