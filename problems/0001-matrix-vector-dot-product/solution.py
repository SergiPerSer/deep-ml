def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	vector_fin = []
	if len(a[0]) == len(b):
		for i in range(len(a)):
			result = 0
			for j, k in zip(a[i],b):
				result += j*k
			vector_fin.append(result)
		return vector_fin
	else:
		return -1
	pass