#level1.py
import RandomLocation
import sqlcreatetable
import InitMap
import time


def levelOne(map):
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print " 2D Space Wars"
	print "\n"
	print " *****LEADERBOARDS***** "
	print "  *****TOP FIVE*****  "
	sqlcreatetable.read_topscore()
	print "\n"
	print "How to play:"
	print "there are 5 rows, ranged(0 - 4)"
	print "there are 5 columns, ranged (0 - 4)"
	print "Input a number(0,1,2,3,4) in rows and columns to"
	print "select a hidden location to find your target."
	print "\n"
	print "Level 1"
	print "\n"
	print "Seek and Destroy the enemy's 'Destroyer Battleship'"
	print "With your Air-launched ballistic missile"
	print "You have 5 turns this Round!"
	print "\n"
	#Init Level 1 map
	map = []
	InitMap.spawn_rows(map)
	InitMap.spawn_cols(map)
	#spawn location
	RandomLocation.random_row(map)
	RandomLocation.random_col(map)
	#assign location
	ship_row = RandomLocation.random_row(map)
	ship_col = RandomLocation.random_col(map)
	InitMap.spawn_rows(map)
	sqlcreatetable.create_table()
	sqlcreatetable.user_entry()
	
		###Debugger###
	print "Shiprow", ship_row  #comment the print for ship_row
	print "Shipcol", ship_col  # and ship_col after debugging is complete
#########################################################################
	
	for turn in range(5,0,-1):
		print "\n"
		print "Name: ", 
		sqlcreatetable.read_name()
		print "Score: ", 
		sqlcreatetable.read_score()
		print "Turns Left: ", turn
		print "\n"
	
		try:
			guess_row = int(raw_input("Guess Row:"))
			guess_col = int(raw_input("Guess Col:"))

			if guess_row == ship_row and guess_col == ship_col:
				map[guess_row][guess_col] == "D"
				InitMap.spawn_rows(map)
				sqlcreatetable.update()
				print "Congratulations! You sunk my battleship!"
				print "Name: ", 
				sqlcreatetable.read_name()
				print "Score: ", 
				sqlcreatetable.read_score()
				advanceLevel = raw_input("Advance to next level? ('y' or 'n') :")
				print "\n"
	#			break
			
				while True:
					if advanceLevel == 'y':
						levelTwo(map)

					elif advanceLevel == 'n':
						print "Exiting Game..."
						time.sleep(1)
						print "Closing Modules...", "5",
						time.sleep(1)
						print "4",
						time.sleep(1)
						print "3",
						time.sleep(1)
						print "2",
						time.sleep(1)
						print "1",
						time.sleep(1)
						print "Modules Closed..."
						time.sleep(0.5)
						exit()

					else:
						print "ValueError: Incorrect value detected."
						advanceLevel = raw_input("Restart level? ('y' or 'n') :")

			else:
				if guess_row < 0 or guess_row > 4 or guess_col < 0 or guess_col > 4:
					InitMap.spawn_rows(map)
					print "Oops, that's not even in the ocean."
					print "Name: ", 
					sqlcreatetable.read_name()
					print "Score: ", 
					sqlcreatetable.read_score()
					print "\n"

				elif map[guess_row][guess_col] == "X":
					InitMap.spawn_rows(map)
					print "You guessed that one already."
					print "Name: ", 
					sqlcreatetable.read_name()
					print "Score: ", 
					sqlcreatetable.read_score()
					print "\n"
					
				else:
					map[guess_row][guess_col] = "X"
					InitMap.spawn_rows(map)
					print "You missed my battleship!"
					print "Name: ", 
					sqlcreatetable.read_name()
					print "Score: ", 
					sqlcreatetable.read_score()
					print "\n"
										
		except ValueError:
			print "Oops!  That was no valid number.  Try again..."
						
		if turn <= 1:
			print "Game Over"
			print "Name: ", 
			sqlcreatetable.read_name()
			print "Score: ", 
			sqlcreatetable.read_score()
			print "\n"
			print " *****LEADERBOARDS***** "
			print "   *****TOP FIVE*****  "
			sqlcreatetable.read_topscore()
			print "\n"
			print "You didn't make it to the end..."
			
			response = raw_input("Restart level? ('y' or 'n') :")
			while True:
				if response == 'y':
					levelOne(map)

				elif response == 'n':
					print "Exiting Game..."
					time.sleep(1)
					print "Closing Modules...", "5",
					time.sleep(1)
					print "4",
					time.sleep(1)
					print "3",
					time.sleep(1)
					print "2",
					time.sleep(1)
					print "1",
					time.sleep(1)
					print "Modules Closed..."
					time.sleep(0.5)
					exit()

				else:
					print "ValueError: Incorrect value detected."
					response = raw_input("Restart level? ('y' or 'n') :")




