import random
import sys 

class Node():
    def __init__(self, node_name):
        self.name = node_name 
        pass

    def test(self):
        print('test')

class Directory(Node):
    DIR_MAX_ELEMS = 3

    def __init__(self, node_name):
        super().__init__(node_name)
        self.items = {}

    def list_items(self):
        for i, item in enumerate(self.items.values()):
            print(str(i)+') '+item.name)
        print('\n')

    def move_item(self, item_name, new_location):
        print(len(new_location.items))
        if len(new_location.items)<Directory.DIR_MAX_ELEMS:

            new_location.items[item_name] = self.items[item_name]
            self.delete(item_name)
        else:   
            return -1
        return 1

    def create(self, name, file_type):
        if len(self.items)<Directory.DIR_MAX_ELEMS:
            self.items[name] = file_type(name)
        else:   
            return -1
        return 1

    def delete(self, name):
        del self.items[name]
        return 1

class File(Node):

    def readfile(self):
        print(self.data)
        return self.data

class BinaryFile(File):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.data = random.randint(0,sys.maxsize*2+1)

class LogTextFile(File):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.data = ''

    def append_str(self, text):
        self.data += '\n'+text

class BufferFile(File):
    MAX_BUF_FILE_SIZE = 3

    def __init__(self, node_name):
        super().__init__(node_name)
        self.data = []

    def append(self, item):
        if len(self.data)<BufferFile.MAX_BUF_FILE_SIZE:
            self.data.append(item)
        else:
            return -1
        return 1

    def consume(self):
        if len(self.data)<BufferFile.MAX_BUF_FILE_SIZE:
            el = self.data[0]
            self.data = self.data[1:-1]
            return el
        else:
            return -1

NODE_TYPES = {
    'dir' : Directory,
    'bin' : BinaryFile,
    'log' : LogTextFile,
    'buff' : BufferFile
}