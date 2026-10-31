arr= [3,2,2,3]
left = 0
val = 3
n = len(arr)

for i in range(n):
    if arr[i]!=val:
        arr[i],arr[left] = arr[left],arr[i]
        left+=1
arr[:] = arr[:left]

print(left-1)

print(arr)