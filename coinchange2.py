import sys

def mincoins(coins,n,sum):
    subset = [[0 for x in range(sum+1)]for x in range(n+1)]
    for i in range(n+1):
        subset[i][0] = 0
    for i in range(sum+1):
        subset[0][i] = sys.maxsize-1
    
    for j in range(1,sum+1):
        i = 1
        if j % coins[0] == 0:
            subset[i][j] = j/coins[0]
        else:
            subset[i][j] = sys.maxsize-1

    for i in range(2,n+1):
        for j in range(1,sum+1):
            if coins[i-1] <= j:
                subset[i][j] = min(subset[i][j-coins[i-1]]+1,subset[i-1][j])
            else:
                subset[i][j] = subset[i-1][j]
    return subset[n][sum]

    






coins = [9, 6, 5, 1]
m = len(coins)
V = 11
print("Minimum coins required is",mincoins(coins, m, V))