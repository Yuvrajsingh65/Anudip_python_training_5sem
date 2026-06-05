# Store all transactions in a list
# Positive values are deposits and negative values are withdrawals
transactions = [5000, -2000, 3000, -1000, -500, 7000]

# -----------------------------
# 1. Calculate Current Balance
# -----------------------------

# Start balance from 0
balance = 0

# Add each transaction to the balance
for amount in transactions:
    balance = balance + amount

# Display the final balance
print("Current Balance =", balance)


# --------------------------------------
# 2. Count Deposits and Withdrawals
# --------------------------------------

# Variables to store the count
deposit_count = 0
withdrawal_count = 0

# Check each transaction
for amount in transactions:

    # If amount is positive, it is a deposit
    if amount > 0:
        deposit_count += 1

    # If amount is negative, it is a withdrawal
    else:
        withdrawal_count += 1

# Display total number of deposits and withdrawals
print("Total Deposits =", deposit_count)
print("Total Withdrawals =", withdrawal_count)


# ------------------------------------------------
# 3. Create Separate Lists for Deposits and Withdrawals
# ------------------------------------------------

# Empty lists to store deposits and withdrawals
deposits = []
withdrawals = []

# Separate transactions into two lists
for amount in transactions:

    # Add positive amounts to deposits list
    if amount > 0:
        deposits.append(amount)

    # Add negative amounts to withdrawals list
    else:
        withdrawals.append(amount)

# Display both lists
print("Deposits List =", deposits)
print("Withdrawals List =", withdrawals)


# -----------------------------------------
# 4. Find Largest Deposit
# -----------------------------------------

# Assume the first deposit is the largest
largest_deposit = deposits[0]

# Compare all deposits one by one
for amount in deposits:
    if amount > largest_deposit:
        largest_deposit = amount

print("Largest Deposit =", largest_deposit)


# -----------------------------------------
# 5. Find Largest Withdrawal
# -----------------------------------------

# Assume the first withdrawal is the largest withdrawal
largest_withdrawal = withdrawals[0]

# Compare all withdrawals
# The most negative value represents the largest withdrawal
for amount in withdrawals:
    if amount < largest_withdrawal:
        largest_withdrawal = amount

print("Largest Withdrawal =", largest_withdrawal)
