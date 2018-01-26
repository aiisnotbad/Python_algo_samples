'''
Problem:

The 10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

My solution ...

'''


import datetime as dt           #This is to test the performance of the algorithm

#check if a number is prime, return True if it's a prime number
#input: the number to check
def check_if_prime(num):
    flag = True                                 #start with the True assomption to open the loop
    i = 2                                       #start with the smallest prime
    while flag == True and i < (num/2 + 1):     #Here we devide by 2 so that we never calculate for no reason
        if num % i == 0:
            flag = False
        i = i + 1

    return flag

# This will increment until the corresponding prime is reach, using the previous function
# Input: the position of the primer number we want
# Output: the requested prime number
def increment_until_prime(pos):
    i = 0
    current = 2

    while i < pos:                              # Increment until pos is reach

        if check_if_prime(current) == True:
            i = i + 1
        current = current + 1

    return current - 1



pos = 10001                                                       #The position of the prime we want

a = dt.datetime.now()                                            # Time mark to check performance
# Run the functions and print the result
print('The', pos, 'th prime number is:', increment_until_prime(pos))
b = dt.datetime.now()                                            # Time mark to check performance


print('It took',(b-a).total_seconds(),'seconds to process.')    # Print the performance result
