def issubsetsum(arr,n,sum):
    subset = [[False for x in range(sum+1)]for x in range(n+1)]
    for i in range(n+1):
        subset[i][0] = True
    for i in range(1,sum+1):
        subset[0][i] = False
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1] > j:
                subset[i][j] = subset[i-1][j]
            elif arr[i-1] <= j:
                subset[i][j] = subset[i-1][j] or subset[i-1][j-arr[i-1]]
    return subset[n][sum]
def findpartition(arr,n):
    sum = 0
    for i in arr:
        sum += i
    if sum % 2 != 0:
        return False
    else:
        return issubsetsum(arr,n,sum//2)
arr = [3, 1, 5, 9, 12]
n = len(arr)
 
# Function call
if findpartition(arr, n) == True:
    print("Can be divided into two subsets of equal sum")
else:
    print("Can not be divided into two subsets of equal sum")
     