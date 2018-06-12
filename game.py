import numpy as np

class Game:
	
	numTurns = 0

	def __init__():
		name = input("Enter p1 name")
		p1 = new Player(self, name, new Gameboard(), np.random.randint(0, 23))
		print(p1.getName() + " selected " + p1.getBoard().getCharacter(p1.getSelected()).getName())
		name = input("Enter p2 name")
		p2 = new Player(self, name, new Gameboard(), np.random.randint(0, 23))
		print(p2.getName() + " selected " + p2.getBoard().getCharacter(p2.getSelected()).getName())
