'''
Problem:
Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There is exactly one Pythagorean triplet for which a + b + c = 1000.
Find it.


My solution...

'''

# This will find the pythagorian triplet of a given 'c' value
# Input: the 'c' (last triplet) we want
# Output: the 'a' and 'b' (first 2 triples)

def find_pythagorian_T(c):
    c2 = c ** 2                         # we start by having the square of c
    found = False                       # this flag will stop the loop when the solution is found
    i = 1                               # 'a' increment so that we start the brute force solution finder
    j = 1                               # 'b' increment so that we start the brute force solution finder

    while found == False:
        for i in range(1, c):           # the combinaisons won't go further than 'c', intuitively
            i2 = i**2                   # we go through all 'a' squares
            for j in range(i,i + c):
                j2 = j**2               # we go through all 'b' squares

                if i2 + j2 == c2:       # each time, we compare the sum of 'a' and 'b' with 'c' square
                    #found = True       # for clarity here the flag is in comment, although it is not needed
                    return i, j         # when found, we return the results


# Run and print the result
print(find_pythagorian_T(1000))
