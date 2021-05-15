# Ben-Ryder 2019

import logging

import paths
from project import data

logging.basicConfig(filename='main.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
game_reference = "server"

try:

    def main():
        game_model = data.load(paths.gamePath + game_reference)
        print(game_model.__dict__)


    if __name__ == "__main__":
        main()

except Exception as e:
    logging.exception("caught at main")
    raise e