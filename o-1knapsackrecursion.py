def knapsack(wt,val,w,n):
   if w==0 or n == 0:
      return 0
   if wt[n-1] <= w:
      return max(val[n-1]+knapsack(wt,val,w-wt[n-1],n-1),knapsack(wt,val,w,n-1))
   else:
      return knapsack(wt,val,w,n-1)

val = [50,100,150,200]
wt = [8,16,32,40]
w = 64
n = len(val)
res=knapsack(wt,val,w,n)
print(res)