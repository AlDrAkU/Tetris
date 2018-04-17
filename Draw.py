__author__ = 'Razvan'
from tkinter import *
from Control import*
import random
from Representation import*
def draw(model, canvas):
    # called after onkey() and onloop(), so every
    # X milliseconds and after each time the user
    # presses a key
    canvas.delete(ALL)
    # clear canvas

    block_height = 20
    block_margin = 4
    dimensions = model["dimensions"]
    square = model["square"]
    square2 = model["square2"]
    square3 = model["square3"]
    square4 = model["square4"]
    setPieces = model["setPieces"]

    for x in range(dimensions[0]):
        for y in range(dimensions[1]):
            color = "#f2f2f2"
            # default color of empty piece
            if (x==square["x"] and y==square["y"]) \
                    or (x==square2["x"] and y==square2["y"]) \
                    or (x==square3["x"] and y==square3["y"]) \
                    or (x==square4["x"] and y==square4["y"]):
                    color = "#ff0000"
                # color of filled piece
            rect = canvas.create_rectangle(
                x * block_height + (x + 1) * block_margin,
                y * block_height + (y + 1) * block_margin,
                (x + 1) * block_height + (x + 1) * block_margin,
                (y + 1) * block_height + (y + 1) * block_margin,
                fill=color, outline=color)
            # draws a rectangle
            #ColorSelect()
            for Piece in setPieces:
                if x==Piece["x"] and y==Piece["y"]:
                    color = "#ff0000"
                    rect = canvas.create_rectangle(
                    x*block_height+(x+1)*block_margin,
                    y*block_height+(y+1)*block_margin,
                    (x+1)*block_height+(x+1)*block_margin,
                    (y+1)*block_height+(y+1)*block_margin,
                   fill=color, outline=color)
def GeneratePiece(model):

    #Generate new tetris piece
    randomShape = random.randint(1,7)
    if randomShape==1: #O-piece
        model["square"] = {"x":5,"y":0}
        model["square2"] = {"x":6,"y":0}
        model["square3"] = {"x":5,"y":1}
        model["square4"] = {"x":6,"y":1}
        color = "#ff0000"
    elif randomShape==2: #J-piece
        model["square"] = {"x":5,"y":0}
        model["square2"] = {"x":6,"y":0}
        model["square3"] = {"x":4,"y":0}
        model["square4"] = {"x":6,"y":1}
        color= "#7cfc00"
    elif randomShape==3: #L-piece
        model["square"] = {"x":5,"y":0}
        model["square2"] = {"x":4,"y":0}
        model["square3"] = {"x":6,"y":0}
        model["square4"] = {"x":4,"y":1}
        color = "#6495ed"
    elif randomShape==4: #T-piece
        model["square"] = {"x":5,"y":0}
        model["square2"] = {"x":4,"y":0}
        model["square3"] = {"x":5,"y":1}
        model["square4"] = {"x":6,"y":0}
        color = "#ffff00"
    elif randomShape==5: #S-piece
        model["square"] = {"x":5,"y":0}
        model["square2"] = {"x":4,"y":0}
        model["square3"] = {"x":5,"y":1}
        model["square4"] = {"x":6,"y":1}
        color = "#9400d3"
    elif randomShape==6: #Z-piece
        model["square"] = {"x":4,"y":0}
        model["square2"] = {"x":5,"y":0}
        model["square3"] = {"x":4,"y":1}
        model["square4"] = {"x":3,"y":1}
        color= "#ffa500"
    elif randomShape==7: #I-piece
        model["square"] = {"x":4,"y":0}
        model["square2"] = {"x":3,"y":0}
        model["square3"] = {"x":5,"y":0}
        model["square4"] = {"x":6,"y":0}
        color= "#ffdab9"
    return model

def ColorSelect():
    randomColor = random.randint(1,7)

    if randomColor == 1:
        color = "#ff0000"
    elif randomColor == 2:
        color= "#7cfc00"
    elif randomColor == 3:
        color = "#6495ed"
    elif randomColor == 4:
        color = "#ffff00"
    elif randomColor == 5:
        color = "#9400d3"
    elif randomColor == 6:
        color= "#ffa500"
    elif randomColor == 7:
        color= "#ffdab9"


