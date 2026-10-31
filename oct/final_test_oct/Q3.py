text = "ab#c"
left = 0
n = len(text)
good = []

for i in range(n-1):
    if text[i+1]!="#" and text[i]!="#":
        good.append(i)
if text[n-1]!="#":
    good.append(n-1)

result = ""

for ind in good:
    result+=text[ind]

print(result)