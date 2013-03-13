psychopy-tools
==============

Some functions/tools I use in my PsychoPy experiments.

As will be obvious, I do *not* use the PsychoPy inbuild data types, hence some functions are concerned with writing data. Would probably be better to use the PsychoPy inbuilt data type and writing functions. 

# baseFunctions.py
- `getId(path='', filename = 'id.lst', condition = True)`:
Obtain next participant id and/or condition. Loads a text file containing one column (or two, if `condition == True`) separated by whitespace from `path` and returns the value(s) of the first line without `*` at the end, then adds a `*` to this line and saves the file.
    
- `writeQuestionnaire(header, dict, name, expName, localPath, netwPath, id, condition = False, sep = "\t")`:
Append content of single dictionnary `dict` (with keys given in `header`) to file `(expName + '_' + name + '.txt')` at locations `localPath` and `netwPath` using separator `sep`.

- `writeResults(header, testLists, expName, localPath, netwPath, id, extra = "", extension = "rtd", printHeader = True, mode = "w", sep = "\t")`: Write lists of dictionaries `testList` (or list of lists of dictionaries) with keys given in `header` to file `(expName + '_' + extra + str(id) +'.' + extension)` at locations `localPath` and `netwPath` using separator `sep`.

# button.py
Contains functions `introOneButton` and `introTwoButton` for displaying introductory screens (usually png files produced in PowerPoint) with one or two buttons (with hover effect) for pressing continue. Both functions need quite some objects to work.

# final.py
This file contains the final routines in an experiment: obtain demographic data, ask participants for any comments, write this. The code to invoke this is usually:

    import final
    
    if TEST:
        endWin = visual.Window((1920,1080),allowGUI=True, monitor='sozPsyMon2', fullscr=False, units ='norm', color = BGCOLOR, winType='pyglet', screen = 1)
    else:
        endWin = visual.Window((1920,1080),allowGUI=True, monitor='sozPsyMon2', fullscr=False, units ='norm', color = BGCOLOR, winType='pyglet')
    
    endWin.flip()
    endWin.setMouseVisible(True)
    
    demoDict = {"age": 0, "sex": "", "occupation1": "", "occupation2": "", "sight":"", "sightDioptre":"", "sightProblem":"", "colorVision": True, "comment":""}
    headerDemo = ["age", "sex", "occupation1", "occupation2", "sight", "sightProblem", "sightDioptre", "colorVision"]
    
    final.getDemographics(demoDict, endWin, id, cond, LOCALPATH, NETWPATH, EXPNAME, headerDemo, sep = "|")
    endWin.flip()
    ende2 = visual.SimpleImageStim(endWin, PATH_TO_FINAL_SCREEN, pos=(0,0))
    ende2.draw()
    endWin.flip()
    
    event.waitKeys(300, ['s'])
    
    endWin.close()
    core.quit()
