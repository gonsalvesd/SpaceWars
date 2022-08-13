#InitMap.py
def spawn_rows(map):
	for rows in map:
		print "  ".join(rows)
		
def spawn_cols(map):
	for columns in range(5):
		map.append(["O"] * 5)

		
def spawn_cols2(map):
	for columns in range(7):
		map.append(["O"] * 7)
				

def spawn_cols3(map):
	for columns in range(9):
		map.append(["O"] * 9)
		

def spawn_cols4(map):
	for columns in range(11):
		map.append(["O"] * 11)


def spawn_cols5(map):
	for columns in range(15):
		map.append(["O"] * 15)