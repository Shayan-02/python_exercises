def opposite_face(n):
    # Dictionary to store the opposite pairs
    opposite = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    return opposite.get(n, "Invalid input")

# Input
n = int(input())

# Output the opposite face
print(opposite_face(n))
