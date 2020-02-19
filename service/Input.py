import random
import RPi.GPIO as GPIO


def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    # input buttons
    GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def getInput(numberOfParticipants):
    return random.randrange(0, numberOfParticipants)


def getInput():
    pressedButtons = []

    while True:
        if GPIO.input(7) == GPIO.HIGH:
            pressedButtons.append(0)

        if GPIO.input(8) == GPIO.HIGH:
            pressedButtons.append(1)

        if GPIO.input(10) == GPIO.HIGH:
            pressedButtons.append(2)

        if GPIO.input(11) == GPIO.HIGH:
            pressedButtons.append(3)

        if GPIO.input(12) == GPIO.HIGH:
            pressedButtons.append(4)

        if GPIO.input(13) == GPIO.HIGH:
            pressedButtons.append(5)

        if GPIO.input(15) == GPIO.HIGH:
            pressedButtons.append(6)

        if GPIO.input(16) == GPIO.HIGH:
            pressedButtons.append(7)

        if GPIO.input(18) == GPIO.HIGH:
            pressedButtons.append(8)

        if GPIO.input(19) == GPIO.HIGH:
            pressedButtons.append(9)

        if GPIO.input(21) == GPIO.HIGH:
            pressedButtons.append(10)

        if GPIO.input(22) == GPIO.HIGH:
            pressedButtons.append(11)

        if GPIO.input(23) == GPIO.HIGH:
            pressedButtons.append(12)

        if GPIO.input(24) == GPIO.HIGH:
            pressedButtons.append(13)

        if GPIO.input(26) == GPIO.HIGH:
            pressedButtons.append(14)

        if GPIO.input(29) == GPIO.HIGH:
            pressedButtons.append(15)

        if GPIO.input(31) == GPIO.HIGH:
            pressedButtons.append(16)

        if GPIO.input(32) == GPIO.HIGH:
            pressedButtons.append(17)

        if GPIO.input(33) == GPIO.HIGH:
            pressedButtons.append(18)

        if GPIO.input(35) == GPIO.HIGH:
            pressedButtons.append(19)

        if len(pressedButtons) > 0:
            return pressedButtons
