__author__ = 'Razvan'
from tkinter import *
from Draw import*
from Representation import*
FilledRow = 0
FilledRowsDeleted = 0
def rotateFallingPiece(model):
    square = model["square"]
    square2 = model["square2"]
    square3 = model["square3"]
    square4 = model["square4"]

    square2Xcoord=square["x"]-square2["x"]
    square3Xcoord=square["x"]-square3["x"]
    square4Xcoord=square["x"]-square4["x"]
    square2Ycoord=square["y"]-square2["y"]
    square3Ycoord=square["y"]-square3["y"]
    square4Ycoord=square["y"]-square4["y"]
    square2["x"]= square["x"]-square2Ycoord
    square2["y"]= square["y"]+square2Xcoord
    square3["x"]= square["x"]-square3Ycoord
    square3["y"]= square["y"]+square3Xcoord
    square4["x"]= square["x"]-square4Ycoord
    square4["y"]= square["y"]+square4Xcoord
    SpaceCheck(model)

def onkey(model, keycode):
    # called when user presses a key

    square = model["square"]
    square2 = model["square2"]
    square3 = model["square3"]
    square4 = model["square4"]
    GameOver(model)


    if keycode==37:  # LeftArrow
        if square["x"]>0 and square2["x"]>0 and square3["x"]>0 and square4["x"]>0 and LookForSpaceLeft(model):
            xdecrement(model)

    elif keycode==38: #Block rotates
        rotateFallingPiece(model)
    elif keycode==39:  # RightArrow
        #print(keycode)
        square = model["square"]
        if square["x"]<9 and square2["x"]<9 and square3["x"]<9 and square4["x"]<9 and LookForSpaceRight(model):
           xincrement(model)

    elif keycode==40:  # DownArrow
        square = model["square"]
        if square["y"]<19 and square2["y"]<19 and square3["y"]<19 and square4["y"]<19 and LookForSpaceUnder(model):
            yincrement(model)
def FilledRowCheck(model):

    setPieces = model["setPieces"]
    for iY in range(0,19,1):
        FilledBlocks =0
        for iX in range(0,9,1):
            if {'y': iY, 'x': iX}  in setPieces:
                FilledBlocks +=1
            if FilledBlocks ==10:
                for iZ in range(0,9,1):
                    setPieces[:] = [d for d in setPieces if d.get('y') != iZ]


def FilledRowDelete(model):
    setPieces = model["setPieces"]
    for i in range(0,20,1):
        for iY in range(0,20,1):
            if  {'y': iY, 'x': 0} in setPieces:
                if  {'y': iY, 'x': 1} in setPieces:
                    if  {'y': iY, 'x': 2} in setPieces:
                        if  {'y': iY, 'x': 3} in setPieces:
                            if  {'y': iY, 'x': 4} in setPieces:
                                if  {'y': iY, 'x': 5} in setPieces:
                                    if  {'y': iY, 'x': 6} in setPieces:
                                        if  {'y': iY, 'x': 7} in setPieces:
                                            if  {'y': iY, 'x': 8} in setPieces:
                                                if  {'y': iY, 'x': 9} in setPieces:

                                                    setPieces[:] = [d for d in setPieces if d.get('y') != iY]
                                                    #CollapseRowsOntoEmptyRow(model)


def CollapseRowsOntoEmptyRow(model):
    setPieces = model["setPieces"]

    for iY in range(20,0,-1):
        if  {'y': iY, 'x': 0} not in setPieces:
            if  {'y': iY, 'x': 1} not in setPieces:
                if  {'y': iY, 'x': 2} not in setPieces:
                    if  {'y': iY, 'x': 3} not in setPieces:
                        if  {'y': iY, 'x': 4} not in setPieces:
                            if  {'y': iY, 'x': 5} not in setPieces:
                                if  {'y': iY, 'x': 6} not in setPieces:
                                    if  {'y': iY, 'x': 7} not in setPieces:
                                        if  {'y': iY, 'x': 8} not in setPieces:
                                            if  {'y': iY, 'x': 9} not in setPieces:
                                                #for datadict in setPieces:
                                                 #   for key, value in datadict.items():
                                                  #      print(datadict.items())
                                                   #     if value == (iY):
                                                    #        datadict[key] = (iY+1)
                                                setPieces[:] = [d for d in setPieces if d.get("y") == iY]
                                                setPieces.append({'y': iY+1, 'x': 0})
                                                setPieces[:] = [d for d in setPieces if d.get("y") == iY]
                                                setPieces.append({'y': iY+1, 'x': 1})
                                                setPieces[:] = [d for d in setPieces if d.get("y") == iY]
                                                setPieces.append({'y': iY+1, 'x': 2})
                                                setPieces[:] = [d for d in setPieces if d.get("y") == iY]
                                                setPieces.append({'y': iY+1, 'x': 3})
                                                setPieces[:] = [d for d in setPieces if d.get("y") == iY]
                                                setPieces.append({'y': iY+1, 'x': 4})
                                                setPieces[:] = [d for d in setPieces if d.get("y") == iY]
                                                setPieces.append({'y': iY+1, 'x': 5})
                                                setPieces[:] = [d for d in setPieces if d.get("y") == iY]
                                                setPieces.append({'y': iY+1, 'x': 6})
                                                setPieces[:] = [d for d in setPieces if d.get("y") == iY]
                                                setPieces.append({'y': iY+1, 'x': 7})
                                                setPieces[:] = [d for d in setPieces if d.get("y") == iY]
                                                setPieces.append({'y': iY+1, 'x': 8})
                                                setPieces[:] = [d for d in setPieces if d.get("y") == iY]
                                                setPieces.append({'y': iY+1, 'x': 9})



