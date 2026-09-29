# Number of Ways to Make Change

# Accept coin denominations
coins = list(map(int, input("Enter coin denominations: ").split()))

# Accept target amount
amount = int(input("Enter target amount: "))

# Create DP table
dp = [0] * (amount + 1)

# There is 1 way to make amount 0: choose no coins
dp[0] = 1

# Calculate number of combinations
for coin in coins:
    for i in range(coin, amount + 1):
        dp[i] = dp[i] + dp[i - coin]

# Display result
print("Total possible combinations:", dp[amount])


'''
Enter coin denominations: 2
Enter target amount: 4
Total possible combinations: 1
'''