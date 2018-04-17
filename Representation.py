__author__ = 'Razvan'
from tkinter import *
from Control import*
from Draw import*
def initialize():
    # called once when the game is started (main() executed)
    # [ put your own model/representation 
    # initialization here ]
    return {"dimensions": (10, 20),
            "square": {"x":5, "y":0}
            ,"square2": {"x":6,"y":0}
            ,"square3": {"x":5,"y":1}
            ,"square4": {"x":6,"y":1}
            , "square5": {"x": 7, "y": 0}
            , "square6": {"x": 5, "y": 2}
            , "square7": {"x": 7, "y": 1}
            , "square8": {"x": 6, "y": 2}
            , "square9": {"x": 7, "y": 2}
            ,"setPieces":[]}
    # the data structure returned from this method
    # is passed as parameter ''model'' to the functions
    # draw(), onkey() and onloop() below

def onloop(model):
    # called every X milliseconds
    square = model["square"]
    square2 = model["square2"]
    square3 = model["square3"]
    square4 = model["square4"]
    setPieces = model["setPieces"]

    if square["y"]<19 \
            and square2["y"]<19 \
            and square3["y"]<19 \
            and square4["y"]<19 \
            and LookForSpaceUnder(model):
        yincrement(model)
    else:
        setPieces.append(square)
        setPieces.append(square2)
        setPieces.append(square3)
        setPieces.append(square4)
        GeneratePiece(model)
        FilledRowDelete(model)

###########################################################
# normally, you would not need to change anything in main #    
def main(update_interval, canvas_dimensions):
    def keypress(event, model, canvas):
        onkey(model, event.keycode)
        draw(model, canvas)

    def gameloop(X, model, master, canvas):
        master.after(X, gameloop, X, model, master, canvas)
        onloop(model)
        draw(model, canvas)

    model = initialize()
    # initialize your model
    master = Tk()
    # initialize top level widget
    master.wm_title("Tetris™ by Razvan Bouros")
    # name of the generated window
    canvas = Canvas(master, width=canvas_dimensions[0],
                    height=canvas_dimensions[1], background="white")
    # initialize canvas
    canvas.pack()
    master.bind("<Key>", lambda e: keypress(e, model, canvas))

    # bind the keypress() function to a key press event
    # while passing the model and the canvas as arguments too
    gameloop(update_interval, model, master, canvas)
    # start the gameloop
    master.mainloop()
    # enables event handling etc. by tkinter

############################################################
if __name__ == "__main__":
    update_interval = 400
    canvas_dimensions = (245, 485)
    # [ you might want to adjust these settings ]
    main(update_interval, canvas_dimensions)