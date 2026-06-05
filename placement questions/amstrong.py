def amstrong(n):
    total=0
    length=len(str(n))
    while n>0:
        digit=n%10
        total=total+digit**length
        n//=10
    return total
print(amstrong(123))
# amstrong=int(input('enter the number: '))
# totall=0
# length=len(str(amstrong))
# while amstrong>0:
#     digit=n%10
#     totall=totall+digit**length
#     amstrong//=10
#     print(amstrong)