def levelTwo(map):
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print " 2D Space Wars"
	print "\n"
	print " *****LEADERBOARDS***** "
	print "  *****TOP FIVE*****  "
	sqlcreatetable.read_topscore()
	print "\n"
	print "How to play:"
	print "there are 7 rows, ranged(0 - 6)"
	print "there are 7 columns, ranged (0 - 6)"
	print "Input a number(0,1,2,3,4,5,6) in rows and columns to"
	print "select a hidden location to find your target."
	print "\n"
	print "Level 2"
	print "\n"
	print "Seek and Destroy the enemy's 'Destroyer Battleship'"
	print "With your Air-launched ballistic missile"
	print "You have 8 turns this round!"
	print "\n"
	#Init Level 2 map
	map = []
	InitMap.spawn_rows(map)
	InitMap.spawn_cols2(map)
	#spawn location
	RandomLocation.random_row(map)
	RandomLocation.random_col(map)
	#assign location
	ship_row = RandomLocation.random_row(map)
	ship_col = RandomLocation.random_col(map)
	InitMap.spawn_rows(map)
	sqlcreatetable.create_table()
	sqlcreatetable.user_entry()

		###Debugger###
	print "Shiprow", ship_row  #comment the print for ship_row
	print "Shipcol", ship_col  # and ship_col after debugging is complete
#########################################################################

	for turn in range(8,0,-1):
		print "\n"
		print "Name: ", 
		sqlcreatetable.read_name()
		print "Score: ", 
		sqlcreatetable.read_score()
		print "Turns Left: ", turn
		print "\n"

		try:
			guess_row = int(raw_input("Guess Row:"))
			guess_col = int(raw_input("Guess Col:"))
	
			if guess_row == ship_row and guess_col == ship_col:
				map[guess_row][guess_col] == "D"
				InitMap.spawn_rows(map)
				sqlcreatetable.update_2()
				print "Congratulations! You sunk my battleship!"
				print "Name: ", 
				sqlcreatetable.read_name()
				print "Score: ", 
				sqlcreatetable.read_score()
				advanceLevel = raw_input("Advance to next level? ('y' or 'n') :")
				print "\n"
	#			break
			
				while True:
					if advanceLevel == 'y':
						levelThree(map)

					elif advanceLevel == 'n':
						print "Exiting Game..."
						time.sleep(1)
						print "Closing Modules...", "5",
						time.sleep(1)
						print "4",
						time.sleep(1)
						print "3",
						time.sleep(1)
						print "2",
						time.sleep(1)
						print "1",
						time.sleep(1)
						print "Modules Closed..."
						time.sleep(0.5)
						exit()

					else:
						print "ValueError: Incorrect value detected."
						advanceLevel = raw_input("Restart level? ('y' or 'n') :")

			else:
				if guess_row < 0 or guess_row > 6 or guess_col < 0 or guess_col > 6:
					InitMap.spawn_rows(map)
					print "Oops, that's not even in the ocean."
					print "Name: ", 
					sqlcreatetable.read_name()
					print "Score: ", 
					sqlcreatetable.read_score()

				elif map[guess_row][guess_col] == "X":
					InitMap.spawn_rows(map)
					print "You guessed that one already."
					print "Name: ", 
					sqlcreatetable.read_name()
					print "Score: ", 
					sqlcreatetable.read_score()
		
				else:
					map[guess_row][guess_col] = "X"
					InitMap.spawn_rows(map)
					print "You missed my battleship!"
					print "Name: ", 
					sqlcreatetable.read_name()
					print "Score: ", 
					sqlcreatetable.read_score()
										
		except ValueError:
			print "Oops!  That was no valid number.  Try again..."

		if turn <= 1:
			print "Game Over"
			print "Name: ", 
			sqlcreatetable.read_name()
			print "Score: ", 
			sqlcreatetable.read_score()
			print "\n"
			print " *****LEADERBOARDS***** "
			print "   *****TOP FIVE*****  "
			sqlcreatetable.read_topscore()
			print "\n"
			print "You didn't make it to the end..."
			
			response = raw_input("Restart level? ('y' or 'n') :")
			while True:
				if response == 'y':
					levelOne(map)

				elif response == 'n':
					print "Exiting Game..."
					time.sleep(1)
					print "Closing Modules...", "5",
					time.sleep(1)
					print "4",
					time.sleep(1)
					print "3",
					time.sleep(1)
					print "2",
					time.sleep(1)
					print "1",
					time.sleep(1)
					print "Modules Closed..."
					time.sleep(0.5)
					exit()

				else:
					print "ValueError: Incorrect value detected."
					response = raw_input("Restart level? ('y' or 'n') :")




