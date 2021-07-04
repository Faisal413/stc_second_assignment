# gather imputs 
def is_string(input_str):
    if input_str.strip().isdigit():
        print(f"The input value {input_str}  'int'")
    elif input_str.replace(".","").isnumeric():
        s = float(input_str)
        print(f"The input value {input_str}  'float'")
    else:
        print(f"The input value {input_str}  'string'")


str1 = input("Enter string and hit enter :")
is_string(str1)

str2 = input("Enter string and hit enter :")
is_string(str2)
