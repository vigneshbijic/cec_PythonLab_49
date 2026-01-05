import math
import random
import datetime
random_number=random.randint(1,100)
print("Random number between 1 and 100: {}".format(random_number))
current_datetime=datetime.datetime.now()
print("Current date and time: {}".format(current_datetime))
number=int(input("Enter a number: "))
square_root=math.sqrt(number)
print("The square root of {} is: {}".format(number,square_root))
