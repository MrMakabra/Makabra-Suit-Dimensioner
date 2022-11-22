from utils.token import Token
from menu import Menu
from playsound import playsound

class main():
    def __init__(self) -> None:
        #playsound(Token.get_token('FUN_FILE_PATH'))
        Menu().show_menu()


if __name__ == "__main__":
    main()