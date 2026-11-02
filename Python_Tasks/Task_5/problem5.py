# Problem 5: String Validators
# Link: https://www.hackerrank.com/challenges/string-validators/problem

s = input()

# start with False, change to True if we find at least one match
has_alnum = False
has_alpha = False
has_digit = False
has_lower = False
has_upper = False

for ch in s:
    if ch.isalnum():
        has_alnum = True
    if ch.isalpha():
        has_alpha = True
    if ch.isdigit():
        has_digit = True
    if ch.islower():
        has_lower = True
    if ch.isupper():
        has_upper = True

print(has_alnum)
print(has_alpha)
print(has_digit)
print(has_lower)
print(has_upper)
