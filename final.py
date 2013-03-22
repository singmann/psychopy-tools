#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import wx.richtext as rt
import os
import codecs
from psychopy import *

class demographics(wx.Frame):    
    def __init__(self, parent, id, title, demoDict):
        activeID = -1
        activeID2 = -1
        self.demoDict = demoDict
        borderX = 80
        borderX2 = borderX + 20
        borderX3 = borderX2 + 140
        posItems = 180
        spaceX = 55
        wx.Frame.__init__(self, parent, id, title, style=wx.BORDER_NONE | wx.STAY_ON_TOP, size=(1000, 900))
        self.SetBackgroundColour((192, 192, 192))
        self.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.NORMAL))
        
        str1 = u"Sie haben das Ende des Experiments erreicht!"
        text = wx.StaticText(self, -1, str1, (180, 50), )
        font = wx.Font(24, wx.SWISS, wx.NORMAL, wx.NORMAL)
        text.SetFont(font)
        
        str2 = u"Zum Schluss benötigen wir nur noch ein paar Angaben zu Ihrer Person.\nBenutzen Sie bitte Maus und Tastatur um diese Angaben zu machen."
        text = wx.StaticText(self, -1, str2, (borderX, 140), )
        font = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.NORMAL)
        text.SetFont(font)
        
        #wx.StaticBox(self, -1, "Demographische Angaben", (borderX, posItems), (840,500))
        
        wx.StaticText(self, -1, "Ihr Alter:", (borderX2, posItems + 1*spaceX))
        self.age = wx.SpinCtrl(self, -1, '', (borderX3, posItems + 1*spaceX - 3), (60, -1), min=0, max=99)
        
        self.Bind(wx.EVT_SPINCTRL, self.OnAgeSelect, self.age)
        
        wx.StaticText(self, -1, "Ihr Geschlecht:", (borderX2, posItems + 2*spaceX))
        self.sex = []
        self.sex1 = wx.RadioButton(self, 1, 'weiblich', (borderX3, posItems + 2*spaceX), (110, -1))
        self.sex2 = wx.RadioButton(self, 1, u'männlich', (borderX3 + 110, posItems + 2*spaceX), (110, -1))
        self.sex3 = wx.RadioButton(self, 1, 'keine Angabe', (borderX3 + 2*110, posItems + 2*spaceX), (180, -1))
        self.sex.append(self.sex1)
        self.sex.append(self.sex2)
        self.sex.append(self.sex3)
        
        for radio in self.sex:
            self.Bind(wx.EVT_RADIOBUTTON, self.OnSexSelect, radio )            
        
        wx.StaticBox(self, -1, u"Ihre Tätigkeit", (borderX2, posItems + 3*spaceX), (800,220))
        self.occupationButton = []
        self.occupationText = []
        self.occupation1 = wx.RadioButton(self, 10, 'StudentIn (Studienfach bitte angeben)', (borderX2 + 15, posItems + 3*spaceX+30), (400, -1), style = wx.RB_GROUP )
        self.text1 = wx.TextCtrl( self, 101, "" , pos = (borderX2 + 15 + 400, posItems + 3*spaceX+30-3), size = (350,-1))
        self.occupation2 = wx.RadioButton(self, 11, 'AuszubildendeR (Beruf bitte angeben)', (borderX2 + 15, posItems + 3*spaceX+70), (400, -1))
        self.text2 = wx.TextCtrl( self, 111, "" , pos = (borderX2 + 15 + 400, posItems + 3*spaceX+70-3), size = (350,-1))
        self.occupation3 = wx.RadioButton(self, 12, u'Angestellt / Selbstständig (als)', (borderX2 + 15, posItems + 3*spaceX+110), (400, -1))
        self.text3 = wx.TextCtrl( self, 121, "" , pos = (borderX2 + 15 + 400, posItems + 3*spaceX+110-3), size = (350,-1))
        self.occupation4 = wx.RadioButton(self, 13, u'SchülerIn', (borderX2 + 15, posItems + 3*spaceX+150), (400, -1))
        self.occupation5 = wx.RadioButton(self, 14, u'Ohne Tätigkeit / Arbeitslos', (borderX2 + 15, posItems + 3*spaceX+190), (400, -1))
        
        self.occupationButton.append(self.occupation1)
        self.occupationButton.append(self.occupation2)
        self.occupationButton.append(self.occupation3)
        self.occupationButton.append(self.occupation4)
        self.occupationButton.append(self.occupation5)
        
        self.occupationText.append(self.text1)
        self.occupationText.append(self.text2)
        self.occupationText.append(self.text3)
        
        for radio in self.occupationButton:
            radio.SetValue(0)
            self.Bind(wx.EVT_RADIOBUTTON, self.OnOccupationSelect, radio )

        for text in self.occupationText:
            text.Enable(False)
        
        
        wx.StaticBox(self, -1, u"Ihre Sehfähigkeit", (borderX2, posItems + 8*spaceX), (800,200))
        self.sightButton = []
        self.sightText =[]
        self.sight1 = wx.RadioButton(self, 21, u'Sehfähigkeit uneingeschränkt', (borderX2 + 15, posItems + 8*spaceX+30), (400, -1), style = wx.RB_GROUP )
        self.sight2 = wx.RadioButton(self, 22, u'Sehfähigkeit eingeschränkt, Sehhilfe (Brille, Kontaktlinsen) wird getragen.', (borderX2 + 15, posItems + 8*spaceX+70), (680, -1) )
        self.sight3 = wx.RadioButton(self, 23, u'Sehfähigkeit eingeschränkt, Sehhilfe (Brille, Kontaktlinsen) wird NICHT getragen.', (borderX2 + 15, posItems + 8*spaceX+110), (700, -1) )
        self.sightButton.append(self.sight1)
        self.sightButton.append(self.sight2)
        self.sightButton.append(self.sight3)
        wx.StaticText(self, -1, u"Außerdem:", (borderX2+15, posItems + 8*spaceX+145))
        self.color = wx.CheckBox(self, 24, u"Farbsehschwäche (z.B. Rot-Grün Blindheit) liegt vor",(borderX2+15, posItems + 8*spaceX+170), style = wx.ALIGN_RIGHT)
        
        for radio in self.sightButton:
            radio.SetValue(0)
            self.Bind(wx.EVT_RADIOBUTTON, self.OnSightSelect, radio )

        for text in self.sightText:
            text.Enable(False)
        
        
        self.ok = wx.Button(self, wx.ID_OK, 'Ok', (470,850), (60, -1))
        self.ok.Disable()
        
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=wx.ID_OK)
        
        
        self.Centre()
        self.Show(True)
    
    def CheckButton(self, event):
        if (self.demoDict["age"] > 15 & self.demoDict["age"] < 100) & ( self.demoDict["sex"] != "") & ( self.demoDict["occupation1"] != "" ) & (self.demoDict["sight"] != ""):
            self.ok.Enable()
        else:
            self.ok.Disable()
    
    def OnAgeSelect(self, event):
        self.demoDict["age"] = self.age.GetValue()
        self.CheckButton(event)
    
    def OnSexSelect(self, event):
        selected = event.GetEventObject()
        self.demoDict["sex"] = selected.GetLabel()
        self.CheckButton(event)
        
    def OnOccupationSelect(self, event):
        global activeID
        activeID = -1
        selected = event.GetEventObject()
        cId = (10 * selected.GetId()) + 1
        self.demoDict["occupation1"] = selected.GetLabel()
        for text in self.occupationText:
            if text.GetId() is cId:
                activeID = cId
                text.Enable(True)
            else:
                text.Enable(False)
        self.CheckButton(event)
    
    def OnSightSelect(self, event):
        global activeID2
        activeID2 = -1
        selected = event.GetEventObject()
        cId = (10 * selected.GetId()) + 1
        self.demoDict["sight"] = selected.GetLabel()
