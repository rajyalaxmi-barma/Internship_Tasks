# Problem 12: Capitalize!
# Link: https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    # split on single spaces so extra spaces are kept
    words = s.split(" ")

    new_words = []
    for word in words:
        if word == "":
            new_words.append(word)
        else:
            # make only the first letter capital, keep the rest as it is
            first_letter = word[0].upper()
            rest = word[1:]
            new_words.append(first_letter + rest)

    return " ".join(new_words)


s = input()
result = solve(s)
print(result)
