#!/usr/bin/env python
# -*- coding: utf-8 -*-

from psychopy import visual, event

def introOneButton(win, mouse, file, pos, sizeText, widthBox, heightBox, fgColor = "Black", 
    bgColor = "#c0c0c0", hoverColor = "#999999", borderColor = "White", text = "Weiter", units = "norm"):
    #introS = visual.SimpleImageStim(win, file, pos=(0,0))
    intro = visual.ImageStim(win, file, pos=(0,0), interpolate=True)
    text = visual.TextStim(win, text = text, pos = pos, height = sizeText, color = fgColor, units = units)
    box = visual.Rect(win, pos = pos, width  = widthBox, height = heightBox, lineColor = borderColor, units = units)
    Continue = False
    while not(Continue):
        intro.draw()
        box.setFillColor(bgColor)
        if box.contains(mouse):
            box.setFillColor(hoverColor)
        box.draw()
        text.draw()
        win.flip()
        inside = False
        if box.contains(mouse) & mouse.getPressed()[0]:
            inside = True
        while mouse.getPressed()[0]:
            Continue = False
            intro.draw()
            box.setFillColor(bgColor)
            if box.contains(mouse):
                box.setFillColor(hoverColor)
            box.draw()
            text.draw()
            win.flip()
            if box.contains(mouse) and inside:
                Continue = True
    win.flip()

def waitButton(win, mouse, stim, pos, sizeText, widthBox, heightBox, fgColor = "Black", 
    bgColor = "#c0c0c0", hoverColor = "#999999", borderColor = "White", text = "Weiter", units = "norm"):
    text = visual.TextStim(win, text = text, pos = pos, height = sizeText, color = fgColor, units = units)
    box = visual.Rect(win, pos = pos, width  = widthBox, height = heightBox, lineColor = borderColor, units = units)
    Continue = False
    while not(Continue):
        [s.draw() for s in stim]
        box.setFillColor(bgColor)
        if box.contains(mouse):
            box.setFillColor(hoverColor)
        box.draw()
        text.draw()
        win.flip()
        inside = False
        if box.contains(mouse) & mouse.getPressed()[0]:
            inside = True
        while mouse.getPressed()[0]:
            Continue = False
            [s.draw() for s in stim]
            box.setFillColor(bgColor)
            if box.contains(mouse):
                box.setFillColor(hoverColor)
            box.draw()
            text.draw()
            win.flip()
            if box.contains(mouse) and inside:
                Continue = True
    win.flip()
    
def introTwoButton(win, mouse, file, pos1, pos2, sizeText, widthBox, heightBox, fgColor = "Black", 
    bgColor = "#c0c0c0", hoverColor = "Blue", borderColor = "White", text1 = "Wiederholen", text2 = "Weiter", units = "norm"):
    intro = visual.ImageStim(win, file, pos=(0,0), interpolate=True)
    text1 = visual.TextStim(win, text = text1, pos = pos1, height = sizeText, color = fgColor, units = units)
    box1 = visual.Rect(win, pos = pos1, width  = widthBox, height = heightBox, lineColor = borderColor, units = units)
    text2 = visual.TextStim(win, text = text2, pos = pos2, height = sizeText, color = fgColor, units = units)
    box2 = visual.Rect(win, pos = pos2, width  = widthBox, height = heightBox, lineColor = borderColor, units = units)
    Continue = False
    Back = False
    while not(Continue) and not(Back):
        intro.draw()
        box1.setFillColor(bgColor)
        box2.setFillColor(bgColor)
        if box1.contains(mouse):
            box1.setFillColor(hoverColor)
            if mouse.getPressed()[0]:
                Back = True
        if box2.contains(mouse):
            box2.setFillColor(hoverColor)
            if mouse.getPressed()[0]:
                Continue = True
        box1.draw()
        text1.draw()
        box2.draw()
        text2.draw()
        win.flip()
    win.flip()
    if Continue:
        return True
    else:
        return False

