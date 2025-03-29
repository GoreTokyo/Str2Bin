input_string = input("Please enter a string: ")

binary_representation = " ".join(format(ord(char), "08b") for char in input_string)

print(f"Result: {binary_representation}")
