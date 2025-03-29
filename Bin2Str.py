binary_string = input("Please enter a binary: ")

ascii_representation = "".join(chr(int(binary, 2)) for binary in binary_string.split())

print(f"Result: {ascii_representation}")
