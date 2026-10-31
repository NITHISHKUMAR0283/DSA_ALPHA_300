prices = [7,1,5,3,6,4]

tot_profit = 0
length = len(prices)
for i in range(1,length):
    curr = prices[i]-prices[i-1]
    if curr>0:
        tot_profit+=curr
print(tot_profit)