def bfs(graph, police_city, thief_city):
    queue = [(police_city, 0)]  # (current city, day)
    visited = set([police_city])

    while queue:
        current_city, day = queue.pop(0)

        # If police catches the thief
        if current_city == thief_city:
            if police_city == thief_city:
                return 0  # Return half the days because of the day-night cycle
            else:
                return day // 2 + 1 # Return half the days because of the day-night cycle

        # Explore neighbors
        for neighbor in graph[current_city]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, day + 1))

    return -1  # If the thief can't be caught


def solve_fano(police_city, thief_city, roads):
    # Create a graph with cities as nodes
    graph = {i: [] for i in range(1, 8)}  # Cities 1 through 7
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)

    # Find the minimum number of days
    return bfs(graph, police_city, thief_city)


# Input example
police_city = int(input())  # Starting city for the police
thief_city = int(input())  # Starting city for the thief
roads = [
    (1, 2),
    (1, 3),
    (1, 4),
    (2, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (3, 4),
    (3, 6),
    (3, 7),
    (4, 5),
    (4, 6),
    (4, 7),
    (5, 6),
    (6, 7)
]  # Roads connecting cities

# Solve the problem
result = solve_fano(police_city, thief_city, roads)
print(result if result != -1 else -1)
