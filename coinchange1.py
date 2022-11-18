def count(coins,n,sum):
    subset = [[0 for i in range(sum+1)]for i in range(n+1)]
    for i in range(n+1):
        subset[i][0] = 1
    for i in range(1,sum+1):
        subset[0][i] = 0

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if coins[i-1] <= j:
                subset[i][j] = subset[i-1][j] + subset[i][j-coins[i-1]]
            else:
                subset[i][j] = subset[i-1][j]
    return subset[n][sum]






coins = [1, 2, 3]
n = len(coins)
sum = 4
print(count(coins, n, sum))