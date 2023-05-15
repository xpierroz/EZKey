"""
THIS IS STILL IN DEVELOPMENT BUT IF U WANNA USE JUST PUT YOUR INT IN THE ENCODED STRING AND RUN THE PROGRAM BABYYYYY
"""


encoded = """

"""
string = ""
for _encoded_int in encoded.split("\n"):
    for encoded_int in _encoded_int.split(" "):
        if encoded_int == "":
            continue
        decoded_bytes = int(encoded_int).to_bytes((int(encoded_int).bit_length() + 7) // 8, byteorder='big')

        # Decode the bytes object to a string
        decoded_string = decoded_bytes.decode()

        string += f" {decoded_string} |"
        
print(string)