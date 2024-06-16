from random import randint

dice = [(2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),(0,0,0,0,0,0,0,0,0,0,0)]



for x in range(1,10001):
        t1 = randint(1,6)
        t2 = randint(1,6)
        # print(t1," ",t2)
        val = t1+t2
        print(val)
        for i in range(0,1):
            for j in range(0,11):
                count = 0
                cpr = dice[i][j]
                if cpr == val:
                  count += 1


# print(val, " = ", count)