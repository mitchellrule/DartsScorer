'''
author = Mitch Rule
email = mitchman5506@gmail.com

This program will keep score of a game of darts for two players.
Each player has to count their score down from 501 and reach zero on 
a double number.
Players will enter their throws into the terminal with a specific syntax
and the scorer calculate their score and eventually determine a winner.
'''

class Player(object):
	'''
	Contains all of the data for each player
	and the functions for calculating scores.
	'''

	def __init__(self, name):
		self.name = name
		self.score = 501
		self.throws = []

	def throw(throw1, throw2, throw3):
