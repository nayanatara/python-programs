#!/usr/bin/python3
from random import randint
t = ["Stone", "Paper", "scissor"]
computer = t[randint(0,2)]
player = False
while player == False:
	player = input("Stone, Paper, scissor?")
if player == computer:
	print("Tie!")
elif player == "Stone":
	if computer == "Paper":
		print("You lose!", computer, "covers", player)
	else:
		print("You win!", player, "smashes", computer)
elif player == "Paper":
	if computer == "Scissor":
		print("You lose!", computer, "cut", player)
	else: 
		print("You won!", player, "covers", computer)
elif player == "scissor":
			if computer == "Stone":
				print("You lose..", computer, "smashes", player)
			else:
				print("You won",player, "cut", computer)
    				


