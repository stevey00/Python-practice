from random import randint
from math import pi, sin

# num = eval(input(3+4))
# name = input('my name is: ' )

# print('hello ', end='')
# print('Your name is:',name,sep=' ')

# temp = eval(input('Please enter temperature in celcius: '))
# f_temp = (temp * (9/5)) + 32

# if f_temp>212:
#     print('it is hot, wear a singlet.')
# if f_temp<27:
#     print('its freezing, wear a pullover nigga')
# if 22<f_temp<212:
#     print('you are somewhere')

# for i in range(3):
#     num = eval(input('please enter a number: '))
#     print('the square of the number is :', num*num, sep=' ')
# print('the loop is now over.')

# for i in range(5,0,-1):
#     print(i, end=' ')
# print('blast off!!!')

# for i in range(1,6):
#     print('*'*i)

# for i in range(6):
#     print('*'*(i+1))


# 1,1,2,3,5,8,13,21,34,55,89
num = eval(input('How many numbers do you want to print? '))
n1,n2=0,1
count=0
if num < 0:
    print('Please enter a positive number.')
elif num == 1:
    print('The fibonacci sequence upto', num, 'is equal to:',n1,sep=' ')
else:
    while count<num:
        print(n1,end=' ')
        nth = n1+n2
        n1=n2
        n2=nth
        count+=1


# x = randint(1,10)   
# print(x, end=' ')
# print(pi)

# count=0
# for i in range(1,101):
#     if (i**2)%10==4:
#         # count=count+1
#         count+=1
# print('There are',count,'numbers that end in a 4.', end=' ')