#        for text in self.sightText:
#            if text.GetId() is cId:
#                activeID2 = cId
#                text.Enable(True)
#            else:
#                text.Enable(False)
        self.CheckButton(event)
    
    def OnClose(self, event):
        for text in self.occupationText:
            if text.GetId() is activeID:
                self.demoDict["occupation2"] = text.GetValue()
        if self.color.IsChecked():
            self.demoDict["colorVision"] = False
        self.Close()



class final(wx.Frame):    
    def __init__(self, parent, id, title, demoDict):
        self.demoDict = demoDict
        borderX = 80
        borderX2 = borderX + 10
        borderX3 = borderX2 + 80
        posItems = 180
        spaceX = 50
        wx.Frame.__init__(self, parent, id, title, style=wx.BORDER_NONE | wx.STAY_ON_TOP, size=(1000, 500))
        self.SetBackgroundColour((192, 192, 192))
        self.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.NORMAL))
        
        str1 = u"Sie haben das Ende des Experiments erreicht!"
        text = wx.StaticText(self, -1, str1, (180, 50), )
        font = wx.Font(24, wx.SWISS, wx.NORMAL, wx.NORMAL)
        text.SetFont(font)
        
        str2 = u"Als letztes haben Sie nun noch die Möglichkeit, uns etwas mitzuteilen.\nIst Ihnen etwas Komisches an dem Experiment aufgefallen?\nHaben Sie das Gefühl, das Experiment ist nicht so gelaufen, wie es sollte?\nBitte tragen Sie in das Feld all das ein, was Sie uns mitteilen möchten."
        text = wx.StaticText(self, -1, str2, (borderX, 140), )
        font = wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL)
        text.SetFont(font)
        
        self.t3 = wx.TextCtrl(self, -1, "", pos = (borderX, 300),  size=(800, 100), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        self.ok = wx.Button(self, wx.ID_OK, 'Ok', (470,450), (60, -1))        
        
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=wx.ID_OK)
        
        
        self.Centre()
        self.Show(True)
            
    def OnClose(self, event):
        self.demoDict["comment"] = self.t3.GetValue()
        self.Close()




