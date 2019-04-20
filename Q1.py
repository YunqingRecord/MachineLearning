
'''
Q1.py
Time: 16/04/2019
Student: ZHAO Yunqing
Course: ELEC 6008
'''


import glob                                              # import read_file module


def f_Read(path, filename):
    '''
    :param path:      saving path for txt files
    :param filename:  the one txt file you want to read
    :return:          1. the txt file names 2. txt file contents
    '''
    contents = glob.glob(path)                           # index all the txt file

    f = open(filename, 'r')                              # open the pointed data file
    text = f.read()                                      # read the opened file ("01.txt")

    return contents, text                                # output the result


fcf, text1 = f_Read(path='../data/*.txt',
                    filename='../data/01.txt')           # save the result to variable

print('txt files in path:', fcf)                         # print all file names
print('text1 contents:', text1)                          # print the read file "01.txt"
