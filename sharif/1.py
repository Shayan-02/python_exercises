def most_frequent_char(filename):
    with open(filename, 'r') as file:
        text = file.read()
        char_frequency = {}
        for char in text:
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
        max_frequency = max(char_frequency.values())
        most_frequent_chars = [char for char, frequency in char_frequency.items() if frequency == max_frequency]
        return most_frequent_chars

filename = input("Enter the filename: ")
most_frequent_chars = most_frequent_char(filename)
print("The most frequent character(s) in the file is/are:", str(most_frequent_chars).replace('[', '').replace(']', '').replace("'", ''))