import os


def findTODO(y, keyword):
    a = []
    for _ in range(len(y)):
        l = y[_][1]
        a.append([y[_][0], [], []])
        for x in range(len(l)):
            if keyword in l[x]:
                a[_][2].append(l[x][l[x].index(keyword):])
                a[_][1].append(str(x + 1))
    return a

def getFileNames(fileEnding, directory):
    files = os.listdir(directory) #List directory
    target_files = [file for file in files if file.endswith(fileEnding)]  #get files with the wanted ending
    return target_files


def getLineList(files):
    a = []
    for x in range(len(files)):
        z = open(files[x], "r")
        b = z.read().split("\n")
        z.close()
        a.append([files[x], b])
    return a

def clear(finalList):
        for x in range(len(finalList)):
            if finalList[x][1] == []:
                del finalList[x]
        return finalList


def main(fileEndings, directory, keyword):
    l = []
    for x in range(len(fileEndings)):
        l.append([fileEndings[x], clear(findTODO(getLineList(getFileNames(fileEndings[x], directory)), keyword))])
    return l

def lastTouch(string): #! Under construction
    l = list(string)
    x = 1
    a = []
    b = []
    for x in range(len(l[0]) - 1):
        file = l[0][x][0][0]
        a = []
        for _ in range(len(l[0][x][0][1])):
            a.append([l[0][x][0][1][_], l[0][x][0][2][_]])
        b.append([file, a])
