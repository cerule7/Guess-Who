WINDOWS 64-BIT INSTRUCTIONS
	-- Install Python 3.6 at https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe
	-- Install CMake at https://cmake.org/files/v3.12/cmake-3.12.0-rc2-win64-x64.msi
	-- Install Anaconda 5.2 for Python 3.6 at https://repo.anaconda.com/archive/Anaconda3-5.2.0-Windows-x86_64.exe
	-- Open Anaconda Prompt and enter the following commands:
		-- pip3 install matplotlib
		-- pip3 install http://download.pytorch.org/whl/cpu/torch-0.4.0-cp36-cp36m-win_amd64.whl
		-- pip3 install torchvision
		-- pip install gym (if this doesn't work do pip3 or pip install gym[all] this will cause errors but install more than the barebones gym. The gym installation is finicky)
	-- Download the GitHub repo at https://github.com/cerule7/Guess-Who

	-- Find your Anaconda folder and navigate to the 'envs folder e.g. ("D:\Anaconda\Lib\site-packages\gym\envs)
		-- Edit __init__.py and add this code:
			register(
	    		id='Guesswho-v0',
	    		entry_point='gym.envs.guesswho:GuesswhoEnv',
	    		)
		-- Also create a folder called 'guesswho' and copy the contents of the GitHub repo to it

	After doing all these steps, you should be able to run the tutorial.py in the original GitHub repo folder. Doing this will run the training/data collection