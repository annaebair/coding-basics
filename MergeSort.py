import math

def merge_sort(input_list):
	length = len(input_list)
	if length <= 2:
		return sort_base_case(input_list)
	half = math.floor(length/2)
	first_half = input_list[0:half]
	second_half = input_list[half:length]
	sorted_first_half = merge_sort(first_half)
	sorted_second_half = merge_sort(second_half)
	return merge(sorted_first_half, sorted_second_half)

def sort_base_case(input_list):
	if len(input_list) == 2:
		val0 = input_list[0]
		val1 = input_list[1]
		first = min(val0, val1)
		second = max(val0, val1)
		return [first, second]
	else:
		return input_list

def merge(list1, list2):
	final_list = []

	while len(list1) > 0 and len(list2) > 0:
		if list1[0] < list2[0]:
			final_list.append(list1[0])
			list1.pop(0)
		else:
			final_list.append(list2[0])
			list2.pop(0)
	final_list.extend(list1)
	final_list.extend(list2)
	return final_list
