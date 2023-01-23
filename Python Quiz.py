import random


print ("Welcome to my first python quiz")
play = input('Are you ready to play? ')

if play != "yes":
    quit()
print("Alright lets play")

A1 = input('What is the capital of the United States?')

if A1 == "Washington, DC":
    print("You're right!!")
else:
    print("You're a dumb son of a bitch")
    print("Sorry for being harsh here is a present!")
    rand = random.randint(1,300)
    print("$", rand)
    rehit = input('Was your present sufficient?' )
    

