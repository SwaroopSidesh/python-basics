# def fibonacciNumber(n):
#     a=0
#     b=1
#     for i in range(n):
#         c=a+b
#         a=b
#         b=c
#         print(a)
# print(fibonacciNumber(10))
fibonacciNumber=int(input('enter the number: '))
a=0
b=1
for i in range(fibonacciNumber):
    c=a+b
    a=b
    b=c
    print(a)
print('the fibonacci number: '+ fibonacciNumber)