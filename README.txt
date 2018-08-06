A machine learning development environment. Created by Charles Rule and William (Alex) Fallin for the Texas State University REUSSA 2018.
Refer to characters.png for the gameboard, code diagram.png for our code structure and questionnumbers.txt for available actions. 

There are seven modes:
- 'binary': play against a bot that only choses binary search as player one
- 'binaryp1': play against a bot that only choses binary search as player two
- 'random': play against a bot that randomly choses actions as player one
- 'randomp1': play against a bot that randomly choses actions as player two
- 'optimal': play against the optimal agent as player one 
- 'demo': play as a human against the neural network
- 'none': the NN plays against itself 

You can switch between modes by changing agentType in the neural network files.

----------------------------------------------------------------------------------------------------------------------------------------

WINDOWS 64-BIT INSTRUCTIONS
	-- Install Python 3.6 at https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe
	-- Install Anaconda 5.2 for Python 3.6 at https://repo.anaconda.com/archive/Anaconda3-5.2.0-Windows-x86_64.exe
	-- Open Anaconda Prompt and enter the following commands:
		-- pip3 install matplotlib
		-- conda install pytorch-cpu -c pytorch 
		-- pip install gym (if this doesn't work do pip3 or pip install gym[all]. This will cause errors but install more than the barebones gym. The gym installation is finicky)
	-- Download the GitHub repo at https://github.com/cerule7/Guess-Who

	-- Find your Anaconda folder and navigate to the 'envs' folder e.g. ("D:\Anaconda\Lib\site-packages\gym\envs)
		-- Edit __init__.py and add this code at the bottom:
			register(
	    		id='Guesswho-v0',
	    		entry_point='gym.envs.guesswho:GuesswhoEnv',
	    		)
		-- Create a folder called 'guesswho' and copy the contents of the GitHub repo into it

	After doing all these steps, run actorcritic.py, qnn.py, or asyncac.py (asynchronous actor-critic) by opening the Anaconda command prompt, navigating to the GuessWho Github folder and then running the file (using 'python tdlearning.py'). Doing this will run the training/data collection.
