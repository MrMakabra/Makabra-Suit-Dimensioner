from utils.token import Token

class Menu():
    def __init__(self) -> None:
        self.option = None

    def show_menu(self, filename : str = Token().get_token('MAIN_MENU_TEXT_PATH')):
        self.__print_menu_file(filename)

    def __print_menu_file(self, filename):
        f = open(filename, 'r')
        content = f.read()
        print (content)
        f.close()

