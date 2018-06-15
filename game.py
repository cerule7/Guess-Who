import numpy as np
from player import Player
from gameboard import gameBoard

class Game:

	def main(): 
		name = input("Enter p1 name")
		sel = np.random.randint(0, 23)
		p1 = Player(name, gameBoard(sel), sel)
		print(p1.getName() + " selected " + p1.getBoard().getCharacter(sel).getName())
		name = input("Enter p2 name")
		sel = np.random.randint(0, 23)
		p2 = Player(name, gameBoard(sel), sel)
		print(p2.getName() + " selected " + p2.getBoard().getCharacter(sel).getName())
		numTurns = 0
		gameOver = False

		while(not gameOver):
			#p1 gets even turns 
			if(numTurns % 2 == 0):
				action = input("P1: Ask question or guess character? (0 or 1)")
				#for debug
				if(action == '-1'):
					quit()
				if(action == '0'):
					attribute = input("Which attribute?")
					p1.getBoard().updateList(p1.getBoard().askQ(attribute, p2.getBoard()))
					p1.getBoard().printBoard()
					#if there is only one character left, auto-win
					if(p1.getBoard().isOneLeft()):
						p1.setScore(p1.getScore() + 1)
						gameOver = True
				else:
					#character guesses end game
					guess = input("Name?")
					if(p2.getSelected == guess):
						p1.setScore(p1.getScore() + 1)
					else:
						p2.setScore(p2.getScore() + 1)
					gameOver = True
			else: 
				action = input("P2: Ask question or guess character? (0 or 1)")
				#for debug
				if(action == '-1'):
					quit()
				if(action == '0'):
					attribute = input("Which attribute?")
					p1.getBoard().updateList(p2.getBoard().askQ(attribute, p1.getBoard()))
					p2.getBoard().printBoard()
					#if there is only one character left, auto-win
					if(p2.getBoard().isOneLeft()):
						p2.setScore(p2.getScore() + 1)
						gameOver = True
				else:
					#character guesses end game
					guess = input("Name?")
					if(p1.getSelected == guess):
						p2.setScore(p2.getScore() + 1)
					else:
						p1.setScore(p1.getScore() + 1)
					gameOver = True
			numTurns += 1
			print("TURNS: " + str(numTurns))

	main()
