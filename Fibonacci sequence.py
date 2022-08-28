# Python dla początkujących, Rafał Mobilo course, 107. For Loop - LAB
# Student: Łukasz Świątek Brzeziński
# Program gives fibonnacci sequence from the number of element you input.

#1
##a1 = 0
##a2 = 1
##a3 = a1 + a2

fibonacciIterations = int(input("Type the integer number the Fibonacci \
sequence should be given: "))
fibonacciSequence = []
for element in range(0, fibonacciIterations):
    if element == 0:
        fibonacciResult = element
        fibonacciSequence.append(fibonacciResult)
    elif element == 1:
        fibonacciResult = fibonacciSequence[element-1] + element
        fibonacciSequence.append(fibonacciResult)
    else:
        fibonacciResult = fibonacciSequence[element-2] + fibonacciSequence[element-1]
        fibonacciSequence.append(fibonacciResult)
    
   
print("your Fibonacci sequence is: \n", fibonacciSequence)