class sightProblems(wx.Frame):    
    def __init__(self, parent, id, title, demoDict):
        self.demoDict = demoDict
        borderX = 80
        borderX2 = borderX + 10
        borderX3 = borderX2 + 80
        posItems = 180
        spaceX = 50
        wx.Frame.__init__(self, parent, id, title, style=wx.BORDER_NONE | wx.STAY_ON_TOP, size=(1000, 500))
        self.SetBackgroundColour((192, 192, 192))
        self.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.NORMAL, wx.NORMAL))
        
        str1 = u"Achtung: Sie haben angegeben das Ihre Sehfähigkeit \neingeschränkt ist, Sie aber trotzdem keine Sehhilfe \n(Brille oder Kontaktlinse) tragen!"
        text = wx.StaticText(self, -1, str1, (100, 50), )
        font = wx.Font(24, wx.SWISS, wx.NORMAL, wx.NORMAL)
        text.SetFont(font)
        
        wx.StaticText(self, -1, "Wie hoch ist Ihr Dioptriewert (ca.):", (borderX2, posItems + 1*spaceX))
        self.dioptrie = wx.TextCtrl( self, 101, "" , pos = (borderX2, posItems + 1.6*spaceX), size = (220,-1))
        
        wx.StaticText(self, -1, u"Wie stark hat Ihre Sehschwäche die Bearbeitung des Experimentes beinträchtigt?", (borderX2, posItems + 2.8*spaceX))
        self.nosee = []
        self.nosee1 = wx.RadioButton(self, 11, 'gar nicht', (borderX2, posItems + 3.5*spaceX), (140, -1))
        self.nosee2 = wx.RadioButton(self, 12, 'etwas', (borderX2 + 140, posItems + 3.5*spaceX), (140, -1))
        self.nosee3 = wx.RadioButton(self, 13, 'deutlich', (borderX2 + 2*140, posItems + 3.5*spaceX), (140, -1))
        self.nosee4 = wx.RadioButton(self, 14, 'stark', (borderX2 + 3*140, posItems + 3.5*spaceX), (140, -1))
        self.nosee5 = wx.RadioButton(self, 15, 'sehr stark', (borderX2 + 4*140, posItems + 3.5*spaceX), (140, -1))
        self.nosee.append(self.nosee1)
        self.nosee.append(self.nosee2)
        self.nosee.append(self.nosee3)
        self.nosee.append(self.nosee4)
        self.nosee.append(self.nosee5)
        
        for radio in self.nosee:
            self.Bind(wx.EVT_RADIOBUTTON, self.OnNoseeSelect, radio )
        
        self.ok = wx.Button(self, wx.ID_OK, 'Ok', (470,450), (60, -1))        
        
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=wx.ID_OK)
        self.ok.Disable()
        
        self.Centre()
        self.Show(True)
            
    def OnNoseeSelect(self, event):
        selected = event.GetEventObject()
        self.demoDict["sightProblem"] = selected.GetLabel()
        self.CheckButton(event)
    
    def CheckButton(self, event):
        #print(str(self.demoDict["sightProblem"]))
        #print(str(self.dioptrie.GetValue()))
        if ((self.demoDict["sightProblem"] != u"") & (self.dioptrie.GetValue() != u"")):
            self.ok.Enable()
        else:
            self.ok.Disable()
    
    def OnClose(self, event):
        self.demoDict["sightDioptre"] = self.dioptrie.GetValue()
        self.Close()



