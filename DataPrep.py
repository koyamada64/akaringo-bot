import random
import linecache

def random_lines(filename):
    idxs = random.sample(range(66), 7)
    return [linecache.getline(filename, i) for i in idxs]

def DataPrep(file1,file2):
    text = random_lines(file1)
    f = open(file2,"w",encoding="utf-8")
    f.writelines(text)
    f.close()
