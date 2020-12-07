# EASY

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

Use a stack and recursion from outside in. 
'''
import collections


def isValid(input) -> bool:

    # Python3 code to Check for  
    # balanced parentheses in an expression 
    open_list = ["[","{","("] 
    close_list = ["]","}",")"] 

    input = list(input)

    if list is None:
        return True

    stack = [] 
    for i in input: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if (len(stack) > 0 and open_list[pos] == stack[len(stack)-1]): 
                stack.pop() 
            else: 
                return "False"

    if len(stack) == 0: 
        return "True"
    else: 
        return "False"

if __name__ == '__main__':

    input = "([dfadfadfadsfafd])"

    result = isValid(input)

    print("Matching paranthesis" if result else "Mismatch")