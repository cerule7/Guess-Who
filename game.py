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
				p1 = getAction(action, p1, p2)
				gameOver = True
			#for debug
			elif(action == '-1'):
				quit()
			else:
				p1 = getAction(action, p1, p2)
				p1.getBoard().printBoard()
		else: 
			action = input("P2: Ask question or guess character? (1 or 2-17)")
			if(action == '1'):
				p2 = getAction(action, p2, p1)
				gameOver = True
			#for debug
			elif(action == '-1'):
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
	if i == '24':
		player.getBoard().updateList(player.getBoard().askQ('isFemale', otherplayer.getBoard()))
	if i == '25':
		player.getBoard().updateList(player.getBoard().askQ('hasHat', otherplayer.getBoard()))
	if i == '26':
		player.getBoard().updateList(player.getBoard().askQ('hasGlasses', otherplayer.getBoard()))
	if i == '27':
		player.getBoard().updateList(player.getBoard().askQ('hasBeard', otherplayer.getBoard()))
	if i == '28':
		player.getBoard().updateList(player.getBoard().askQ('hasMustache', otherplayer.getBoard()))
	if i == '29':
		player.getBoard().updateList(player.getBoard().askQ('hasRosyCheeks', otherplayer.getBoard()))
	if i == '30':
		player.getBoard().updateList(player.getBoard().askQ('isSmiling', otherplayer.getBoard()))
	if i == '31':
		player.getBoard().updateList(player.getBoard().askQ('isBald', otherplayer.getBoard()))
	if i == '32':
		player.getBoard().updateList(player.getBoard().askQ('hasGlasses', otherplayer.getBoard()))
	if i == '33':
		player.getBoard().updateList(player.getBoard().askQ('hasBeard', otherplayer.getBoard()))
	if i == '34':
		player.getBoard().updateList(player.getBoard().askQ('hasMustache', otherplayer.getBoard()))
	#hair colors
	else:
		characterlist = player.getBoard().askHairColor(i, otherplayer.getBoard())
		player.getBoard().updateList(characterlist)
	return player

print("TURNS: " + str(numTurns))
print("Player 1: " + str(p1.getScore()))
print("Player 2: " + str(p2.getScore()))
print(gameOver)

#runs the game
main()