def levelThree(map):
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print " 2D Space Wars"
	print "\n"
	print " *****LEADERBOARDS***** "
	print "  *****TOP FIVE*****  "
	sqlcreatetable.read_topscore()
	print "\n"
	print "How to play:"
	print "there are 9 rows, ranged(0 - 8)"
	print "there are 9 columns, ranged (0 - 8)"
	print "Input a number(0,1,2,3,4,5,6,7,8) in rows and columns to"
	print "select a hidden location to find your target."
	print "\n"
	print "Level 3"
	print "\n"
	print "Seek and Destroy the enemy's 'Destroyer Battleship'"
	print "With your Air-launched ballistic missile"
	print "You have 11 turns this round!"
	print "\n"
	#Init Level 3 map
	map = []
	InitMap.spawn_rows(map)
	InitMap.spawn_cols3(map)
	#spawn location
	RandomLocation.random_row(map)
	RandomLocation.random_col(map)
	#assign location
	ship_row = RandomLocation.random_row(map)
	ship_col = RandomLocation.random_col(map)
	InitMap.spawn_rows(map)
	sqlcreatetable.create_table()


		###Debugger###
	print "Shiprow", ship_row  #comment the print for ship_row
	print "Shipcol", ship_col  # and ship_col after debugging is complete
#########################################################################

	for turn in range(11,0,-1):
		print "\n"
		print "Name: ", 
		sqlcreatetable.read_name()
		print "Score: ", 
		sqlcreatetable.read_score()
		print "Turns Left: ", turn
		print "\n"
		
		try:
			guess_row = int(raw_input("Guess Row:"))
			guess_col = int(raw_input("Guess Col:"))

			if guess_row == ship_row and guess_col == ship_col:
					map[guess_row][guess_col] == "D"
					InitMap.spawn_rows(map)
					sqlcreatetable.update_3()
					print "Congratulations! You sunk my battleship!"
					print "Name: ", 
					sqlcreatetable.read_name()
					print "Score: ", 
					sqlcreatetable.read_score()
					advanceLevel = raw_input("Advance to next level? ('y' or 'n') :")
					print "\n"
		#			break
				
					while True:
						if advanceLevel == 'y':
							levelFour(map)

						elif advanceLevel == 'n':
							print "Exiting Game..."
							time.sleep(1)
							print "Closing Modules...", "5",
							time.sleep(1)
							print "4",
							time.sleep(1)
							print "3",
							time.sleep(1)
							print "2",
							time.sleep(1)
							print "1",
							time.sleep(1)
							print "Modules Closed..."
							time.sleep(0.5)
							exit()

						else:
							print "ValueError: Incorrect value detected."
							advanceLevel = raw_input("Restart level? ('y' or 'n') :")

			else:
				if guess_row < 0 or guess_row > 8 or guess_col < 0 or guess_col > 8:
					InitMap.spawn_rows(map)
					print "Oops, that's not even in the ocean."
					print "Name: ", 
					sqlcreatetable.read_name()
					print "Score: ", 
					sqlcreatetable.read_score()

				elif map[guess_row][guess_col] == "X":
					InitMap.spawn_rows(map)
					print "You guessed that one already."
					print "Name: ", 
					sqlcreatetable.read_name()
					print "Score: ", 
					sqlcreatetable.read_score()
					
				else:
					map[guess_row][guess_col] = "X"
					InitMap.spawn_rows(map)
					print "You missed my battleship!"
					print "Name: ", 
					sqlcreatetable.read_name()
					print "Score: ", 
					sqlcreatetable.read_score()
										
		except ValueError:
			print "Oops!  That was no valid number.  Try again..."

		if turn <= 1:
			print "Game Over"
			print "Name: ", 
			sqlcreatetable.read_name()
			print "Score: ", 
			sqlcreatetable.read_score()
			print "\n"
			print " *****LEADERBOARDS***** "
			print "   *****TOP FIVE*****  "
			sqlcreatetable.read_topscore()
			print "\n"
			print "You didn't make it to the end..."
			
			response = raw_input("Restart level? ('y' or 'n') :")
			while True:
				if response == 'y':
					levelOne(map)

				elif response == 'n':
					print "Exiting Game..."
					time.sleep(1)
					print "Closing Modules...", "5",
					time.sleep(1)
					print "4",
					time.sleep(1)
					print "3",
					time.sleep(1)
					print "2",
					time.sleep(1)
					print "1",
					time.sleep(1)
					print "Modules Closed..."
					time.sleep(0.5)
					exit()

				else:
					print "ValueError: Incorrect value detected."
					response = raw_input("Restart level? ('y' or 'n') :")




