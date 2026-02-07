def find_room_dimensions(R, B):
    # Iterate through possible values for L and W
    for L in range(1, 2001):
        for W in range(L, 2001):  # Ensure W >= L as per the problem requirement
            # Calculate the number of black blocks for this (W, L)
            calculated_R = 2 * (W + L) - 4
            # Calculate the number of yellow blocks for this (W, L)
            calculated_B = W * L - calculated_R
            # Check if it matches the given R and B
            if calculated_R == R and calculated_B == B:
                return W, L


# Input
R, B = map(int, input().split())

# Find the dimensions of the room
W, L = find_room_dimensions(R, B)

# Output the result, larger number first
print(max(W, L), min(W, L))
