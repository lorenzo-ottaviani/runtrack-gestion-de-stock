from models import *


class App:
    """ Main class of the game. """
    def __init__(self):
        """ Initialization of the class. """
    def run(self):
        """"""
        session = ConnectDatabase().my_base


if __name__ == '__main__':  # The program will be run only if executed directly, not if it is called by another program.
    program = App()
    program.run()
