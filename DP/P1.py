# 0/1 knapsack problem with optimization

def knapsack(wt,val,n,w):
    dp = []
    for i in range(n+1):
        dp.append([0]*(w+1))
        
    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i-1] <= j:
                dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][w-wt[j-1]])
            else:
                dp[i][j] = dp[i-1][w-wt[j-1]]
    
    return dp[n][w]

print(knapsack([2,3,1],[1,5,7],3,4))

# Subset sum Problem

# def subset_sum(sum,arr):
#     if sum == 0:
#         return []
#     n = arr.size()
#     if sum > arr[n-1]:
        