def LookForSpaceUnder(model):
    #Look for pieces under current moving piece
    setPieces = model["setPieces"]
    square = model["square"]
    square2 = model["square2"]
    square3 = model["square3"]
    square4 = model["square4"]
    for Piece in setPieces:
        if (Piece["x"]==square["x"] and Piece["y"]==square["y"]+1) \
            or (Piece["x"]==square2["x"] and Piece["y"]==square2["y"]+1) \
            or (Piece["x"]==square3["x"] and Piece["y"]==square3["y"]+1) \
            or Piece["x"]==square4["x"] and Piece["y"]==square4["y"]+1:
            return False
    return True
def LookForSpaceLeft(model):
    #Look for pieces left from the current moving piece
    setPieces = model["setPieces"]
    square = model["square"]
    square2 = model["square2"]
    square3 = model["square3"]
    square4 = model["square4"]
    for Piece in setPieces:
        if (Piece["x"]==square["x"]-1 and Piece["y"]==square["y"]) \
            or (Piece["x"]==square2["x"]-1 and Piece["y"]==square2["y"]) \
            or (Piece["x"]==square3["x"]-1 and Piece["y"]==square3["y"]) or \
                Piece["x"]==square4["x"]-1 and Piece["y"]==square4["y"]:
            return False
    return True
def LookForSpaceRight(model):
   #Look for pieces right from the current moving piece
    setPieces = model["setPieces"]
    square = model["square"]
    square2 = model["square2"]
    square3 = model["square3"]
    square4 = model["square4"]
    for Piece in setPieces:
        if (Piece["x"]==square["x"]+1 and Piece["y"]==square["y"]) \
            or (Piece["x"]==square2["x"]+1 and Piece["y"]==square2["y"]) \
            or (Piece["x"]==square3["x"]+1 and Piece["y"]==square3["y"]) \
            or Piece["x"]==square4["x"]+1 and Piece["y"]==square4["y"]:
            return False
    return True
def SpaceCheck(model):
    square = model["square"]
    square2 = model["square2"]
    square3 = model["square3"]
    square4 = model["square4"]

    if not (LookForSpaceLeft(model)
            and square["x"]>0 and square2["x"]>0
            and square3["x"]>0 and square4["x"]>0):
        xincrement(model)
        if not (LookForSpaceLeft(model)
                and square["x"]>0 and square2["x"]>0
                and square3["x"]>0 and square4["x"]>0):
            xincrement(model)
    if not (LookForSpaceRight(model)
            and square["x"]<10 and square2["x"]<10
            and square3["x"]<10 and square4["x"]<10):
        xdecrement(model)
        if not (LookForSpaceRight(model)
                and square["x"]<10 and square2["x"]<10
                and square3["x"]<10 and square4["x"]<10):
           xdecrement(model)
    if not (LookForSpaceUnder(model)
            and square["y"]<19 and square2["y"]<19
            and square3["y"]<19 and square4["y"]<19):
        ydecrement(model)
        if not (LookForSpaceUnder(model)
                and square["y"]<19 and square2["y"]<19
                and square3["y"]<19 and square4["y"]<19):
            ydecrement(model)
def GameOver(model):
    #code to check if there can be any new blocks spawned if not > sys exit
        setPieces = model["setPieces"]
        if ({'y': 0, 'x': 4}or {'y': 0, 'x': 5} or {'y': 0, 'x': 6} or {'y': 0, 'x': 7})  in setPieces:
            sys.exit()


def yincrement(model):
    square = model["square"]
    square2 = model["square2"]
    square3 = model["square3"]
    square4 = model["square4"]
    square["y"] += 1
    square2["y"] += 1
    square3["y"] += 1
    square4["y"] += 1
def ydecrement(model):
    square = model["square"]
    square2 = model["square2"]
    square3 = model["square3"]
    square4 = model["square4"]
    square["y"] -= 1
    square2["y"] -= 1
    square3["y"] -= 1
    square4["y"] -= 1
def xdecrement(model):
    square = model["square"]
    square2 = model["square2"]
    square3 = model["square3"]
    square4 = model["square4"]
    square["x"] -= 1
    square2["x"] -= 1
    square3["x"] -= 1
    square4["x"] -= 1
def xincrement(model):
    square = model["square"]
    square2 = model["square2"]
    square3 = model["square3"]
    square4 = model["square4"]
    square["x"] += 1
    square2["x"] += 1
    square3["x"] += 1
    square4["x"] += 1