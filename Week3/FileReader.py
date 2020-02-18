class FileReader:
    def __init__(self, _path):
        self.path = _path
    def read(self):
        file_str = ""
        try:
            with open(self.path) as f:
                file_str = f.read()
        except FileNotFoundError:
            return ""
        return file_str

# reader = FileReader('not_exist_file.txt')
# text = reader.read()
# print(text)


# reader = FileReader('some_file.txt')
# text = reader.read()
# print(text)