balance = 10
withdrawal = 50
limit = 40000
special_account = True

print(f"balance {balance} >= withdrawal {withdrawal}: ", balance >= withdrawal)
#false
print(f"withdrawal {withdrawal} <= limit {limit}:", withdrawal <= limit)
#true

#AND
print(f"balance {balance} >= withdrawal {withdrawal} and withdrawal {balance} <= limit {limit}:", balance >= withdrawal and withdrawal <= limit)
#false + true = false
#the both expression need to be true to all expression be true
#one or both expression result in false, all expression will be false

#OR
print(f"balance {balance} >= withdrawal {withdrawal} or withdrawal {balance} <= limit {limit}:", balance >= withdrawal or withdrawal <= limit)
#true
#just one expression need to be true to all expression be true

#DEFAULT COMPARATION
print(f"balance {balance} > withdraw {withdrawal}: ", balance > withdrawal)
#balance is biggest value in comparator withdraw? false

#NOT
print(f"not balance {balance} > withdraw {withdrawal}: ", not balance > withdrawal)
#Balance is not a biggest value in comparator withdraw? true

print(f"(balance {balance} >= withdrawal {withdrawal} or withdrawal {withdrawal} <= limit {limit}) and (special_account {special_account} == True):", (balance >= withdrawal or withdrawal <= limit) and (special_account == True))
#(false or true) and (true)
#true and true = true


#true table
#And
print(f"true and true: ", True and True)
print(f"false and true: ", False and True)
print(f"false and false: ", False and False)
print(f"true and false: ", True and False)

#true
print(f"true or true: ", True or True)
print(f"false or true: ", False or True)
print(f"false or false: ", False or False)
print(f"true or false: ", True or False)



