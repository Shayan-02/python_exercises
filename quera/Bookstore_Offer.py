def minimal_price(N, prices):
    # Sort the book prices in descending order
    prices.sort(reverse=True)

    total_cost = 0

    # Process books in groups of 3
    for i in range(0, N, 3):
        total_cost += prices[i]  # First book (most expensive in group)
        if i + 1 < N:
            total_cost += prices[i + 1]  # Second book (second most expensive)
        # The third book (if exists) is free, so skip adding prices[i + 2]

    return total_cost


# Input reading
N = int(input())  # Number of books
prices = list(map(int, input().split()))  # Prices of the books

# Output the result
print(minimal_price(N, prices))
