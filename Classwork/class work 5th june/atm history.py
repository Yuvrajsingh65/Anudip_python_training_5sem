# List of transactions
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# 1. Calculate current balance
balance = sum(transactions)
print("Current Balance =", balance)

# 2. Count deposits and withdrawals
deposit_count = 0
withdrawal_count = 0

for amount in transactions:
    if amount > 0:
        deposit_count += 1
    else:
        withdrawal_count += 1

print("Total Deposits =", deposit_count)
print("Total Withdrawals =", withdrawal_count)

# 3. Find largest deposit and largest withdrawal
deposits = []
withdrawals = []

for amount in transactions:
    if amount > 0:
        deposits.append(amount)
    else:
        withdrawals.append(amount)

largest_deposit = deposits[0]
for amount in deposits:
    if amount > largest_deposit:
        largest_deposit = amount

largest_withdrawal = withdrawals[0]
for amount in withdrawals:
    if amount < largest_withdrawal:
        largest_withdrawal = amount

print("Largest Deposit =", largest_deposit)
print("Largest Withdrawal =", largest_withdrawal)

# 4. Display separate lists of deposits and withdrawals
print("Deposits List =", deposits)
print("Withdrawals List =", withdrawals)
