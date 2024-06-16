def difference_of_squares(n):
    result = []
    for x in range(1, int(n**0.5) + 1):
        y_square = x**2 - n
        if y_square >= 0 and int(y_square**0.5)**2 == y_square:
            result.append((x, int(y_square**0.5)))
            result.append((-x, int(y_square**0.5)))  # Also considering negative values of x
    return result

number = int(input("Enter a number: "))

solutions = difference_of_squares(number)
if len(solutions) > 0:
    print(f"The number {number} can be written as the difference of two perfect squares in the following ways:")
    for solution in solutions:
        print(f"{solution[0]}^2 - {solution[1]}^2")
else:
    print(f"The number {number} cannot be written as the difference of two perfect squares.")