class Password(wx.Frame):
    def __init__(self, parent, id, title):
        borderX = 80
        wx.Frame.__init__(self, parent, id, title, style=wx.BORDER_NONE | wx.STAY_ON_TOP, size=(1000, 900))
        self.SetBackgroundColour((192, 192, 192))
        
        str1 = u"Sie haben das Ende des Experiments erreicht!"
        text = wx.StaticText(self, -1, str1, (180, 50), )
        font = wx.Font(24, wx.SWISS, wx.NORMAL, wx.NORMAL)
        text.SetFont(font)
        
        str2 = u"Bitte benachrichtigen Sie die Versuchsleitung."
        text = wx.StaticText(self, -1, str2, (borderX, 140), )
        font = wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL)
        text.SetFont(font)
        self.previous = -1

        panel = wx.Panel(self, -1)
        panel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        panel.SetFocus()

        self.Centre()
        self.Show(True)


    def OnKeyDown(self, event):
        keycode = event.GetKeyCode()
        if (self.previous == 306) & (keycode == 49):
                self.Close()
        self.previous = keycode
        event.Skip()


def getDemographics(demoDict, endWin, id, cond, localPath, netwPath, expName, headerDemo, sep = ";"):
    app = wx.App(False)
    demos = demographics(None, -1, 'demographics', demoDict)
    #endWin.flip()
    app.MainLoop()
    if (demoDict["sight"] == u'Sehfähigkeit eingeschränkt, Sehhilfe (Brille, Kontaktlinsen) wird NICHT getragen.'):
        endWin.flip()
        demos = sightProblems(None, -1, 'sightProblems', demoDict)
        app.MainLoop()
    data = map(demoDict.get, headerDemo)
    if os.path.exists(localPath):
        demoL = codecs.open(os.path.join(localPath, (expName + "_demographics.dat")) ,'a', encoding='utf-8')
        demoL.write(unicode(id))
        demoL.write(sep)
        demoL.write(unicode(cond))
        demoL.write(sep)
        for dat in data:
            demoL.write(unicode(dat))
            demoL.write(sep)
        demoL.write("\n")
        demoL.close()
    else:
        print("\n\nERROR: Local drive not accessible!!\n\n")
    if os.path.exists(netwPath):
        demoN = codecs.open(os.path.join(netwPath, (expName + "_demographics.dat")) ,'a', encoding='utf-8')
        demoN.write(unicode(id))
        demoN.write(sep)
        demoN.write(unicode(cond))
        demoN.write(sep)
        for dat in data:
            demoN.write(unicode(dat))
            demoN.write(sep)
        demoN.write("\n")
        demoN.close()  
    else:
        print("\n\nERROR: Network drive not accessible!!\n\n")
    endWin.flip()
    other = final(None, -1, 'final', demoDict)
    endWin.flip()
    app.MainLoop()
    if demoDict["comment"] != "":
        if os.path.exists(localPath):
            if not(os.path.exists(os.path.join(localPath, "comments"))):
                os.mkdir(os.path.join(localPath, "comments"))
            commentFile = codecs.open(os.path.join(localPath, "comments", (expName + "_comment_" + str(id) + ".txt")) ,'a', encoding='utf-8')
            commentFile.write(unicode(demoDict["comment"]))
            commentFile.write("\n")
            commentFile.write("####################end##################\n")
            commentFile.write("\n")
            commentFile.close()
        if os.path.exists(netwPath):
            if not(os.path.exists(os.path.join(netwPath, "comments"))):
                os.mkdir(os.path.join(netwPath, "comments"))
            commentFile = codecs.open(os.path.join(netwPath, "comments\\" , (expName + "_comment_" + str(id) + ".txt")) ,'a', encoding='utf-8')
            commentFile.write(unicode(demoDict["comment"]))
            commentFile.write("\n")
            commentFile.write("####################end##################\n")
            commentFile.write("\n")
            commentFile.close()       
    #endWin.flip()
    #pw = Password(None, -1, 'pw')
    #endWin.flip()
    #app.MainLoop()
    
