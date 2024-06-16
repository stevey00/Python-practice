# Function to convert a date string to a more verbose format
def convert_date(date_string):
    # Split the date string into month, day, and year
    month, day, year = date_string.split('/')

    # Define lists for month names and suffixes for day
    month_names = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December'
    ]
    day_suffixes = ['st', 'nd', 'rd'] + ['th'] * 17 + ['st', 'nd', 'rd'] + ['th'] * 7 + ['st']

    # Convert the month and day to integers
    month = int(month)
    day = int(day)

    # Generate the verbose date format
    verbose_date = f"{month_names[month - 1]} {day}{day_suffixes[day - 1]}, 20{year}"

    return verbose_date

# Prompt the user for a date
date_input = input("Enter a date in the format mm/dd/yy: ")

# Convert the date to a verbose format
verbose_date = convert_date(date_input)

# Print the verbose date
print(f"The verbose format of {date_input} is {verbose_date}.")