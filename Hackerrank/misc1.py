import os
# fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

# result = diagonalDifference(arr)

# fptr.write(str(result) + '\n')

# fptr.close(3
# )
print(arr)

sum1 = 0
sum2 = 0
for i,j in zip(arr,range(len(arr))):
    # print(i)
    
    sum1 = sum1 + i[j]

for i,j in zip(arr,range(len(arr)-1,-13,-1)):
    sum2 = sum2 + i[j]
    
print(sum1)
print(sum2)
print(abs(sum1-sum2))