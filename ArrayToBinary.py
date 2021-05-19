import math

def binary_array_to_number(arr):

	arr.reverse()
	amount = 0
	i = 0

	for l in arr:

		result = l * pow(2, i)
		i += 1
		amount = amount + result

	return amount

binary = [0,1,1,1]

data = binary_array_to_number(binary)
print(binary, "====>", data)