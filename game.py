import numpy as np
from player import Player
from gameboard import gameBoard

def main(): 
	sel = np.random.randint(0, 24)
	p1 = Player("PLAYER 1", gameBoard(sel), sel)
	print(p1.getName() + " selected " + p1.getBoard().getCharacter(sel).getName())
	sel = np.random.randint(0, 24)
	p2 = Player("PLAYER 2", gameBoard(sel), sel)
	print(p2.getName() + " selected " + p2.getBoard().getCharacter(sel).getName())
	numTurns = 0
	gameOver = False

	while(gameOver == False):
		#p1 gets even turns 
		if(numTurns % 2 == 0):
			action = input("P1: Ask question or guess character? (1 or 2-17)")
			if(action == '1'):
				gameOver == True
			#for debug
			if(action == '-1'):
				quit()
			else:
				p1 = getAction(action, p1, p2)
				p1.getBoard().printBoard()
		else: 
			action = input("P2: Ask question or guess character? (1 or 2-17)")
			if(action == '1'):
				gameOver == True
			#for debug
			if(action == '-1'):
				quit()
			else:
				p2 = getAction(action, p2, p1)
				p2.getBoard().printBoard()
		numTurns += 1
		print("TURNS: " + str(numTurns))

def getAction(i, player, otherplayer):
	#each number corresponds to an action 
	#auto quit (debug only)
	if i == '-1': 
		quit()
	#guess specific characater
	if i == '1':
		guess = input("Name?")
		if(otherplayer.getSelected() == guess):
				player.setScore(player.getScore() + 1)
		else:
				otherplayer.setScore(otherplayer.getScore() + 1)
	#y/n questions
	if i == '2':
		player.getBoard().updateList(player.getBoard().askQ('isFemale', otherplayer.getBoard()))
	if i == '3':
		player.getBoard().updateList(player.getBoard().askQ('hasHat', otherplayer.getBoard()))
	if i == '4':
		player.getBoard().updateList(player.getBoard().askQ('hasGlasses', otherplayer.getBoard()))
	if i == '5':
		player.getBoard().updateList(player.getBoard().askQ('hasBeard', otherplayer.getBoard()))
	if i == '6':
		player.getBoard().updateList(player.getBoard().askQ('hasMustache', otherplayer.getBoard()))
	if i == '7':
		player.getBoard().updateList(player.getBoard().askQ('hasRosyCheeks', otherplayer.getBoard()))
	if i == '8':
		player.getBoard().updateList(player.getBoard().askQ('isSmiling', otherplayer.getBoard()))
	if i == '9':
		player.getBoard().updateList(player.getBoard().askQ('isBald', otherplayer.getBoard()))
	if i == '10':
		player.getBoard().updateList(player.getBoard().askQ('hasGlasses', otherplayer.getBoard()))
	if i == '11':
		player.getBoard().updateList(player.getBoard().askQ('hasBeard', otherplayer.getBoard()))
	if i == '12':
		player.getBoard().updateList(player.getBoard().askQ('hasMustache', otherplayer.getBoard()))
	#hair colors
	else:
		characterlist = player.getBoard().askHairColor(i, otherplayer.getBoard())
		player.getBoard().updateList(characterlist)
	return player

#runs the game
main()
