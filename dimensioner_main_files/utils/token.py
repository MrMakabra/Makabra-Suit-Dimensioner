import os
import json
from utils.pathfinder import Pathfinder

TOKENS_FILE_PATH = Pathfinder().get_base_dir_path()  + '/constants/tokens.json'

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
        f = open(TOKENS_FILE_PATH, 'r')
        content = f.read()
        _dir = json.loads(content)
        f.close()
        return _dir
