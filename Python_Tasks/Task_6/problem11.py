# Problem 11: String Formatting
# Link: https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    width = len(bin(number)) - 2

    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]            # [2:] removes the "0o" in front
        hexa = hex(i)[2:].upper()     # [2:] removes the "0x", upper() makes capitals
        binary = bin(i)[2:]           # [2:] removes the "0b" in front

        # rjust() adds spaces on the left to make each value the same width
        print(decimal.rjust(width), octal.rjust(width), hexa.rjust(width), binary.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
