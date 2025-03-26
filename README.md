# blackjack-game
This is a Blackjack game coded in Python.
Made of 4 classes `Card`, `Deck`, `Hand` and `Game`. The first 3 are used to represent the cards, deck and hands in a real blackjack game whilst the `Game` class controls the gameplay itself.

## Features
Currently it is 1 player vs the dealer playing a standard game of casino blackjack from a single deck.

## Instalation
This package comes with a variety of options for environment management. Installation instructions using Conda, Venv and Docker are below. After cloning the repo, please use whichever is most convenient for you.
### Conda
Run  
```bash
conda env create -f environment.yaml  
conda activate blackjack_env  
```
This will create the environment and activate it. Now run  
```bash
pip install .
```
to install the package to your environment.

## Venv
Run: 
```bash
python3 -m venv venv  
source venv/bin/activate  
```
To create and activate a Venv called venv, now run  
```bash
pip install -r requirements.txt  

to install dependancies. Now run  
pip install .  
```
To install the package to your environment.

## Docker
Run:  
```bash
docker build -t blackjack-game . 
```
To build the docker image and name it blackjack-game, then run:  
```bash
docker run -i blackjack-game  
```
To start a container based on the image in interactive mode to allow you to play a game.



## Usage
To play, run:  
```bash
play_game.py 
```
If using docker then a game should run when starting the container.

## Testing
This package has been structured so that the tests in ./tests can all be run by running: 
```bash
pytest
```
in your cli.

## License
Unlicense, contained seperately in file named LICENSE at ./license.