def levelFour(map):
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print " 2D Space Wars"
	print "\n"
	print " *****LEADERBOARDS***** "
	print "  *****TOP FIVE*****  "
	sqlcreatetable.read_topscore()
	print "\n"
	print "How to play:"
	print "there are 11 rows, ranged(0 - 10)"
	print "there are 11 columns, ranged (0 - 10)"
	print "Input a number(0,1,2,3,4,5,6,7,8,9,10) in rows and columns to"
	print "select a hidden location to find your target."
	print "\n"
	print "Level 4"
	print "\n"
	print "Seek and Destroy the enemy's 'Destroyer Battleship'"
	print "With your Air-launched ballistic missile"
	print "You have 15 turns this round!"
	print "\n"
	#Init Level 4 map
	map = []
	InitMap.spawn_rows(map)
	InitMap.spawn_cols4(map)
	#spawn location
	RandomLocation.random_row(map)
	RandomLocation.random_col(map)
	#assign location
	ship_row = RandomLocation.random_row(map)
	ship_col = RandomLocation.random_col(map)
	InitMap.spawn_rows(map)
	sqlcreatetable.create_table()


		###Debugger###
	print "Shiprow", ship_row  #comment the print for ship_row
	print "Shipcol", ship_col  # and ship_col after debugging is complete
