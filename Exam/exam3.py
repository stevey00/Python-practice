'''
A Fibonnaci sequence of integers which first two terms are 0 and 1 and all other terms of the sequence
are obtained by adding their preceeding two numbers.

write a python code that asks a number from the user then uses a recursive function to compute its Fibonnaci
 sequence and display it.
'''

1,1,2,3,5,8,13,21,34,55,89
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