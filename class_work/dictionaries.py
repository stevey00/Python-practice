# d = {'A': 'my name is steve'}

# # d[D] = 'I love cats.'

# print(d['A'])

products = {}

ans = 'yes'

while ans == 'yes':
    key = input('enter a name for the product: ')
    key.lower()
    value = int(input('enter a price for the product: '))
    products[key] = value
    val = input('do you want to enter more products: Yes or no? ')
    val.lower()
    ans = val

print('Here are the products: ', list(products.items()))

display = input("enter a product and we will display it's price: ")

if display in products:
    print(products[display])
else:
    print('sorry, product was not found in the list of products')



# collect an amount from the user. if the a product in the dictionary is less than the amount entered display that product.

amt = int(input('Enter an amount and we will display all products with price lower than that amount: '))

print([i for i in products if products[i] < amt])
