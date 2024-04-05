import tkinter as tk
from PIL import Image, ImageTk

def on_enter(event):
    # Adjust the opacity when the mouse enters the button
    button.config(image=hover_image)

def on_leave(event):
    # Restore the original opacity when the mouse leaves the button
    button.config(image=normal_image)

root = tk.Tk()

# Load the image using Pillow
pil_image = Image.open("images/Acorde.jpg")

# Create an image with reduced opacity (50% transparent)
transparent_pil_image = pil_image.copy()
transparent_pil_image.putalpha(128)  # 128 is 50% transparency

# Convert the PIL Image to a Tkinter-compatible PhotoImage
normal_image = ImageTk.PhotoImage(transparent_pil_image)
hover_image = ImageTk.PhotoImage(pil_image)

# Create a button with the normal image as its background
button = tk.Button(root, image=normal_image, borderwidth=0)

# Bind mouse enter and leave events to change opacity
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

# Pack the button into the main window
button.pack()

root.mainloop()
