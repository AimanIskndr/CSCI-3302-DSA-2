coins = [6, 5, 1]
change = int(input())

cnt = 0
i = 0
while change != 0:
    cnt += change // coins[i]
    change -= coins[i] * (change // coins[i])
    i += 1


print(cnt)
#  input: 119 | output: 20
#  input: 19 | output: 4