def getComments(demoDict, endWin, id, localPath, netwPath, expName):
    app = wx.App(False)
    other = final(None, -1, 'final', demoDict)
    endWin.flip()
    app.MainLoop()
    if demoDict["comment"] != "":
        if os.path.exists(localPath):
            if not(os.path.exists(os.path.join(localPath, "comments"))):
                os.mkdir(os.path.join(localPath, "comments"))
            commentFile = codecs.open(os.path.join(localPath, "comments", (expName + "_comment_" + str(id) + ".txt")) ,'a', encoding='utf-8')
            commentFile.write(unicode(demoDict["comment"]))
            commentFile.write("\n")
            commentFile.write("####################end##################\n")
            commentFile.write("\n")
            commentFile.close()
        if os.path.exists(netwPath):
            if not(os.path.exists(os.path.join(netwPath, "comments"))):
                os.mkdir(os.path.join(netwPath, "comments"))
            commentFile = codecs.open(os.path.join(netwPath, "comments\\" , (expName + "_comment_" + str(id) + ".txt")) ,'a', encoding='utf-8')
            commentFile.write(unicode(demoDict["comment"]))
            commentFile.write("\n")
            commentFile.write("####################end##################\n")
            commentFile.write("\n")
            commentFile.close()       
    #endWin.flip()
    #pw = Password(None, -1, 'pw')
    #endWin.flip()
    #app.MainLoop()

if __name__ == '__main__':
    demoDict = {"age": 0, "sex": "", "occupation1": "", "occupation2": "", "sight":"", "sightDioptre":"", "sightProblem":"", "colorVision": True, "comment":""}
    app = wx.App(False)
    #demos = demographics(None, -1, 'demographics', demoDict)
    #app.MainLoop()
    #if (demoDict["sight"] == u'Sehfähigkeit eingeschränkt, Sehhilfe (Brille, Kontaktlinsen) wird NICHT getragen.'):
    demos = sightProblems(None, -1, 'sightProblems', demoDict)
    app.MainLoop()
    other = final(None, -1, 'final', demoDict)
    app.MainLoop()
    pw = Password(None, -1, 'pw')
    app.MainLoop()
    print(demoDict)



