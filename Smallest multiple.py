'''
Problem:

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


My solution...

'''



#Returns True if the modulus of a number is 0 for a serie of numbers
#inputs : number to check, min range, max range
def check_if_modulus_is_zero(num, min, max):

    flag = True
    i = min
    while flag == True and i <= max:
        if num % i != 0:
            flag = False

        i = i + 1

    return flag

#Increment until the range is fully checked
#Inputs : minimum range, maximum range
def until_modulus_range(min, max, starting):


    current = starting   										#start with the max

    flag2 = False
    while flag2 == False:

        flag2 = check_if_modulus_is_zero(current,min,max)
        current += 1    										#increment

    return current - 1

#This accelerates the process as it start with the previous max product
def optimise_until(min, max):
    preceding = max
    for i in range (min, max + 1):
        preceding = until_modulus_range(min, i, preceding)

    return preceding

	
print('Running...')
print(optimise_until(1, 18))
print('Completed!')
