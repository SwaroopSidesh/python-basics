# # def my_function(*kids):
# #     print('the yougust child is '+ kids[2])
# # my_function('ram','shiva','venkat')

# def my_function(*args):
#     print('type: ',type(args))
#     print('fisrt arugment: ',args[0])
#     print('second argument: ',args[1])
#     print('all arguments:',args)
# my_function('raju','kumar','varun')

# def my_function(greeting,*names):
#     for name in names:
#         print(greeting,name)
# my_function('hellow','ravi','harishi','swaroop')

# def my_function(*numbers):
#     total=0
#     for num in numbers:
#         total += num
#     return total
# print(my_function(1,2,3))
# print(my_function(10,20,30,40,50))
# print(my_function(5))

def my_functiin(*numbers):
    if len(numbers)==0:
        return None
    max_num=numbers[0]
    for num in numbers:
        if num>max_num:
            max_num=num
    return max_num
print(my_functiin(3,7,2,9,1))