import random
import webbrowser
cronologia = {}
coda = [">", ":", ";", "<", "-", "~", "hi"]
tips = ["you can type 'quit' to quit", "eating uranium is an extremely good idea!", "C is superior to C++", "Imagine using windows, cant be me", "Git Gud", "The cake is a lie", 'print("im pretty sure im writing this wrong")', "Im genunely convinced that Artemis 13 is peak", "Domain Expansion: Infinite Random bs", 'helloworld("print") \n \n Syntax Error: Never code again']
ragebait = ["NaN", "NiK (Not like i Know)", "I dont know, just do it manually, man", "Syntax Error: im Lazy", "Theres a bug that doesnt let me calculate, its so hidden even i cant find it", "No." ]
incalculation = True
usedcoda = random.choice(coda)
print(random.choice(tips))
print("\n Welcome to PieCalc")
while incalculation is True:
    action = input(usedcoda)
    if action == "quit":
        print("Why whould you quit? its not like this program is useless")
        print("U sure you wanna quit? this will remove 10 points from the happyness of PieCalc")
        quitchoice = input("Press 1 if ur good and wanna stay, press 2 if you are bad and wanna quit \n" + usedcoda)
        if quitchoice == "2":
            webbrowser.open("rickroll.it")
            incalculation = False
            print("Your actions will be remembered...")
        else:
            print("You stayin'? lets go!")
    else:
        print(random.choice(ragebait))