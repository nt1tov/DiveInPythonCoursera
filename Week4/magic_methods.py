import os
import tempfile

class File:
    def __init__(self, path):
        if not os.path.exists(path):
            with open(path, 'w') as f:
                pass
        self.file_path = path
    
    def read(self):
        with open(self.file_path) as f:
            return f.read()

    def write(self, file_str):
        with open(self.file_path, 'w') as f:
            f.write(file_str)

    def __add__(self, obj):
        tmp_path = tempfile.gettempdir()
        tmp_filename = os.path.join(tmp_path, self.file_path)

        lhs_str = ""
        with open(self.file_path, 'r') as f:
            lhs_str = f.read()

        rhs_str = ""
        with open(obj.file_path, 'r') as f:
            rhs_str = f.read()

        with open(tmp_filename, 'w') as f:
            f.write(lhs_str)
            f.write(rhs_str)
        f = File(tmp_filename)
        return f

    def __str__(self):
        return self.file_path

    def __getitem__(self, index): 
        line_list = []
        with open(self.file_path) as f:
            line_list = f.readlines()
        return line_list[index]
 