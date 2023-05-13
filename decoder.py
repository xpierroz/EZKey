"""
THIS IS STILL IN DEVELOPMENT BUT IF U WANNA USE JUST PUT YOUR INT IN THE ENCODED STRING AND RUN THE PROGRAM BABYYYYY
"""


encoded = """

"""
s = encoded.split(" ")
for encoded_int in s:
    decoded_bytes = int(encoded_int).to_bytes((int(encoded_int).bit_length() + 7) // 8, byteorder='big')

    # Decode the bytes object to a string
    decoded_string = decoded_bytes.decode()

    # Print the decoded string
    print(decoded_string)