# def reverse(n):
#     total=0
#     while n>0:
#         a=n%10
#         total=total*10+a
#         n//=10
#     return total
# print(reverse(123))
reverse=int(input('enter the number'))
total=0
while reverse>0:
    a=reverse%10
    total=total*10+a
    reverse=reverse//10
print(reverse)