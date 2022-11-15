def knapsack(wt,val,w,n):
    k = [[0 for x in range(w+1)]for x in range(n+1) ]
    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif wt[i-1] <= j:
                k[i][j] = max(val[i-1]+k[i-1][j-wt[i-1]],k[i-1][j])
            else:
                k[i][j] = k[i-1][j]
    return k[n][w]
    
val = [50,100,150,200]
wt = [8,16,32,40]
w = 64
n = len(val)
print(knapsack( wt, val,w, n))