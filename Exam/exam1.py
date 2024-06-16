'''
write a pyton program that runs through a list of values (to be entered by the user) by comparing
it one by one with the value sought, and exits the loop:

-or when it has gone through the whole list without finding the Value
-either when the value has been found

if the value has been found, the program announces "Won", otherwise, the program announces "Lost".
'''

def search_value(values, target):
    for value in values:
        if value == target:
            print("Won")
            return
    print("Lost")


def main():
    try:
        value_list = input("Enter a list of values (separated by spaces): ").split()
        target_value = input("Enter the value to search for: ")
        search_value(value_list, target_value)
    except FileNotFoundError:
        print("File not found. Exiting...")

if __name__ == "__main__":
    main()