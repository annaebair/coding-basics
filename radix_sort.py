
def radix_sort(array):

	final_array = []
	max_elt = array_max(array)
	max_size = len(str(max_elt)) + 1

	for target_size in range(1, max_size):
		relevant_digit_length = []

		for item in array: 

			if len(str(item)) == target_size:
				relevant_digit_length.append(item)

		sorted_relevant = get_sorting(relevant_digit_length, 0)
		final_array.extend(sorted_relevant)

	return final_array

	
def array_max(array):

	current_max = 0

	for item in array:

		if item > current_max:
			current_max = item

	return current_max


def get_sorting(array, sig_dig):
	if len(array) == 0:
		return array

	first_elt = array[0]

	if all(item == first_elt for item in array):
		return array

	level_ordering = []

	bin_0 = []
	bin_1 = []
	bin_2 = []
	bin_3 = []
	bin_4 = []
	bin_5 = []
	bin_6 = []
	bin_7 = []
	bin_8 = []
	bin_9 = []

	for item in array:

		sorting = int(str(item)[sig_dig])

		if sorting == 0:
			bin_0.append(item)
		elif sorting == 1:
			bin_1.append(item)
		elif sorting == 2:
			bin_2.append(item)
		elif sorting == 3:
			bin_3.append(item)
		elif sorting == 4:
			bin_4.append(item)
		elif sorting == 5:
			bin_5.append(item)
		elif sorting == 6:
			bin_6.append(item)
		elif sorting == 7:
			bin_7.append(item)
		elif sorting == 8:
			bin_8.append(item)
		elif sorting == 9:
			bin_9.append(item)

	bin_list = [bin_0, bin_1, bin_2, bin_3, bin_4, bin_5, bin_6, bin_7, bin_8, bin_9]

	for bin_num in bin_list:

		if len(bin_num) > 1:
			bin_num = get_sorting(bin_num, sig_dig+1)
			level_ordering.extend(bin_num)

		else:
			level_ordering.extend(bin_num)

	return level_ordering

if __name__=='__main__':
	test = [23, 76, 36, 90, 642, 12, 44, 79, 73, 16, 78, 91, 4, 9, 9, 400, 5, 123, 927, 53, 0, 12, 293856]
	print(radix_sort(test))

