# Will have to come back to this - can't get code to run properly

# my_functions.py
# This program will contain a function called fibonacci() that will take in a number 
# and return a list containing a Fibonacci sequence of that many numbers. 
# Author: Zoe McNamara Harlowe

import logging
# Configure the logging module
#logging.basicConfig(level=logging.DEBUG)


def fibonacci(number):
    if number < 0: 
        raise ValueError('number must be > 0') 
    if number == 0:
        return []
    
    number = int(input("Please enter a number: "))
    fibonacci_list = [0, 1]
    for i in range(2, number):
        fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
    print(fibonacci_list)
    logging.debug("%d: %s",number, fibonacci_list)
    return fibonacci_list
   

if __name__ == "__main__":

    # Test cases
    return7 = [0, 1, 1, 2, 3, 5, 8]
    return11 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    #logging.debug("%s", fibonacci(7))

    assert fibonacci(7) == return7, 'incorrect return for 7' 
    assert fibonacci(11) == return11, 'incorrect return for 11' 
    assert fibonacci(0) == [], 'incorrect return value for 0' 
    assert fibonacci(1) == [0], 'incorrect return value for 1'

    # Catch a ValueError if a negative number is entered
    try:
        fibonacci(-1)
    except ValueError:
        pass
    else:
        assert False, 'fibonacci missing ValueError'
    print("all good")

