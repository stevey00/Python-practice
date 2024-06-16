from random import randint

# l = []

# for i in range(50):
#    l.append(randint(1, 100))
# print(l)

l = [randint(1, 100) for i in range(20)]
print("Here's the list: ",l)

average = sum(l)/len(l)
print('Average: ',average)

print('Smallest value: ', min(l) )
print('Largest value: ', max(l))

l.reverse()
newl = l.copy()
print("Here's the reversed list: ", newl)


# for i in range(len(l)):
#     if l.index(i) == True:
#         print('Yes')
#     else: 
#         print('No')
    
    




# print('There are ', numFive ,' "5s" in this list ')
