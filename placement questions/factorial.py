# def factorial_number(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# print(factorial_number(5))
# def factorial_number(n):
#     i=n-1
#     for i in range(i>0,n):
#         n=n*i
#     return n
# print(factorial_number(5))
factorial_number=int(input('enter the number: '))
i=factorial_number-1
for i in range(i>0,factorial_number):
    factorial_number*=i
print(factorial_number)