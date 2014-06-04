#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import codecs
import cPickle as pickle
# from psychopy import core, visual


def getId(path='', filename = 'id.lst', condition = False):
    filePath = os.path.join(path,filename)
    if os.path.isfile(filePath):
        vpFile = open(filePath, 'r')
    else:
        print('Error! vpcode.lst does not exist or is not accessable.')
        quit()
    
    tmp = []
    line = '*'
    while '*' in line:
        line = vpFile.readline()
        tmp.append(line)
    
    if line == '':
        print('Error! No number available.')
        quit()
    
    infos = line.split()
    id = unicode(infos[0])
    if (condition):
        cond = str(infos[1])
    
    tmp.pop()
    if (condition):
        nline = infos[0] + ' ' + infos[1] + ' *\n'
    else:
        nline = infos[0] + ' *\n'
    tmp.append(nline)

    while line != '':
        line = vpFile.readline()
        tmp.append(line)

    vpFile.close()
    tmpPath = path + filename +'.tmp'
    tmpFile = open(tmpPath,'w')
    tmpFile.writelines(tmp)
    tmpFile.close()    
    os.remove(filePath)
    os.rename(tmpPath, filePath)
    
    if (condition):
        return id, cond
    else:
        return id


def writeQuestionnaire(header, dict, name, expName, localPath, netwPath, id, condition = False, sep = "\t"):
    writeQuestionnaireSingle(header = header, dict = dict, name = name, expName = expName, path = localPath, id = id, condition = condition, sep = sep)
    writeQuestionnaireSingle(header = header, dict = dict, name = name, expName = expName, path = netwPath, id = id, condition = condition, sep = sep)

def writeQuestionnaireSingle(header, dict, name, expName, path, id, condition = False, sep = "\t"):
    if os.path.exists(path):
        outfileNN = os.path.join(path, (expName + '_' + name + '.txt'))
        if os.path.isfile(outfileNN):
            outfileN = codecs.open(outfileNN,'a', encoding='utf-8')
        else:
            outfileN = codecs.open(outfileNN,'w', encoding='utf-8')
            outfileN.write("id" + sep)
            if condition:
                outfileN.write("condition" + sep)
            for key in header:
                outfileN.write(key)
                outfileN.write(sep)
            outfileN.write("\n")

        outfileN.write(unicode(id) + sep)
        if condition:
            outfileN.write(unicode(condition) + sep)
        line = map(dict.get, header)    
            
        for i in range(len(line)):
            outfileN.write(unicode(line[i]).replace("\r\n", " | "))
            outfileN.write(sep)
        outfileN.write('\n')
        outfileN.close()
    else:
        print("\n\n***********************************")
        print("ERROR: following drive not accessible!!\nContact owner of Experiment!!")
        print(unicode(path))
        print("************************************\n")
    
def writeResults(header, testLists, expName, localPath, netwPath, id, extra = "", extension = "rtd", printHeader = "auto", mode = "w", sep = "\t"):
    writeResultsSingle(header = header, testLists = testLists, expName = expName, path = localPath, id = id, extra = extra, extension = extension, printHeader = printHeader, mode = mode, sep = sep)
    writeResultsSingle(header = header, testLists = testLists, expName = expName, path = netwPath, id = id, extra = extra, extension = extension, printHeader = printHeader, mode = mode, sep = sep)
    
def writeResultsSingle(header, testLists, expName, path, id, extra = "", extension = "rtd", printHeader = "auto", mode = "w", sep = "\t"):
    
    if printHeader == "auto":
        if mode == "a":
            printHeader = False
        else:
            printHeader = True

    # write data to file
    output = []
    if printHeader:
        output.append(header)
    if type(testLists[0]) is list:
        for testList in testLists:
            for trial in testList:
                line = map(trial.get, header)
                output.append(line)
    else:
        for trial in testLists:
            line = map(trial.get, header)
            output.append(line)
            
    if os.path.exists(path):  
        outfileLN = os.path.join(path, (expName + '_' + extra + str(id) +'.' + extension)) 
        outfileL = codecs.open(outfileLN, mode, encoding='utf-8')
        for line in output:
            for i in range(len(line)):
                outfileL.write(unicode(line[i]))
                outfileL.write(sep)
            outfileL.write('\n')
        outfileL.close()
    else:
        print("\n\n***********************************")
        print("ERROR: following drive not accessible!!\nContact owner of Experiment!!")
        print(unicode(path))
        print("************************************\n")

def pickleResults(object, expName, localPath, netwPath, id, extra = "", extension = "pickle"):
    pickleResultsSingle(object = object, expName = expName, path = localPath, id = id, extra = extra, extension = extension)
    pickleResultsSingle(object = object, expName = expName, path = netwPath, id = id, extra = extra, extension = extension)
    
def pickleResultsSingle(object, expName, path, id, extra = "", extension = "pickle"):
    if os.path.exists(path):
        outfileLN = os.path.join(path, (expName + '_' + extra + str(id) +'.' + extension))  
        outfileL = open(outfileLN, "wb")
        pickle.dump(object, outfileL, -1)
        outfileL.close()
    else:
        print("\n\n***********************************")
        print("ERROR: Following drive not accessible!!\nContact owner of Experiment!!")
        print(unicode(path))
        print("************************************\n")
        
    

def writeSingleFile(string, expName, name, localPath, netwPath, id, extension = "txt", mode = "w",):
    if os.path.exists(localPath):
        commentFile = codecs.open(os.path.join(localPath, (expName + "_" + name + "_" + str(id) + "." + extension)), mode, encoding='utf-8')
        commentFile.write(unicode(string))
        commentFile.write("\n")
        commentFile.write("####################end##################\n")
        commentFile.write("\n")
        commentFile.close()
    else:
        print("\n\n***********************************")
        print("ERROR: Local drive not accessible!!\nContact owner of Experiment!!")
        print("************************************\n")
    if os.path.exists(netwPath):
        commentFile = codecs.open(os.path.join(netwPath, (expName + "_" + name + "_" + str(id) + "." + extension)), mode, encoding='utf-8')
        commentFile.write(unicode(string))
        commentFile.write("\n")
        commentFile.write("####################end##################\n")
        commentFile.write("\n")
        commentFile.close()
    else:
        print("\n\n***********************************")
        print("ERROR: Network drive not accessible!!\nContact owner of Experiment!!")
        print("************************************\n")
