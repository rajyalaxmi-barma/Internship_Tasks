# Problem 10: Designer Door Mat
# Link: https://www.hackerrank.com/challenges/designer-door-mat/problem

n, m = input().split()
n = int(n)
m = int(m)

# top half of the mat
for i in range(1, n, 2):
    pattern = ".|." * i
    # center() puts the pattern in the middle and fills the sides with "-"
    print(pattern.center(m, "-"))

# middle line
print("WELCOME".center(m, "-"))

# bottom half of the mat (same as the top half, upside down)
for i in range(n - 2, 0, -2):
    pattern = ".|." * i
    print(pattern.center(m, "-"))
