#int to float
int_number = 10.50
number_int_to_float = float(int_number)
print("The int value: ", int_number, " float value: ", number_int_to_float)

#int to string
#convertion by function
number_int_to_string = str(int_number)
print("The int value: ", int_number, " string value: ", number_int_to_string)


#convertion by string and variable concatenation
print(f"The int value: {int_number}")

#convertion string to int
print("The int value to string:", int("100"))
print("The type of value:", type(int("100")))