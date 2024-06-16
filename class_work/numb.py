# def list_factors(number):
#     factors = []
#     for i in range(1, number + 1):
#         if number % i == 0:
#             factors.append(i)
#     return factors

# number = 12
# factors = list_factors(number)
# print("The factors of", number, "are:", factors)


# for i in range(1, 10):
#     for j in range(1, i + 1):
#         if i % j == 0:
#             factors.append(j)
#             print(factors)

#             sum = array_sum_without_last(factors)
#             print(factors)

#             if sum == i:
#                 print(i)
#             else:
#                 break


def list_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def array_sum_without_last(arr):
    sum = 0
    for i in range(len(arr) - 1):
        sum += arr[i]
    return sum


for i in range(1, 10000+1):
    factors = list_factors(i)
    total = array_sum_without_last(factors)
    if total == i:
        print(i)