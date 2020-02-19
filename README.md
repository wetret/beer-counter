# Beer Counter
This small python 3 application is written for a RaspberryPi with 24 connected input buttons.

Prerequisits are:

- `apt-get install mpg123`
- `pip install RPi.GPIO`
- `pip install pyfiglet`
- `pip install fake-rpigpio` for testing on your local machine (not the RaspberryPi)

Depending if you want to setup a new game or run an existing game, comment/uncomment the marked lines in `view/RunningGame.py`. Setting up a new game is only possible on a machine with a connected keyboard. For running a preexisting game no keyboard is required, only 24 connected buttons. Used GPIO pins as input for the buttons are defined in the file `service/Input.py`.

Setting up a new game:

`python Application.py`


Start a preexisting game:

`python Application.py <game-name>`

