def max_length_with_k_distinct(s, k):
    char_count = {}
    max_length = 0
    window_start = 0

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in char_count:
            char_count[right_char] = 0
        char_count[right_char] += 1

        while len(char_count) > k:
            left_char = s[window_start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

s = input()
k = int(input())
print(max_length_with_k_distinct(s, k))