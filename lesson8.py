#map (function, iterable,...)

def calculateSquare(n):
    return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)

numberSquare = list(result)
print(numberSquare)

result = map(lambda x: x*x*x, numbers)
numbers= set(result)
print(numbers)


num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print (list(result))

#filter
alphabet = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if (alphabet in vowels):
        return True
    else:
        return False
    
filterVowels = filter(filterVowels, alphabet)

print('The filtered vowels are: ')
for vowels in filterVowels:
    print(vowels)

