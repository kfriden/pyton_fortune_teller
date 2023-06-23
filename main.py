#Kaitlyn Friden 2/12/2020 kaitlyn_fortune.py
#Python program that acts like a cootie catcher, asks to pick a number, then a color, and spits back lines from a text file
#!/usr/bin/python

import random
import time

fo = open("fortune.txt","r")  #this is telling the program to open the text file fortune.txt and read it
x=1
while x == 1:
    y = int(input("Pick a number between 1 and 6.. ")) #input needs to be an integer between 1 and 6
    if y == 1:
        for z, line in enumerate(fo):  #for and if statements that print out each line in the text file in order from top to bottom
            if z == 0:  #choose the first line in the text file
                print(line)
        time.sleep(3)  #wait 3 seconds until the next command
    elif y == 2:
        for z, line in enumerate(fo):
            if z == 1:
                print(line)
        time.sleep(3)
    elif y == 3:
        for z, line in enumerate(fo):
            if z == 2:
                print(line)
        time.sleep(3)
    elif y == 4:
        for z, line in enumerate(fo):
            if z == 3:
                print(line)
        time.sleep(3)
    elif y == 5:
        for z, line in enumerate(fo):
            if z == 4:
                print(line)
        time.sleep(3)
    elif y == 6:
        for z, line in enumerate(fo):
            if z == 5:
                print(line)
        time.sleep(3)
    
    sel = input("Pick a color you like: ")
    time.sleep(3)
    x = ["You will prevail at anything you set your mind to.", "You like cheesecake?? SO DO I!", "Stay focused, and you will soon be on the path to greatness.", "Uh oh, 404 fortune error..", "Time heals all wounds, be patient, you're doing great", "Good vibes are being sent your way, keep being yourself!"] 
    #x is an array containing sentences that get chosen at random to be printed below

    if sel != "":
        print("Gimme a sec to think on this..")
        time.sleep(5)
        x = random.choice(x)  #each time you run through the program, x will be chosen from the array at random and be different every time
        print("Your fortune is..", x)
        saveFile = open('myfortune.txt', 'w')  #creates a file called myfortune.txt 
        saveFile.write(x) #writes your random fortune x to the text file
        saveFile.close() #closes the file after writing to it
        time.sleep(5)
        print("Thanks for playing! Come back soon for another fortune.")
        

    


