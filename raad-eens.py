import random
print("Raad het getal tussen 1 en 1000") 
guess = -1 
ronde = 1 
point = 0 
while ronde <= 20: 
    print("Ronde " + str(ronde))
    number = random.randint(1,1000)
    kans = 1  
    while number != guess:
        guess = int(input(str(kans) + ": "))
        if guess < number:
            print("Hoger")
            if (number - guess) <= 20:
                print("Je bent heel warm")
            elif (number - guess) <= 50:
                print("Je bent warm")
        elif guess > number:
            print("Lager")
            if (guess - number) <= 20: 
                print("Je bent heel warm")
            elif (guess - number) <= 50:
                print("Je bent warm")
        else: 
            print("Correct")
            point = point + 1
        kans = kans + 1
        if kans > 10:
            break
    print("Het getal was " + str(number))
    if ronde >= 20:
        break  
    print("Points: " + str(point))
    print("Nog een getal raden? Ja/Nee")
    antwoord = input("")
    if not (antwoord == "Ja" or antwoord == "ja"):
        break
    ronde = ronde + 1
print("Einde!")
print("Uw eindscore is " + str(point))



    
        
    