#########################################################################
	
	for turn in range(15,0,-1):
		print "\n"
		print "Name: ", 
		sqlcreatetable.read_name()
		print "Score: ", 
		sqlcreatetable.read_score()
		print "Turns Left: ", turn
		print "\n"
		
		try:
			guess_row = int(raw_input("Guess Row:"))
			guess_col = int(raw_input("Guess Col:"))
				
			if guess_row == ship_row and guess_col == ship_col:
				map[guess_row][guess_col] == "D"
				InitMap.spawn_rows(map)
				sqlcreatetable.update_4()
				print "Congratulations! You sunk my battleship!"
				print "Name: ", 
				sqlcreatetable.read_name()
				print "Score: ", 
				sqlcreatetable.read_score()
				advanceLevel = raw_input("Advance to next level? ('y' or 'n') :")
				print "\n"
	#			break
			
				while True:
					if advanceLevel == 'y':
						levelFive(map)

					elif advanceLevel == 'n':
						print "Exiting Game..."
						time.sleep(1)
						print "Closing Modules...", "5",
						time.sleep(1)
						print "4",
						time.sleep(1)
						print "3",
						time.sleep(1)
						print "2",
						time.sleep(1)
						print "1",
						time.sleep(1)
						print "Modules Closed..."
						time.sleep(0.5)
						exit()

					else:
						print "ValueError: Incorrect value detected."
						advanceLevel = raw_input("Restart level? ('y' or 'n') :")

			else:
				if (guess_row < 0 or guess_row > 10) or (guess_col < 0 or guess_col > 10):
					print "Oops, that's not even in the ocean."
					print "Name: ", 
					sqlcreatetable.read_name()
					print "Score: ", 
					sqlcreatetable.read_score()
					InitMap.spawn_rows(map)
					
				elif(map[guess_row][guess_col] == "X"):
					print "You guessed that one already."
					print "Name: ", 
					sqlcreatetable.read_name()
					print "Score: ", 
					sqlcreatetable.read_score()
					InitMap.spawn_rows(map)
					
				else:
					print "You missed my battleship!"
					print "Name: ", 
					sqlcreatetable.read_name()
					print "Score: ", 
					sqlcreatetable.read_score()
					map[guess_row][guess_col] = "X"
					InitMap.spawn_rows(map)

		except ValueError:
			print "Oops!  That was no valid number.  Try again..."

		if turn <= 1:
			print "Game Over"
			print "Name: ", 
			sqlcreatetable.read_name()
			print "Score: ", 
			sqlcreatetable.read_score()
			print "\n"
			print " *****LEADERBOARDS***** "
			print "   *****TOP FIVE*****  "
			sqlcreatetable.read_topscore()
			print "\n"
			print "You didn't make it to the end..."
			
			response = raw_input("Restart level? ('y' or 'n') :")
			while True:
				if response == 'y':
					levelOne(map)

				elif response == 'n':
					print "Exiting Game..."
					time.sleep(1)
					print "Closing Modules...", "5",
					time.sleep(1)
					print "4",
					time.sleep(1)
					print "3",
					time.sleep(1)
					print "2",
					time.sleep(1)
					print "1",
					time.sleep(1)
					print "Modules Closed..."
					time.sleep(0.5)
					exit()

				else:
					print "ValueError: Incorrect value detected."
					response = raw_input("Restart level? ('y' or 'n') :")




def levelFive(map):
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print "\n"
	print " 2D Space Wars"
	print "\n"
	print " *****LEADERBOARDS***** "
	print "  *****TOP FIVE*****  "
	sqlcreatetable.read_topscore()
	print "\n"
	print "How to play:"
	print "there are 15 rows, ranged(0 - 14)"
	print "there are 15 columns, ranged (0 - 14)"
	print "Input a number(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14) in rows and columns to"
	print "select a hidden location to find your target."
	print "\n"
	print "Level 5"
	print "\n"
	print "Seek and Destroy the enemy's 'Destroyer Battleship'"
	print "With your Air-launched ballistic missile"
	print "You have 20 turns this round!"
	print "\n"
	#Init Level 5 map
	map = []
	InitMap.spawn_rows(map)
	InitMap.spawn_cols5(map)
	#spawn location
	RandomLocation.random_row(map)
	RandomLocation.random_col(map)
	#assign location
	ship_row = RandomLocation.random_row(map)
	ship_col = RandomLocation.random_col(map)
	InitMap.spawn_rows(map)
	sqlcreatetable.create_table()
	

		###Debugger###
	print "Shiprow", ship_row  #comment the print for ship_row
	print "Shipcol", ship_col  # and ship_col after debugging is complete
