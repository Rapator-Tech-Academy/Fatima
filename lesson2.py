print("Cities I should visit")

NextDestination = ['tokyo', 'berlin', 'amsterdam', 'london', 'new york', 'istanbul']

# in, not in

cityName = 'tokyo', 'berlin', 'amsterdam', 'london', 'new york', 'istanbul'

cityName = input("Choose your first destanation: ")

if cityName in NextDestination:
  print(f'{cityName} is Your Next Destinaton')


#while
""""
i=0

while len(NextDestination) >= i:
    print(NextDestination[i])
    i +=1

"""
#for
"""
for cityName in NextDestination:
    print(cityName)
"""

"""
your_next_destination = input("Choose where to go next: ")

for cityName in NextDestination:
    if cityName == your_next_destination:
        print(f'{cityName} you go next')
        break
"""