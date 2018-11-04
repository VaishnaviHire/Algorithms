# Algorithm for Prefix to Postfix:
#
# Read the Prefix expression in reverse order (from right to left)
# If the symbol is an operand, then push it onto the Stack
# If the symbol is an operator, then pop two operands from the Stack
# Create a string by concatenating the two operands and the operator after them.
# string = operand1 + operand2 + operator
# And push the resultant string back to Stack
# Repeat the above steps until end of Prefix expression.
import collections
def infixtopostfix(str1):
    pre = str1[::-1]
    operators = ['+','-','/','*']
    stack =[]
    op1=op2=''
    for i in range(len(pre)):
        if pre[i]  in operators:
            if stack:
                op1 = stack.pop()
            if stack:
                op2 = stack.pop()
            res = op1 + op2 + pre[i]
            stack.append(res)

        else:
            stack.append(pre[i])


    return stack[-1]

def some(arr):
    res = []
    for i in arr:
        res.append(infixtopostfix(i))
    return res

def anagrams(a,b):
    res = []
    for i in range(len(a)):
        if len(a[i]) != len(b[i]):
            res.append(-1)
            continue
        a1 = collections.Counter(a[i])-collections.Counter(b[i])
        res.append(sum(a1.values()))

    return res



print anagrams(['a','jk','abb','mn','abc','abcdefg'],['bb','kj','bbc','op','def','axyzmno'])




print some(['*34','+1*23','+12'])