#########################################################################
	
	for turn in range(20,0,-1):
		print "\n"
		print "Name: ", 
		sqlcreatetable.read_name()
		print "Score: ", 
		sqlcreatetable.read_score()
		print "Turns Left: ", turn
		print "\n"
		
		try:
			guess_row = int(raw_input("Guess Row:"))
			guess_col = int(raw_input("Guess Col:"))
				
			if guess_row == ship_row and guess_col == ship_col:
				map[guess_row][guess_col] == "D"
				InitMap.spawn_rows(map)
				sqlcreatetable.update_5()
				print "Congratulations! You sunk my battleship!"
				print "Name: ", 
				sqlcreatetable.read_name()
				print "Score: ", 
				sqlcreatetable.read_score()
	#			advanceLevel = raw_input("Advance to next level? ('y' or 'n') :")
	#			print "\n"
	#			break
			
	#			while True:
	#				if advanceLevel == 'y':
	#					print "More updates coming soon."
	#					sleep(5)
	#
	#				elif advanceLevel == 'n':
	#					print "Exiting Game..."
	#					time.sleep(1)
	#					print "Closing Modules...", "5",		#79 - 107
	#					time.sleep(1)							#opens when
	#					print "4",								#new maps are upgraded
	#					time.sleep(1)
	#					print "3",
	#					time.sleep(1)
	#					print "2",
	#					time.sleep(1)
	#					print "1",
	#					time.sleep(1)
	#					print "Modules Closed..."
	#					time.sleep(0.5)
	#					exit()

	#				else:
	#					print "ValueError: Incorrect value detected."
	#					advanceLevel = raw_input("Restart level? ('y' or 'n') :")

				response = raw_input("Restart level? ('y' or 'n') :")
				while True:
					if response == 'y':
						levelOne(map)

					elif response == 'n':
						print "Exiting Game..."
						time.sleep(1)
						print "Closing Modules...", "5",
						time.sleep(1)					
						print "4",
						time.sleep(1)
						print "3",
						time.sleep(1)
						print "2",
						time.sleep(1)
						print "1",
						time.sleep(1)
						print "Modules Closed..."
						time.sleep(0.5)
						exit()

					else:
						print "ValueError: Incorrect value detected."
						response = raw_input("Restart level? ('y' or 'n') :")
			else:
				if (guess_row < 0 or guess_row > 14) or (guess_col < 0 or guess_col > 14):
					print "Oops, that's not even in the ocean."
					print "Name: ", 
					sqlcreatetable.read_name()
					print "Score: ", 
					sqlcreatetable.read_score()
					InitMap.spawn_rows(map)
					
				elif(map[guess_row][guess_col] == "X"):
					print "You guessed that one already."
					print "Name: ", 
					sqlcreatetable.read_name()
					print "Score: ", 
					sqlcreatetable.read_score()
					InitMap.spawn_rows(map)
					
				else:
					print "You missed my battleship!"
					print "Name: ", 
					sqlcreatetable.read_name()
					print "Score: ", 
					sqlcreatetable.read_score()
					map[guess_row][guess_col] = "X"
					InitMap.spawn_rows(map)

		except ValueError:
			print "Oops!  That was no valid number.  Try again..."

		if turn <= 1:
			print "Game Over"
			print "Name: ", 
			sqlcreatetable.read_name()
			print "Score: ", 
			sqlcreatetable.read_score()
			print "\n"
			print " *****LEADERBOARDS***** "
			print "   *****TOP FIVE*****  "
			sqlcreatetable.read_topscore()
			print "\n"
			print "You didn't make it to the end..."
			
			response = raw_input("Restart level? ('y' or 'n') :")
			while True:
				if response == 'y':
					levelOne(map)

				elif response == 'n':
					print "Exiting Game..."
					time.sleep(1)
					print "Closing Modules...", "5",
					time.sleep(1)
					print "4",
					time.sleep(1)
					print "3",
					time.sleep(1)
					print "2",
					time.sleep(1)
					print "1",
					time.sleep(1)
					print "Modules Closed..."
					time.sleep(0.5)
					exit()

				else:
					print "ValueError: Incorrect value detected."
					response = raw_input("Restart level? ('y' or 'n') :")