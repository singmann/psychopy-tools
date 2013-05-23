#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import codecs
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
    
    outfileLN = os.path.join(localPath, (expName + '_' + name + '.txt'))
    outfileNN = os.path.join(netwPath, (expName + '_' + name + '.txt'))
    
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
    if os.path.isfile(outfileLN):
        outfileL = codecs.open(outfileLN,'a', encoding='utf-8')
    else:
        outfileL = codecs.open(outfileLN,'w', encoding='utf-8')
        outfileL.write("id" + sep)
        if condition:
            outfileL.write(condition + sep)
        for key in header:
            outfileL.write(key)
            outfileL.write(sep)
        outfileL.write("\n")
    
    outfileN.write(unicode(id) + sep)
    outfileL.write(unicode(id) + sep)
    if condition:
        outfileN.write(unicode(condition) + sep)
        outfileL.write(unicode(condition) + sep)        
    
    line = map(dict.get, header)    
        
    for i in range(len(line)):
        outfileL.write(unicode(line[i]).replace("\r\n", " | "))
        outfileL.write(sep)
        outfileN.write(unicode(line[i]).replace("\r\n", " | "))
        outfileN.write(sep)
    outfileL.write('\n')
    outfileN.write('\n')
    outfileL.close()
    outfileN.close()

def writeResults(header, testLists, expName, localPath, netwPath, id, extra = "", extension = "rtd", printHeader = "auto", mode = "w", sep = "\t"):
    
    outfileLN = os.path.join(localPath, (expName + '_' + extra + str(id) +'.' + extension))
    outfileNN = os.path.join(netwPath, (expName + '_' + extra + str(id) +'.' + extension))    
    
    if printHeader == "auto":
        if os.path.isfile(outfileNN):
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
    

    outfileL = codecs.open(outfileLN, mode, encoding='utf-8')
    outfileN = codecs.open(outfileNN, mode, encoding='utf-8')
    
    for line in output:
        for i in range(len(line)):
            outfileL.write(unicode(line[i]))
            outfileL.write(sep)
            outfileN.write(unicode(line[i]))
            outfileN.write(sep)
        outfileL.write('\n')
        outfileN.write('\n')
    outfileL.close()
    outfileN.close()
    
