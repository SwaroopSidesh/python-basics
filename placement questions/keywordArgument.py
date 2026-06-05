# def myfuntion(**myvar):
#     print('type: ',type(myvar))
#     print('name: ',myvar['name'])
#     print('age: ',myvar['age'])
#     print('all data: ',myvar)
# myfuntion(name='Ravi',age='25',city='hyderabad')

# def my_function(usename,**details):
#     print('usename: ',usename)
#     print('additional detals: ')
#     for key,value in details.items():
#         print('',key+':',value)
# my_function('ravi123',age=25,city='hyderabad',hobby='coding')

#regular arguments*args,**kwargs
def my_function(title,*args, **kwargs):
    print('title: ',title)
    print('positon arguments: ',args)
    print('keyword arguments: ',kwargs)
my_function('user infot','ravi','varun',age='25',city='hyd')
