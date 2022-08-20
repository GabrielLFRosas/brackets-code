#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
def isBalanced(brackets):
    # Write your code here
    open_bracket_items = {'(': ')',
                        '[': ']',
                        '{': '}'}

    # Size of the entered string
    length = int(len(brackets))
    if (length%2) != 0: # if odd, return
        return 'NO'

    for index in range(int(length-1)):
        bracket = brackets[index] # Current character
        next_bracket = brackets[index + 1] # Next character
        if bracket in open_bracket_items and not next_bracket in open_bracket_items: 
            if next_bracket != open_bracket_items[bracket] : 
                return 'NO'
          
    return 'YES'


if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')
