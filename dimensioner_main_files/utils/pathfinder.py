import os


class Pathfinder():
    def __init__(self) -> None:
        pass

    def get_project_path(self):
        return os.path.dirname(os.path.abspath(__file__))

    def get_base_dir_path(self):
        return os.path.dirname(self.get_project_path())