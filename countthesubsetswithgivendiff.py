def issubsetsum(arr,n,sum):
    subset = [[0 for x in range(sum+1)]for x in range(n+1)]
    for i in range(n+1):
        subset[i][0] = 1
    for i in range(1,sum+1):
        subset[0][i] = 0
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1] > j:
                subset[i][j] = subset[i-1][j]
            if arr[i-1] <= j:
                subset[i][j] = subset[i-1][j] + subset[i-1][j-arr[i-1]]
            
    return subset[n][sum]


def countsubdiff(arr,diff,n):
    sum = 0
    for i in arr:
        sum += i
    s1 = (diff + sum)//2
    return issubsetsum(arr, n, s1)

set = [1,1,2,3]
diff = 1
n = len(set)
print(countsubdiff(set, diff, n))
