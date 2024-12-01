def test(lst):
	result = {}
	for item in lst:
		result[item[0]] = item[1:]
	return result

students = [[1, "Aaqib" , "IX"], [2, "Hasnain" , "XI"], [3, "Hanzla", "VI"]]

print("\nOriginal list of lists:")
print(students)
print("\nConverted  lists to a dictionary:")
print(test(students))