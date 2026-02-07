def process_letter(n, m, s, rules):
    state = 1  # Initial state
    rules_dict = {}

    # Convert rules into a dictionary for quick lookup
    for rule in rules:
        v, u, c = rule.split()
        v, u = int(v), int(u)
        if v not in rules_dict:
            rules_dict[v] = {}
        rules_dict[v][c] = u

    # Process the letter
    while s and state in rules_dict and s[0] in rules_dict[state]:
        state = rules_dict[state][s[0]]
        s = s[1:]

    return s if s else "-1"


# Input
n, m = map(int, input().split())
s = input().strip()
rules = [input().strip() for _ in range(m)]

# Process and output the result
result = process_letter(n, m, s, rules)
print(result)
