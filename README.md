# blackjack-game
This is a Blackjack game coded in Python.

## Features
Currently it is 1 player vs the dealer playing a standard game of casino blackjack from a single deck.

## Instalation
First clone the repo,
### Conda
run  
conda env create -f environment.yaml  
conda activate blackjack_env  
This will create the environment and activate it. Now run  
pip install .
to install the package to your environment.

## Venv
run  
python3 -m venv venv  
source venv/bin/activate  
to create and activate a Venv called venv, now run  
pip install -r requirements.txt  
to install dependancies. Now run  
pip install .  
to install the package to your environment.

## Docker
run  
docker build -t blackjack-game  
to build the docker image and name it blackjack-game, then run  
docker run blackjack-game  
to start a container based on the image.



## Usage
To play, run play_game.py , if using docker then a game should run when starting the container.
## Documentation

## Contributing

## License
Unlicense, contained seperately in file named LICENSE at ./license.