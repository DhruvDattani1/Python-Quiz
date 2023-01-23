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
A2 = input('Whats 25 times 25? ')

if A2 == "625":
    print("nice you get nothing")
    print("My quiz has ended")
    exit()
else:
    print("Damn you get one more chance with a final questions")



    
        

    


