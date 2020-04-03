import os


def read_from_file(file):
    if os.path.exists(file):
        infile = open(file, "r")
        line = infile.readline()
        infile.close()
    else:
        raise Exception("No such file")
    return line