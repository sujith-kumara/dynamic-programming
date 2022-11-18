def rod(length,price,n,size):
    k = [[0 for x in range(n+1)]for x in range(size+1)]
    for i in range(size+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                k[i][j] = 0
            if length[i-1] <= j:
                k[i][j] = max(price[i-1]+k[i][j-length[i-1]],k[i-1][j])
            else:
                k[i][j] = k[i-1][j]

    return k[size][n]






length = [1,2,3,4,5,6,7,8]
price = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(price)
n = size
print(rod(length,price,n,size))