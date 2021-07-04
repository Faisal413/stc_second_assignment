import string

# gather imputs

# determine if we are encodeng or decoding 
encode_decode = input("Enter 'encode' or 'decode' to determine the mode: ")

if 'encode' in encode_decode.lower():
    encode = True
    user_input = input("Enter the string to 'encode': ")
elif 'decode' in encode_decode.lower():
    encode = False
    user_input = input("Enter the string to 'decode': ")
else:
    raise Exception("Could not determine if it is 'encode' or 'decode'")

## build an encoder and a decoder
encoder = {letter:str(i).zfill(4) for i,letter in enumerate(string.printable)}
decoder = {str(i).zfill(4):letter for i,letter in enumerate(string.printable)}

print("#"*35)
print("USER INPUT: ",  user_input)

if encode:
    print("ENCODED OUTPUT: ",  "".join([encoder[c]  for c in user_input]))
else:
    user_input_chunks = [user_input[i:i+4] for i in range(0, len(user_input), 4)]
    print("DECODED OUTPUT: ", "".join([decoder[c]  for c in user_input_chunks]))