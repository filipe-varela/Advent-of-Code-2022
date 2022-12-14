import copy

class FileSystemGraph(object):
    def __init__(self):
        self.filesystem: dict[str,int] = {}
        self.list_of_dirs: str = []
    
    def __getitem__(self, slice) -> int:
        return self.filesystem[slice]

    def __setitem__(self, slice, value) -> None:
        self.filesystem[slice] = value

    def folders(self) -> list[str]:
        return self.list_of_dirs

    def keys(self) -> list[str]:
        return self.filesystem.keys()

    def get_list_of_dirs(self) -> list[str]:
        return copy.deepcopy(self.list_of_dirs)

    def get_last_dir(self) -> list[str]:
        return "".join(self.list_of_dirs)

    def add_filesystem(self, new_filesystem: dict[str,int]) -> None:
        self.filesystem = copy.deepcopy(new_filesystem)

    def add_list_of_dirs(self, new_list: list[str]) -> None:
        self.list_of_dirs = copy.deepcopy(new_list)

    def add_dir(self, name_dir: str) -> str:
        self.list_of_dirs.append(name_dir)
        return name_dir

    def copy(self):
        tmp = FileSystemGraph()
        tmp.add_filesystem(self.filesystem)
        tmp.add_list_of_dirs(self.list_of_dirs)
        return tmp

    def __str__(self) -> str:
        return f"{self.filesystem=}\t{self.list_of_dirs=}"

    def __rpr__(self) -> str:
        return f"{self.filesystem}"

    def pop(self):
        return self.list_of_dirs.pop()