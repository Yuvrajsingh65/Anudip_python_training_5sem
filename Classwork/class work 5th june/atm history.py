# List of customer transactions
# Positive values represent deposits
# Negative values represent withdrawals

transactions = [5000, -2000, 3000, -1000, -500, 7000]

# -----------------------------------------
# 1. Calculate the Current Balance
# -----------------------------------------

# Start balance from 0
balance = 0

# Add each transaction to the balance
for amount in transactions:
    balance = balance + amount

# Display the current balance
print("Current Balance =", balance)


# -----------------------------------------
# 2. Count Total Deposits and Withdrawals
# -----------------------------------------

# Variables to count deposits and withdrawals
deposit_count = 0
withdrawal_count = 0

# Check every transaction
for amount in transactions:

    # Positive value means deposit
    if amount > 0:
        deposit_count += 1

    # Negative value means withdrawal
    else:
        withdrawal_count += 1

# Display the counts
print("Total Deposits =", deposit_count)
print("Total Withdrawals =", withdrawal_count)


# -----------------------------------------
# 3. Create Separate Lists for Deposits
#    and Withdrawals
# -----------------------------------------

# Empty lists to store deposits and withdrawals
deposits = []
withdrawals = []

# Separate transactions into two lists
for amount in transactions:

    # Store deposits in deposits list
    if amount > 0:
        deposits.append(amount)

    # Store withdrawals in withdrawals list
    else:
        withdrawals.append(amount)

# Display both lists
print("Deposits List =", deposits)
print("Withdrawals List =", withdrawals)


# -----------------------------------------
# 4. Find Largest Deposit
# -----------------------------------------

# Assume first deposit is the largest
largest_deposit = deposits[0]

# Compare all deposits
for amount in deposits:
    if amount > largest_deposit:
        largest_deposit = amount

print("Largest Deposit =", largest_deposit)


# -----------------------------------------
# 5. Find Largest Withdrawal
# -----------------------------------------

# Assume first withdrawal is the largest withdrawal
largest_withdrawal = withdrawals[0]

# Compare all withdrawals
# More negative value means larger withdrawal
for amount in withdrawals:
    if amount < largest_withdrawal:
        largest_withdrawal = amount

print("Largest Withdrawal =", largest_withdrawal)
