#! usr/bin/python

print 'Content-type: text/html'
print ''

numberOfPrime = 0
number = 2

while numberOfPrime <= 1000 :
  isPrime = True
  for i in range (2, number):
    if number % i == 0 :
      isPrime = False
      
  if isPrime == True :
    print number
    numberOfPrime += 1

  number += 1
