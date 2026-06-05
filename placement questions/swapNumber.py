# n1=int(input('enter the number: '))
# n2=int(input('enter the number: '))
# num=n1+n2
# n1=num-n1
# n2=num-n2
# print(n1)
# print(n2)
def swap(n1,n2):
    num=n1+n2
    n1=num-n1
    n2=num-n2
    return n1,n2
print(swap(4,7))