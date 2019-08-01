"""# The Factors funtion gives all factors of a number
def Factors(number):
    number = abs(number)
    listOfFactors = []

    for i in range(1,number+1):
        if number % i == 0:
            listOfFactors.append(i)

    return listOfFactors

#The counToN counts from 1 to a number
def countToN(num2):
    num2 = abs(num2)
    
    for j in range(1,num2+1):
        print j

#The input variables
m = raw_input("Enter an integer ")
m = int(m)

n = raw_input("Enter an integer ")
n = int(n)

#Function calls
print Factors(m)
countToN(n)
"""

def CharacterCount():
    word = raw_input("Enter a string ")
    d = {}

    for i in word:
        if d.has_key(i):
            d[i]= d[i] + 1
        else:
            d[i] = 1
print d

CharacterCount()