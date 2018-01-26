'''
Problem
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


My solution...

'''

#Returns True if it is a palimdromic expression
def check_palindromic(num):

    if type(int(num)) != int:
        return False

    exp = str(num)
    exp1, exp2 = exp[:len(exp)//2], exp[len(exp)//2:]
    if exp1 == exp2[::-1]:
        return True
    else:
        return False


#Produce a max palindromic number from a minimum and a maximum
#Have a dependency function
def max_palindromix(min, max):
    for x in range(min, max):

        for y in range(min, max):
            #c = c + 1      #Counts the number of combinaisons, if needed
            #print(x,' X ', y)      #print the possible combinaisons, if needed
            prod = x * y
            if check_palindromic(prod) == True:
                max_pal = prod

    return max_pal

#Run and print the functions
print(max_palindromix(100, 1000))
