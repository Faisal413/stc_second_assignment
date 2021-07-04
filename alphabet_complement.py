import string

# gather imputs 
user_input1 = input('Enter any string of letters: ')

if user_input1.isnumeric():
    raise Exception("string of letters does not contain letters")

# create the sets 
user_set1 = set(user_input1.lower())
alphabet = set(string.ascii_lowercase)

print("Letters not used:", "".join(sorted(list(alphabet.difference(user_set1)))))