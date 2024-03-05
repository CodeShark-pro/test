def find_most_repeated_character(input_string):
   
    char_count = {}

    # Iterate through each character in the input string
    for char in input_string:
        # Increment the count for the character if it's already in the dictionary
        # Otherwise, initialize to 1
        char_count[char] = char_count.get(char, 0) + 1

    max_count = max(char_count.values())

    most_repeated_chars = []

    # character gin rhe
    for char, count in char_count.items():
        # If the count is equal to the maximum count, add the character to the list
        if count == max_count:
            most_repeated_chars.append(char)

    return most_repeated_chars, max_count

user_input = input("Enter a string: ")

#function call yeh h
most_repeated_chars, max_count = find_most_repeated_character(user_input)

print("Most repeated character(s):", most_repeated_chars)
print("Count of most repeated character(s):", max_count)
