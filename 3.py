def upsideDownEqual(S):
    for i in range(len(S)):
        if (S[i] not in ('0', '1', '2', '5', '6','8','9')):
            return "No"
    return "Yes"
 
input1 = int(input())
count = 0
for i in range(1,1000):
    if (upsideDownEqual(str(i)) == 'Yes'):
        res = i
        count = count+1
    if count==input1:
        break
print(res)