#find the second largest element in a list
numbers=[10,20,4,45,99,99,45]
#remove dupilacte
unique_numbers=list(set(numbers))
#print(unique_numbers)
#sort the elements
unique_numbers.sort()
#get index with second largest element
print('second largest: ',unique_numbers[-2])
#get index with second smallest element
print('second largest: ',unique_numbers[1])