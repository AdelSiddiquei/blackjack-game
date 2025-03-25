# blackjack-game
This is a Blackjack game coded in Python.

## Features
Currently it is 1 player vs the dealer playing a standard game of casino blackjack from a single deck.

## Instalation
First clone the repo,
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
docker build -t blackjack-game  
```
To build the docker image and name it blackjack-game, then run:  
```bash
docker run blackjack-game  
```
To start a container based on the image.



## Usage
To play, run:  
```bash
play_game.py 
```
If using docker then a game should run when starting the container.
## Documentation

## Contributing

## License
Unlicense, contained seperately in file named LICENSE at ./license.