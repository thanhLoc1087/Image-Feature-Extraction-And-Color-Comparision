import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageTk
import numpy as np

# Function to handle button click to retrieve images
def on_retrieve_images():
    # Get the images created on the canvas
    img1 = get_canvas_image(canvas1, 32, 32)
    img2 = get_canvas_image(canvas2, 32, 32)

    # Display the saved images
    display_image(img1, image_label1)
    display_image(img2, image_label2)

    # Show a success message
    messagebox.showinfo("Success", "Images retrieved successfully!")

# Function to get the content of a canvas as an image
def get_canvas_image(canvas, width, height):
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    cell_width = canvas.winfo_reqwidth() // 32
    cell_height = canvas.winfo_reqheight() // 32

    # Iterate over the cells and copy the content of each cell to the image
    for row in range(32):
        for col in range(32):
            x1, y1 = col * cell_width, row * cell_height
            x2, y2 = x1 + cell_width, y1 + cell_height
            cell_content = canvas.find_enclosed(x1, y1, x2, y2)
            if cell_content:
                color_tag = canvas.gettags(cell_content[0])
                if color_tag and color_tag[0] != "white":
                    draw.rectangle([x1, y1, x2, y2], fill=color_tag[0], outline=color_tag[0])

    return img

# Function to handle mouse movement and drawing on the canvas
def on_canvas_drag(event, canvas):
    cell_width = canvas.winfo_reqwidth() // 32
    cell_height = canvas.winfo_reqheight() // 32

    col = event.x // cell_width
    row = event.y // cell_height

    # Use the current_color directly when drawing on the canvas
    draw_color = current_color.get()
    canvas.create_rectangle(col * cell_width, row * cell_height, (col + 1) * cell_width, (row + 1) * cell_height, fill=draw_color, outline=draw_color)

# Function to display an image on a Label
def display_image(img, label):
    img = img.resize((100, 100), Image.BILINEAR)
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img

# Set up the main window
root = tk.Tk()
root.title("Image Drawing Demo")

# Function to handle color selection
def on_color_change(color):
    current_color.set(color)

# Create and pack widgets
canvas1 = tk.Canvas(root, width=280, height=280, bg="white")
canvas1.pack(side=tk.LEFT, padx=10)
canvas1.bind("<B1-Motion>", lambda event: on_canvas_drag(event, canvas1))

canvas2 = tk.Canvas(root, width=280, height=280, bg="white")
canvas2.pack(side=tk.RIGHT, padx=10)
canvas2.bind("<B1-Motion>", lambda event: on_canvas_drag(event, canvas2))

color_frame = tk.Frame(root)
color_frame.pack()

colors = ["black", "red", "green", "blue"]
current_color = tk.StringVar()
current_color.set(colors[0])

for color in colors:
    color_button = tk.Button(color_frame, bg=color, width=2, height=1, command=lambda c=color: on_color_change(c))
    color_button.pack(side=tk.LEFT, padx=5)

retrieve_button = tk.Button(root, text="Retrieve Images", command=on_retrieve_images)
retrieve_button.pack(pady=10)

image_label1 = tk.Label(root)
image_label1.pack(side=tk.LEFT, padx=10)

image_label2 = tk.Label(root)
image_label2.pack(side=tk.RIGHT, padx=10)

# Run the main loop
root.mainloop()
