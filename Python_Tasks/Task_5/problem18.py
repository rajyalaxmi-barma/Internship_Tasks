# Problem 18: The Minion Game
# Link: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = "AEIOU"
    stuart = 0   # score of Stuart (substrings starting with a consonant)
    kevin = 0    # score of Kevin (substrings starting with a vowel)
    length = len(string)

    # a letter at position i starts (length - i) different substrings
    for i in range(length):
        if string[i] in vowels:
            kevin = kevin + (length - i)
        else:
            stuart = stuart + (length - i)

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
