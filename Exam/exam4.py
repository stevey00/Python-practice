'''
In python, write a program to display the multiplication table of any number entered by the user.
'''

def multiplication_table(number):
    print(f"Multiplication Table of {number}:")
    for i in range(1, 13):
        result = number * i
        print(f"{number} x {i} = {result}")


def main():
    number = int(input("Enter a number: "))
    multiplication_table(number)


if __name__ == "__main__":
    main()
