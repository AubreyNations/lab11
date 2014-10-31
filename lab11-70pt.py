##########################################
#                                        #
#    2nd Example of animation w/ Canvas  #
#                                        #
##########################################

# Detect if we have hit a boundary

from Tkinter import *
root = Tk()
# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='#7CE7F7')
drawpad.grid(row=0, column=0)

# Create the oval
circle = drawpad.create_oval(10, 10, 100, 100, fill='purple')
direction = 1
# Create our animation function
def animate():
    global direction
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(circle)
    if x2 > drawpad.winfo_width(): 
        direction = - 5
    elif x1 < 0:
        direction = 5
    #Move our oval object by the value of direction
    drawpad.move(circle,direction,0)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(1, animate)

# Kick off our animation
animate()
root.mainloop()