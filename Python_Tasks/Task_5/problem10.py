# Problem 10: Swap Case
# Link: https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    result = ""
    for ch in s:
        if ch.islower():
            result = result + ch.upper()
        elif ch.isupper():
            result = result + ch.lower()
        else:
            # digits, spaces, symbols stay the same
            result = result + ch
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
