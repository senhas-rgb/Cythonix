def argParser():
    import sys
    try:
        file2parse=sys.argv[1]
        return file2parse, 0 # return filename and success code
    except:
        print("Filename not provided.")
        print("Syntax: main.py <inputFile>")
        return None , 1

#file,code = argParser()

#if code == 1:
#    exit()

def fileParser(fileName):
    fileContents = []
    import os

    if os.path.isfile(fileName) == True and open(fileName, 'r').read(1) != '':
        File = open(fileName, 'r')
        fileContents = File.read().split('\n')
        return fileContents , 0
    else:
        print("File does not exist or is empty.")
        return None , 1

#text,code1 = fileParser(file)

#if code1 == 1:
#    exit()

def stringDetect(inputText):
    strings=[]
    for line in inputText:
        if line == '\n':
            break
        else:
            if 'print' in line:
                for index in range(len(line)):
                    if line[index] == "'" or line[index] == '"':
                        defsymbol = line[index]
                        startIndex = index
                        break
                index = 0
                for index in range(startIndex+1, len(line)):
                    if line[index] == defsymbol:
                        stopIndex = index
                        break
                strings.append[line[startIndex:stopIndex+1]]
                