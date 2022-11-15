def issubsetsum(arr,n,sum):
    if sum == 0 :
        return True
    if n ==0 :
        return False
    if arr[n-1] > sum :
        return issubsetsum(arr,n-1,sum)
    return issubsetsum(arr,n-1,sum-arr[n-1]) or issubsetsum(arr,n-1,sum)
def findpartition(arr,n):
    sum = 0
    for i in range(n):
        sum += arr[i]
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
     