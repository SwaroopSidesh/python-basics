# print(primeNumber(4))
# primeNumber=int(input('enter the number: '))
# # a=2
# # if a/primeNumber==0:
# #     print('even')
# # else:
# #     print('not prime')
def primeNumber(n):
    for a in range(2,n):
        a/n==0
        return 'prime'
    return 'not prime'
print(primeNumber(5))
