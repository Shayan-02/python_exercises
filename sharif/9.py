def count_pronunciations(word):
    # Define the set of English letters allowed
    english_vowels = set('aeiou')

    # Initialize pronunciation count
    pronunciation_count = 1

    # Iterate through each character in the word
    for char in word:
        if char in english_vowels:
            pronunciation_count *= 2


    return pronunciation_count

# Sample input and output
input_word = input()
output = count_pronunciations(input_word)
print(output)  # Expected output: 4
