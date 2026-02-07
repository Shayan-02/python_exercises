# Function to find the person with the most embezzlement
def find_max_embezzlement(n, data):
    max_embezzlement = -1
    max_name = ""

    for entry in data:
        name, amount = entry
        if amount > max_embezzlement:
            max_embezzlement = amount
            max_name = name

    return max_name


# Input reading
n = int(input())  # Number of employees
data = []

# Read the names and amounts of embezzlement
for _ in range(n):
    name, amount = input().split()
    data.append((name, int(amount)))

# Find and print the name of the person with the maximum embezzlement
print(find_max_embezzlement(n, data))
