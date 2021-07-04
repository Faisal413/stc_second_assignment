# gather imputs 
user_str = input('Enter any string of letters: ')

if user_str.isnumeric():
    raise Exception("string of letters does not contain letters")
    
print("".join([l for l in user_str if l not in ['a','e','i','o','u']]))