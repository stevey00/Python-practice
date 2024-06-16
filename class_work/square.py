def read_squares(x, y):
    squares = []
    for i in range(x, y+1):
        sqr = i**2
        squares.append(sqr)
    return squares

square_list = read_squares(1, 100)

# print(len(read_squares(100)))

squares_fours = []
squares_nine = []

for i in square_list:
    item = str(i)
    last = item[-1]
    if last == '4':
        squares_fours.append(i)

for i in square_list:
    item = str(i)
    last = item[-1]
    if last == '9':
        squares_nine.append(i)
        
print(squares_fours)    
print(squares_nine)    