import re

def minion_game(string):
    strlen = len(string)
    kev_score = 0
    stuart_score = 0
    for i in range(strlen):
        if re.search("[AEIOU]", string[i]):
            kev_score = kev_score + strlen -i
        else:
            stuart_score = stuart_score + strlen - i
    if kev_score > stuart_score:
        print('Kevin '+str(kev_score))
    elif stuart_score > kev_score:
        print('Stuart '+ str(stuart_score))
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)


# Kevin and Stuart want to play the 'The Minion Game'.
#
# Game Rules
#
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#A player gets +1 point for each occurrence of the substring in the string
# https://www.hackerrank.com/challenges/the-minion-game/problem