# print("*");
# print("**");
# print("***");
# print("****");


# res1 = 512 - 282;
# val1 = 47.48 + 5.0;
# ans = float(res1)/val1;
# print(ans);


# uAns = eval(input('Please enter a number: '));
# square = uAns ** 2;
# print("The square of ", uAns, " is ", square, sep=" ");


# x = eval(input('Please enter a number: '));
# print(x,2*x,3*x,4*x,5*x, sep="---");


# weightKg = eval(input('Please enter value for weight: '));
# weightPd = weightKg*2.2;
# print('Weight in Pds is: ', weightPd, "Pds");


# num1 = eval(input('Enter first number: '));
# num2 = eval(input('Enter second number: '));
# num3 = eval(input('Enter third number: '));
# total = num1+num2+num3;
# av = total/3;
# print("The total is: ", total, "The average is: ", av);


# price = eval(input('Please enter the bill amount: '));
# tip = eval(input('Please enter the tip amount: '));
# tipVal = 1 + (tip/100);
# bill = int(tipVal*price);
# print('Your total bill including tip amount is: ', bill)


# for i in range(10):
#  print("Hello");

# for i in range(3):
#     # print('*'*6);
#     print('*'*(i+1));


# def print_diamond(rows):
#     if rows % 2 == 0:
#         rows += 1
    
#     n = (rows + 1) // 2
    
#     for i in range(1, n + 1):
#         for j in range(n - i):
#             print(" ", end="")
#         for j in range(2 * i - 1):
#             print("*", end="")
#         print()
    
#     for i in range(n - 1, 0, -1):
#         for j in range(n - i):
#             print(" ", end="")
#         for j in range(2 * i - 1):
#             print("*", end="")
#         print()

# # Example usage
# num_rows = eval(input('Please enter the number of rows: '))
# print_diamond(num_rows)


row = int(input('Please how large should be your diamond: '))

for i in range(row):
    print(' '*(row-i)+' *'*(i+1))
for j in range(row-1):
    print(' '*(j+2)+' *'*(row-1-j))