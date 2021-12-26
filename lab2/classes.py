class Node():
    def __init__(self, node_name):
        pass

    def test(self):
        print('test')

class Directory(Node):
    DIR_MAX_ELEMS = 3

    def __init__(self):
        super().__init__()
        self.items = []

    def list_items(self):
        pass

    def move_item(self, item_name, new_location):
        pass

    def create(self, file_type, name):
        pass

    def delete(self, name):
        pass

class File(Node):
    def readfile(self):
        pass

class BinaryFile(File):
    pass

class LogTextFile(File):
    def append_str(self, text):
        pass

class BufferFile(File):
    MAX_BUF_FILE_SIZE = 3
    
    def append(self, item):
        pass

    def consume(self):
        pass

NODE_TYPES = {
    'dir' : Directory,
    'bin' : BinaryFile,
    'log' : LogTextFile,
    'buff' : BufferFile
}