pattern = [0]*360
freq = [0]*360
p= "ab"
text = "eidbaooo"
found = False
for i in range(len(p)):
    pattern[ord(p[i])]+=1
left = 0
for i in range(len(text)):
    freq[ord(text[i])]+=1
    while freq[ord(text[i])]>pattern[ord(text[i])] and left<len(text):
        freq[ord(text[left])]-=1
        left+=1

    if i-left+1==len(p):
        found=True
        print("True")
if not found :
    print("False")
