n = int(input())
names = [input() for _ in range(n)]

names.sort(key=lambda name: len(set(name)), reverse=True)

selected_name = names[0]

print(len(set(selected_name)))
