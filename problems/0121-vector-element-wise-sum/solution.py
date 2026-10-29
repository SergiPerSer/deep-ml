def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	result =[]
	if len(a) == len(b):
		for i, j in zip(a,b):
			result.append(i+j)
		return result
	else:
		return -1
	pass