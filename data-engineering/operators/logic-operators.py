balance = 10
WITHDRAWL = 50
LIMIT = 40000
SPECIAL_ACCOUNT = True

print(f"balance {balance} >= WITHDRAWL {WITHDRAWL}: ", balance >= WITHDRAWL)
# false
print(f"WITHDRAWL {WITHDRAWL} <= LIMIT {LIMIT}:", WITHDRAWL <= LIMIT)
# true

# AND
print(
    f"balance {balance} >= WITHDRAWL {WITHDRAWL} and WITHDRAWL {balance} <= LIMIT {LIMIT}:",
    balance >= WITHDRAWL and WITHDRAWL <= LIMIT,
)
# false + true = false
# the both expression need to be true to all expression be true
# one or both expression result in false, all expression will be false

# OR
print(
    f"balance {balance} >= WITHDRAWL {WITHDRAWL} or WITHDRAWL {balance} <= LIMIT {LIMIT}:",
    balance >= WITHDRAWL or WITHDRAWL <= LIMIT,
)
# true
# just one expression need to be true to all expression be true

# DEFAULT COMPARATION
print(f"balance {balance} > withdraw {WITHDRAWL}: ", balance > WITHDRAWL)
# balance is biggest value in comparator withdraw? false

# NOT
print(f"not balance {balance} > withdraw {WITHDRAWL}: ", not balance > WITHDRAWL)
# Balance is not a biggest value in comparator withdraw? true

print(
    f"(balance {balance} >= WITHDRAWL {WITHDRAWL} or WITHDRAWL {WITHDRAWL} <= LIMIT {LIMIT}) and (SPECIAL_ACCOUNT {SPECIAL_ACCOUNT} == True):",
    (balance >= WITHDRAWL or WITHDRAWL <= LIMIT) and (SPECIAL_ACCOUNT == True),
)
# (false or true) and (true)
# true and true = true


# true table
# And
print("true and true: ", True and True)
print("false and true: ", False and True)
print("false and false: ", False and False)
print("true and false: ", True and False)

# true
print("true or true: ", True or True)
print("false or true: ", False or True)
print("false or false: ", False or False)
print("true or false: ", True or False)
