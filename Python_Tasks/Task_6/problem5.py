# Problem 5: Write a Function
# Link: https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = False

    # a year divisible by 4 is a leap year ...
    if year % 4 == 0:
        leap = True
        # ... except century years (divisible by 100) ...
        if year % 100 == 0:
            leap = False
            # ... unless they are divisible by 400
            if year % 400 == 0:
                leap = True

    return leap


year = int(input())
print(is_leap(year))
