def issubsetsum(arr,n,sum):
    subset = [[0 for i in range(sum+1)]for i in range(n+1)]

    for i in range(n+1):
        subset[i][0] = 1
    for i in range(1,sum+1):
        subset[0][i] = 0
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1] > j:
                subset[i][j] = subset[i-1][j]
            if  arr[i-1] <= j:
                subset[i][j] = subset[i-1][j] + subset[i-1][j-arr[i-1]]


    return subset[n][sum]

set = [2,3,5,6,8,10]
sum = 10
n = len(set)
print(issubsetsum(set,n,sum))
