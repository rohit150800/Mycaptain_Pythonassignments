"""def most_frequency(string):
    d=dict()
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    return d
    sorted_freq = sorted(key.items(),key=lambda x:x[1],reverse=True)
    for char,freq in sorted_freq:
        print("f{char}:{freq}")
print(most_frequency("Mississippi"))"""



def most_frequent(input_string):
    # Create an empty dictionary to store letter frequencies
    letter_freq = {}

    # Convert the input string to lowercase to treat uppercase and lowercase letters as the same
    input_string = input_string.lower()

    # Iterate through the string and count letter frequencies
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            if char in letter_freq:
                letter_freq[char] += 1
            else:
                letter_freq[char] = 1

    # Sort the dictionary items by frequency in descending order
    sorted_freq = sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)

    # Print the letters in decreasing order of frequency
    for char, freq in sorted_freq:
        print(f"{char}: {freq}")

# Example usage:
input_string = "Mississippi"
most_frequent(input_string)
