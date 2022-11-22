import json

class Token():
    def __init__(self) -> None:
        pass

    def get_token(self, token):
        _dir = self._makedir()
        _token = _dir[token]
        if _token is None:
            raise ValueError(f"Token {token} not found.")
        return _token

    def _makedir(self):
        f = open('dimensioner_main_files/constants/tokens.json', 'r')
        content = f.read()
        _dir = json.loads(content)
        f.close()
        return _dir
