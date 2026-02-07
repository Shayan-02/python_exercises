# Function to calculate the number of free courses Mina can enroll in
def free_courses(n):
    # Total discount Mina receives
    total_discount = 10 * n
    # Number of courses she can enroll in for free
    free_courses_count = total_discount // 100
    return free_courses_count


# Input: Number of students Mina has referred
n = int(input())

# Output: Number of free courses Mina can enroll in
print(free_courses(n))
