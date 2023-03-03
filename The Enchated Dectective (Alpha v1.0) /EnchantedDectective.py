#Starting Notes (Stable)

print("The Enchanted Detectice (A Python Based Decison Game)")
print("")
print(" ¬ Use Python 3.14 in Fullscreen for the best experience")
print(" ¬ *But most text editors are completely compatible too i personally prefer you to use VS Code tho")


EnteredContinue0 = 0.0
EnteredContinue1 = 0.0
EnteredContinue2 = 0.0

SelectOption1 = "Type a Letter Between A to D To Select a Option ¬ "
Selectoption1wrong = "Please Enter a Letter Between A to D To Select a Option Again! (in Higherkey) ¬ "

PressEnter_Var = "Press Enter to Continue ¬"
Player_Name_Var = "Type a Vaild Player Name (or Leave it blank for the name Lillana) ¬ "
PressEnter_Var = "Press Enter to Continue ¬ "
PressEnter_Var_wrong = "Please Press Enter to Continue Again! ¬ "

typeA = "Type 'A' Question: "
typeAB = "Type A or B Question: "
typeABC = "Type Betwen A to C Question: "
typeABCD = "Type Between A to D Question: "

typeWrong = "Please Type A Question!: "
typeABWrong = "Please type A to B Question!:"
typeABCWrong = "Please type A to B Question!: "
typeABCDWrong = "Please type A to D Question!: "

#Menu (Stable)
print("")
print("THE ENCHANTED DETECTICE")
print("-----------------------------------------------")
print("")
print("a) Start Game")
print("b) Options - Coming Soon...")
print("c) Quick Notes - Coming Soon...")
print("d) GitHub")
print("")
print("*Check GitHub For Any Updates")
print("-----------------------------------------------")
print("")


MainMenu = input(SelectOption1)
while MainMenu!="A" and MainMenu!="B" and MainMenu!="C" and MainMenu!="D": 
    MainMenu = input(Selectoption1wrong)

print("")
print("")

PlayerUsername = input(Player_Name_Var)


if PlayerUsername == "":
    PlayerUsername = "Lillana"



#Start Menu  - The Main Game     ! 

if MainMenu == "A" or "a":
  
    print("")
    print("THE ENCHANTED DECTECTIVE: A PYTHON BASED DECISON GAME")
    print("")
    print("")
    print("-----------------------------------------------------")
    print("")
    print("Warning: This Game is still in Early Development (a lot of bugs and fixes)")
    print("")
    print("-----------------------------------------------------")
    print("")

print("! Quick Note Before You Start - Please just type the letterd (a, b and c) or numbers if your ask to")
print("")


EnteredContinue0 = input(PressEnter_Var)
while EnteredContinue0!="": 
    EnteredContinue0 = input(PressEnter_Var_wrong)


if EnteredContinue0 == "":

    print("")
    print("")
    print("")
    print("")
    print("I'm",PlayerUsername ,"a detective in the Ardenia police force. I've always been good at solving puzzles and getting to the bottom of things, but my real talent is something that most people would consider a liability:")
    print("")
    print("")
    print("I can talk to animals. It's not something I go around advertising, but it comes in handy when I'm working on a case. Like this one, for example.")
    print("")
    print("")
    print("I was called to the palace to investigate a string of disappearances that had been occurring in the gardens. The palace staff had been going missing one by one, and no one knew why. The palace guards had searched the gardens and the surrounding area, but they hadn't found any clues.")
    print("")
    print("")
    print("As soon as I arrived, I could tell that something was off. The palace staff were all on edge, and the palace guards seemed more like they were guarding a prison than a royal residence. And then there was the ghost. Everyone had heard the rumors of the Ghost of the Rose Garden, but I had never taken them seriously. Until now. I could feel its presence everywhere I went, like a chill in the air. ")
    print("")
    print("")
    print("I knew I had to get to the bottom of this case, but I didn't know where to start. That's when I remembered my special talent. I went to the gardens and started talking to the animals.")
    print("")


EnteredContinue1 = input(PressEnter_Var)
while EnteredContinue1!="": 
    EnteredContinue1 = input(PressEnter_Var_wrong)


# Question 0 - Lilliana was talking to a group of birds. 


if EnteredContinue1 =="":
    print("")
    print("")
    print("")
    print(PlayerUsername ,"was talking to a group of birds")
    print("---------------------------------------------")
    print ("a) What's been going on here?")
    print("b) What's up little birdie, you know whats is up?")
    print("")
    TypeQuestion0 = input(typeAB)
while TypeQuestion0!="A" and TypeQuestion0 !="B" and TypeQuestion0 != "a" and TypeQuestion0 != "b": 
    TypeQuestion0 = input(typeABWrong)


    

if TypeQuestion0 =="a" or "A" or "b" or "B":
    print("")
    print("---------------------------------------------")
    print("")
    print("The Birds: The ghost, the ghost")
    print("")
    print("---------------------------------------------")
    print("")
    print ("a) what do you know that ghost?")
    print("b) .")
    print("c) .")
    print("")
    TypeQuestion1 = input("Type 'A' Question: ")
while TypeQuestion1!="A" and TypeQuestion1 != "a" : 
    TypeQuestion1 = input(typeWrong)

# Question 1 


if TypeQuestion1 == "a" or "A":
    print("")
    print("---------------------------------------------")
    print("")
    print("Bird 1: it's been taking people, its comes in the night and takes them away")
    print("")

    EnteredContinue2 = input(PressEnter_Var)
while EnteredContinue2!="": 
    EnteredContinue2 = input(PressEnter_Var_wrong)

    
if EnteredContinue2 == "": 
    print("")
    print("")
    print("")
    print("")
    print("I thanked the birds for their help and went to talk to a group of squirrels. They told me that they had seen a figure in a hooded cloak hanging around the palace at night. ")
    print("")
    print("")
    print("With this information, I returned to the palace and reported to Inspector Hans, my gruff but loyal partner on the force. He listened to my findings but was skeptical, insisting that the disappearances were just a publicity stunt. ")
    print("")
    print("")
    print("I was determined to prove him wrong and put an end to the ghost's reign of terror. I knew it wouldn't be easy, but I was ready for the challenge. ")
    print("")
    print("")
    print("The second chapter of my investigation began with a visit to the palace library. I wanted to learn more about the history of the ghost and see if there were any clues in the palace's records. ")
    print("")
    print("")
    print("")
