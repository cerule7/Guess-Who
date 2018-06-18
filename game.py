import numpy as np
from player import Player
from gameboard import gameBoard

def main(): 
	sel = np.random.randint(0, 24)
	g1 = gameBoard(sel)
	p1 = Player("PLAYER 1", g1, sel)
	print(p1.getName() + " selected " + p1.getBoard().getCharacter(p1.getBoard().getSelected()).getName())
	j = np.random.randint(0, 24)
	g2 = gameBoard(j)
	p2 = Player("PLAYER 2", g2, j)
	print(p2.getName() + " selected " + p2.getBoard().getCharacter(p2.getBoard().getSelected()).getName())
	numTurns = 0
	gameOver = False

	while(gameOver == False):
		#p1 gets even turns 
		if(numTurns % 2 == 0):
			action = int(input("P1: action?"))
			if(action >= 0 and action < 24):
				p1 = getAction(action, p1, p2)
				gameOver = True
			#for debug
			elif(action == -1):
				quit()
			else:
				p1 = getAction(action, p1, p2)
				print('P1 ACTIVE: ' + str(p1.getBoard().numberActive()))
				print('P2 ACTIVE: ' + str(p2.getBoard().numberActive()))
				if(p1.getBoard().isOneLeft()):
					p1.setScore(p1.getScore() + 1)
					print("PLAYER 1 WINS")
					gameOver = True
		else: 
			action = int(input("P2: action?"))
			if(action >= 0 and action < 24):
				p2 = getAction(action, p2, p1)
				gameOver = True
			#for debug
			elif(action == -1):
				quit()
			else:
				p2 = getAction(action, p2, p1)
				print("P1 ACTIVE: " + str(p1.getBoard().numberActive()))
				print("P2 ACTIVE: " + str(p2.getBoard().numberActive()))
				if(p2.getBoard().isOneLeft()):
					p2.setScore(p2.getScore() + 1)
					print("PLAYER 2 WINS")
					gameOver = True
		numTurns += 1
		print("TURNS: " + str(numTurns))

def getAction(i, player, otherplayer):
	#each number corresponds to an action 
	#auto quit (debug only)
	print("the player is " + player.getName())
	print("the other player is " + otherplayer.getName())
	if i == -1: 
		quit()
	#guess specific character
	if i >= 0 and i < 24:
		if(i == otherplayer.getBoard().getSelected()):
			print("CORRECT GUESS")
			player.setScore(player.getScore() + 1)
		else:
			print("INCORRECT GUESS")
			otherplayer.setScore(otherplayer.getScore() + 1)
		return 
	#y/n questions
	if i == 24:
		player.getBoard().updateList(player.getBoard().askQ('isFemale', otherplayer.getBoard()))
	if i == 25:
		player.getBoard().updateList(player.getBoard().askQ('hasHat', otherplayer.getBoard()))
	if i == 26:
		player.getBoard().updateList(player.getBoard().askQ('hasGlasses', otherplayer.getBoard()))
	if i == 27:
		player.getBoard().updateList(player.getBoard().askQ('hasBeard', otherplayer.getBoard()))
	if i == 28:
		player.getBoard().updateList(player.getBoard().askQ('hasMustache', otherplayer.getBoard()))
	if i == 29:
		player.getBoard().updateList(player.getBoard().askQ('hasRosyCheeks', otherplayer.getBoard()))
	if i == 30:
		player.getBoard().updateList(player.getBoard().askQ('isSmiling', otherplayer.getBoard()))
	if i == 31:
		player.getBoard().updateList(player.getBoard().askQ('isBald', otherplayer.getBoard()))
	if i == 32:
		player.getBoard().updateList(player.getBoard().askQ('hasGlasses', otherplayer.getBoard()))
	if i == 33:
		player.getBoard().updateList(player.getBoard().askQ('hasBeard', otherplayer.getBoard()))
	if i == 34:
		player.getBoard().updateList(player.getBoard().askQ('hasMustache', otherplayer.getBoard()))
	#hair colors
	else:
		characterlist = player.getBoard().askHairColor(i, otherplayer.getBoard())
		player.getBoard().updateList(characterlist)
	return player

#runs the game
main()
