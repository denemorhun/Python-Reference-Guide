def bubble_sort(array):

	i = 0
	j = 1
	# first traversal
	for i in range(len(array)):
	# comparison
		for j in range(len(array)-i):
			if (array[i] > array[j]):
				temp = array[i]
				array[i] = array[j]
                array[j] = temp
            else: 
                i+=1
                j+=i+1


bubble_sort([13, 17, 12, 15, 18, 11, 20, 14, 16, 19])

print(bubble_sort)