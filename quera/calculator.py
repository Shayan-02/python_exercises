def calculate_floor(moves):
    floor = 0
    for move in moves:
        if move == "U".lower():
            floor += 1
        elif move == "D".lower():
            floor -= 1
    return floor


moves = input()
print(calculate_floor(moves))
