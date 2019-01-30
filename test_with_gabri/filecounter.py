import os, os.path

class FileCounter:
    def count_file(self, directory):
        return sum([len(files) for r, d, files in os.walk(directory)])
