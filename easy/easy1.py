def length_of_last_word(s):
    words = s.split()
    if words:
        return len(words[-1])
    else:
        return 0

user_input = input("Enter a string: ")

result = length_of_last_word(user_input)
print(f"Length of the last word: {result}")