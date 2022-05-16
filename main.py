print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = int(input("You're lost in an island and a tiger wants to eat you. What are you going to do? \n1.Run.\n2.Scare it.\n"))

if choice1 == 2:
  print("The tiger ate you. Game over.")
elif choice1 == 1:
  choice2 = int(input("You find what it seems to be an abandoned house in the island. What are you going to do? \n1.Enter into the house.\n2.Continue running.\n"))
  if choice2 == 2:
    print("You fell into a hole and died. Game over.")
  elif choice2 == 1:
    choice3 = int(input("You entered into the house but there is a man inside. What are you going to do? \n1.Ask him where is the treause.\n2.Kill him.\n"))
    if choice3 == 1:
      print("The man says that he would never tell you where is the treasure. Then, suddenly, he kills you. Game over.")
    elif choice3 == 2:
      print("After killing him you find in his pocket a map where it shows where is the treasure, it is under the bed! You win!")
    else:
     print("You didn't select between 1 or 2.") 
  else:
    print("You didn't select between 1 or 2.") 
else:
  print("You didn't select between 1 or 2.")
  


