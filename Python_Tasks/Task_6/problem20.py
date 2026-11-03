# Problem 20: Validating the Phone Number
# Link: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

n = int(input())

for i in range(n):
    number = input()

    # a valid number: exactly 10 digits and it starts with 7, 8 or 9
    if len(number) == 10 and number.isdigit() and number[0] in "789":
        print("YES")
    else:
        print("NO")
