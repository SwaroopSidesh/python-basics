number=[6,7,9,4,5]
largest=number[0]
smallest=number[0]
for num in number:
    if num > largest:
        largest=num
    if num < smallest:
        smallest=num
print('largest: ',largest)
print('smallest: ',smallest)