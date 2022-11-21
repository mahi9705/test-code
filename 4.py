def FindSubMatrix(mat):
    r = len(mat)
    cl = len(mat[0])
 
    temp = []
    for i in range(r):
        temp1 = []
        for j in range(cl):
            if i == 0 or j == 0:
                temp1 += mat[i][j],
            else:
                temp1 += 0,
        temp += temp1,

    for i in range(1, r):
        for j in range(1, cl):
            if (mat[i][j] == 0):
                temp[i][j] = min(temp[i][j-1], temp[i-1][j],temp[i-1][j-1]) + 1
            else:
                temp[i][j] = 0

    mv = temp[0][0]
    mii = 0
    mj = 0
    for i in range(r):
        for j in range(cl):
            if (mv < temp[i][j]):
                mv = temp[i][j]
                mii = i
                mj = j
 
    print(tuple((mii-mv,mj)),',',tuple((mii-mv,mj+mv)),',',tuple((mii,mj)),',',tuple((mii,mj+mv))) 
 
n=int(input())
mat=[list(map(int,input().split())) for i in range(n)]
 
FindSubMatrix(mat)