def decode_encoded_string(stringsplit):
    # Split the encoded string using underscores
    parts = stringsplit.split('_')
    
    # Assuming the order is: name, domain name, register number
    if len(parts) != 3:
        return None  # Return None if the string doesn't have all three parts
    
    # Creating a dictionary with keys 'name', 'domain', and 'register'
    decoded_dict = {
        'Name': parts[0],
        'Domain': parts[1],
        'Register': parts[2]
    }
    
    return decoded_dict

# Output 
encoded_string = "Priya Dharshini_Pets care Management_2347247"
Output = decode_encoded_string(encoded_string)
if Output is not None:
    print(Output)
else:
    print("Not Defined")
