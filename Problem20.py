##Find the sum of the digits in the number 100!

import math
num = 100

#get 100!
fact = math.factorial(int(num))

digitSum = 0

#iterate trhough 100! digits and add to sum
for digits in str(fact):

 digitSum += int(digits)

print(digitSum) 