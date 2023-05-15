#Randomisation and python lists
#Random module is a python module used to generate random values within a range
#Module - code in different file that is imported when needed in another file

import random
# random_interger = random.randint(0, 2)
# print (random_interger)
# random_float = random.random() * 5
# print(random_float)

# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")

#Python Lists
#List Data Structure in python
# states_of_America = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]
# print(states_of_America[1])
# print(states_of_America[-1])# this line prints the last item on the list - from the last
# states_of_America[2] = "Old Jersey" #changes the name of the item selected on the list
# print(states_of_America)
# states_of_America.append("Albanus") #adds a new item at the end of the list
# print(states_of_America)
# states_of_America.extend(["Albanus", "New Albanus"]) #adds a new list at the end of the existing list
# print(states_of_America)

# print("WELCOME TO REHIM RESTAURANT.")
# nameString = input("Enter names for random choice to pay the bill, separated by comma .\n")
# names = nameString.split(", ")
# print(len(names))
# random_name = random.randint(0, len(names) - 1)
# choice = names[random_name]
# print(f"{choice} is going to pay the bill today.")

# #Alternatively using the choice() function
# choice_to_pay = random.choice(names)
# print(f"{choice_to_pay} is going to pay the bill today.")

# #NB indexerror: list out of range... is due to surpassing the last value, forgeting we start conting from 0.
# #given the states of america, the last in the list is at index 49 and not 50 and the first in the list is at index 0 and not 1.
# #Nested Lists
# fruits = ['apples', 'mangoes', 'bananas']
# vegetables = ['kales','spinach','tomatoes']
# dirty_dozen = [fruits,vegetables]#This is a list containing two lists (nested lists)
# print(dirty_dozen)

#Treasure Placement
# row1 = ["-","-","-"]
# row2 = ["-","-","-"]
# row3 = ["-","-","-"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to place the treasure? Enter row_coloumn in that order \n")
# if position == "11":
#     map[0][0] = "X"
#     print(f"{row1}\n{row2}\n{row3}")
# elif position == "12":
#     map[1][0] = "X"
#     print(f"{row1}\n{row2}\n{row3}")
# elif position == "13":
#     map[2][0] = "X"
#     print(f"{row1}\n{row2}\n{row3}")
# elif position == "21":
#     map[0][1] = "X"
#     print(f"{row1}\n{row2}\n{row3}")
# elif position == "22":
#     map[1][1] = "X"
#     print(f"{row1}\n{row2}\n{row3}")
# elif position == "23":
#     map[2][1] = "X"
#     print(f"{row1}\n{row2}\n{row3}")
# elif position == "31":
#     map[0][2] = "X"
#     print(f"{row1}\n{row2}\n{row3}")
# elif position == "32":
#     map[1][2] = "X"
#     print(f"{row1}\n{row2}\n{row3}")
# elif position == "33":
#     map[2][2] = "X"
#     print(f"{row1}\n{row2}\n{row3}")
# print("---------------------------------------------")
#     #Alternatively
# row1 = ["-","-","-"]
# row2 = ["-","-","-"]
# row3 = ["-","-","-"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to place the treasure? Enter row_coloumn in that order \n")
# selected_row = map[int(position[1]) - 1]
# selected_row[int(position[0]) - 1] = "X"
# print(f"{row1}\n{row2}\n{row3}")

print("Welcome to rock, paper and scisor game")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

random_computer = random.randint(0, 2)
choice = int(input("Enter 0 for Rock 1 for Paper or 2 for Sciscors \n"))
if random_computer == 0 and choice == 0:
    print(rock)
    print(f"computer choose {rock}, \n It's a Draw!")
elif random_computer == 1 and choice == 1:
    print(paper)
    print(f"computer choose {paper}, \n It's a Draw!")
elif random_computer == 2 and choice == 2:
    print(scissors)
    print(f"computer choose {scissors}, \n It's a Draw!")
elif random_computer == 0 and choice == 1:
    print(paper)
    print(f"computer choose {rock}, \n YOU WIN!")
elif random_computer == 0 and choice == 2:
    print(scissors)
    print(f"computer choose {rock}, \n YOU LOSE!")
elif random_computer == 1 and choice == 0:
    print(paper)
    print(f"computer choose {paper}, \n YOU LOSE!")
elif random_computer == 2 and choice == 0:
    print(scissors)
    print(f"computer choose {scissors}, \n YOU WIN!")
elif random_computer == 1 and choice == 2:
    print(paper)
    print(f"computer choose {rock} \n YOU WIN!")
else:
    print("You typed an invalid number, You Lose!")    