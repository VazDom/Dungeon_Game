import os
import random


CELLS= [(0,0),(1,0),(2,0),(3,0),(4,0),
		(0,1),(1,1),(2,1),(3,1),(4,1),
		(0,2),(1,2),(2,2),(3,2),(4,2),
		(0,3),(1,3),(2,3),(3,3),(4,3),
		(0,4),(1,4),(2,4),(3,4),(4,4)]

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
	# Returns a list of tuples
	return random.sample(CELLS, 3) 


def move_player(player, move):
	x,y = player
	if move == "LEFT":
		x -= 1
	if move == "RIGHT":
		x += 1
	if move == "UP":
		y -= 1
	if move == "DOWN":
		y += 1
	return x, y


def get_moves(player):
	moves = ["LEFT", "RIGHT", "UP", "DOWN"]
	# Unpacking player tuple into x and y coordinates
	x,y = player
	if x == 0:
		moves.remove("LEFT")
	if x == 4:
		moves.remove("RIGHT")
	if y == 0:
		moves.remove("UP")
	if y == 4:
		moves.remove("DOWN")
	return moves


def draw_map(player):
	print(" _"*5)
	title = "|{}"

	for cell in CELLS:
		x,y = cell
		if x < 4:
			line_end = ""
			if cell == player:
				output = title.format("X")
			else:
				output = title.format("_")
		else:
			line_end = "\n"
			if cell == player:
				output = title.format("X|")
			else:
				output = title.format("_|")
		print(output, end = line_end)




def game_loop():
	# Unpacking CELLS list
	monster, door, player = get_locations()
	playing = True

	while playing:
		clear_screen()
		draw_map(player)
		valid_moves = get_moves(player)

		print("you are currently in room {}".format(player))
		print("you can move {}".format(", ".join(valid_moves))) 
		print("Enter QUIT to quit")

		move = input("> ")
		move = move.upper()

		if move == "QUIT":
			print("\n ** See you next time! **\n")
			break
		if move in valid_moves:
			player = move_player(player, move)
			if player == monster:
				print("\n ** OH NO! the monster got you**\n")
				playing = False
			if player == door:
				print("\n You escaped! CONGRATS \n")
				playing = False
		else:
			input("\n ** Walls are hard dont run into them ** \n")
	else:
		if input("Pay again? [y/n]".lower()) != "n":
			game_loop()
		



clear_screen()
print("Wellcome to the dungeon")
input("Press return to start")
clear_screen()
game_loop()
