## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW

import sys


def main():
    ## YOU CODE SHOULD START HERE AST THE SAME
    ## IDENTATION AS THIS COMMENT
    if len(sys.argv) > 1:
        x = int(sys.argv[1])
    else:
        x = int(input("Enter an integer number:"))

    p = divisors(x)
    t = compare(x)
    if p > t:
        return "anti-prime"
    else:
        return "not-anti-prime"
    ## THE LAST LINES OF YOUR CODE SHOULD EITHER
    ## RETURN THE VALUE "anti-prime" or "not anti-prime"
    ## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
    ## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
    ## "anti-prime" or "not anti-prime"


def divisors(a):
    i = 1
    c = 0
    while a >= i:
        if a % i == 0:
            c += 1
        i += 1
    return c


def compare(e):
    j = 0
    h = 1
    while h < e:
        if divisors(h) > j:
            j = divisors(h)
        h += 1
    return j


## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__":
    ## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
    ## TO RUN THIS PROGRAM AS, FOR INSTANCE:
    ## $ python antiprime.py 6
    ## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
    ## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
    print(main())
