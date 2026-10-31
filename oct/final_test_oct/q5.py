arr = [1,2,1]
n  = len(arr)
stack = []
arr = arr[:]+arr[:]
result = [-1] * (2*n)

for i in range(2*n):
    while len(stack)>0 and stack[-1][0]<arr[i]:
        top = stack[-1]
        stack.pop()
        ind = top[1]
        result[ind]=arr[i]
    stack.append((arr[i],i))
print(result[:n])