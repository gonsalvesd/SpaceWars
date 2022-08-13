#RandomLocation.py
import random
from random import randint

def random_row(map):
	return random.randint(0, len(map) - 1)

def random_col(map):
	return random.randint(0, len(map[0]) - 1)