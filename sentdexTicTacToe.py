import itertools, random


def win(current_game):

	def all_same(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True
		else:
			return False

	# Horizontal
	for row in game:
		if all_same(row):
			print(f"Player {row[0]} is the winner horizontally!")
			return True

	# Diagonal
	diags = []
	for col, row in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner diagonally (/)!")
		return True

	diags = []
	for ix in range(len(game)):
		diags.append(game[ix][ix])
	if all_same(diags):
		print(f"Player {diags[0]} is the winner diagonally (\\)!")	
		return True

	# Vertical
	for col in range(len(game)):
		check = []

		for row in game:
			check.append(row[col])

		if all_same(check):
			print(f"Player {check[0]} is the winner vertically (|)!")
			return True

	return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):
	try:
		if game_map[row][column] != 0:
			print("This position is occupado! Choose another!")
			return game_map, False
		print("   "+"  ".join([str(i) for i in range(len(game))]))
		if not just_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count, row)
		return game_map, True

	except IndexError as e:
		print(f"Error: Make sure you input correct value for row/column. Choices: {choice_options}", e)
		return game_map, False

	except Exception as e:
		print("Something went very wrong!", e)	
		return game_map, False


play = True
while play:
	
	try:
		game_size = int(input("What size game of tic tac toe? (2 - 7) "))
	except ValueError:
		game_size = 0
	if not game_size in range(2,8):
		game_size = 3
		print("Invalid size! Game set to classic 3x3 tic tac toe.")
	game = [[0 for i in range(game_size)] for i in range(game_size)]
	
	if game_size in range(2, 4):
		max_players = 2;
	else:
		try:
			max_players = int(input("How many players? "))
		except ValueError:
			max_players = 0
		if not max_players in range(2,game_size):
			max_players = 2
			print("Oops! Can't play with that no. of players. Default set as 2 players.")
	players = list(range(1,max_players+1))

	print(f"Starting a {game_size}x{game_size} game with {max_players} players...")
	choice_options = list(range(len(game)))

	game_won = False
	game, _ = game_board(game, just_display=True)
	player_choice = itertools.cycle(players)
	while not game_won:
		current_player = next(player_choice)
		print(f"Current Player: {current_player}")
		played = False

		while not played:
			try:
				column_choice = int(input(f"What column do you want to play? {choice_options}: "))
			except ValueError:
				print(f"Error: Make sure you input row/column as a \"number\" in given range ({choice_options}). Choosing random value...")
				column_choice = random.randrange(game_size)

			try:
				row_choice = int(input(f"What row do you want to play? {choice_options}: "))
			except ValueError:
				print(f"Error: Make sure you input row/column as a \"number\" in given range ({choice_options}). Choosing random value...")
				row_choice = random.randrange(game_size)

			game, played = game_board(game, current_player, row_choice, column_choice)

		if win(game):
			game_won = True
			again = input("The game is over, would you like to play again? (y/n) ")
			if again.lower() == "y":
				print("Restarting...")
			else:
				print("Byeeeeeee")
				play = False