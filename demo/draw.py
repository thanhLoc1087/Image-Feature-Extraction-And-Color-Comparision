# Drawing Application Using Python

#importing all the necessary Libraries

from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser,filedialog,messagebox
from tkinter import messagebox
import PIL.ImageGrab as ImageGrab
from PIL import Image


#Defining Class and constructor of the Program
class Draw():
    def __init__(self,root):

#Defining title and Size of the Tkinter Window GUI
        self.root =root
        self.root.title("Copy Assignment Painter")
        self.root.geometry("810x530")
        self.root.configure(background="white")
#         self.root.resizable(0,0)
 
#variables for pointer and Eraser   
        self.pointer= "black"
        self.erase="white"

#Widgets for Tkinter Window
    
# Configure the alignment , font size and color of the text
        text=Text(root)
        text.tag_configure("tag_name", justify='center', font=('arial',25),background='#292826',foreground='orange')

# Insert a Text
        text.insert("1.0", "Drawing Application in Python")

# Add the tag for following given text
        text.tag_add("tag_name", "1.0", "end")
        text.pack()
        
# Pick a color for drawing from color pannel
        self.pick_color = LabelFrame(self.root,text='Colors',font =('arial',15),bd=5,relief=RIDGE,bg="white")
        self.pick_color.place(x=0,y=40,width=90,height=185)

        colors = ['blue','red','green', 'orange','violet','black','yellow','purple','pink','gold','brown','indigo']
        i=j=0
        for color in colors:
            Button(self.pick_color,bg=color,bd=2,relief=RIDGE,width=3,command=lambda col=color:self.select_color(col)).grid(row=i,column=j)
            i+=1
            if i==6:
                i=0
                j=1

 # Erase Button and its properties   
        self.pointer_color_btn = Button(self.root, text="PointerColor", bd=4, bg='white', command=self.choose_pointer_color, width=9, relief=RIDGE)
        self.pointer_color_btn.place(x=0, y=197)

# Reset Button to clear the entire screen 
        self.clear_screen= Button(self.root,text="Clear Screen",bd=4,bg='white',command= lambda : self.background.delete('all'),width=9,relief=RIDGE)
        self.clear_screen.place(x=0,y=227)

# Save Button for saving the image in local computer
        self.save_btn= Button(self.root,text="Save",bd=4,bg='white',command=self.save_drawing,width=9,relief=RIDGE)
        self.save_btn.place(x=0,y=257)

# Background Button for choosing color of the Canvas
        self.bg_btn= Button(self.root,text="Background",bd=4,bg='white',command=self.canvas_color,width=9,relief=RIDGE)
        self.bg_btn.place(x=0,y=287)


#Creating a Scale for pointer and eraser size
        self.pointer_frame= LabelFrame(self.root,text='size',bd=5,bg='white',font=('arial',15,'bold'),relief=RIDGE)
        self.pointer_frame.place(x=0,y=320,height=200,width=70)

        self.pointer_size =Scale(self.pointer_frame,orient=VERTICAL,from_ =48 , to =0, length=168)
        self.pointer_size.set(1)
        self.pointer_size.grid(row=0,column=1,padx=15)


#Defining a background color for the Canvas 
        self.background = Canvas(self.root,bg='white',bd=5,relief=GROOVE,height=470,width=680)
        self.background.place(x=80,y=40)


#Bind the background Canvas with mouse click
        self.background.bind("<B1-Motion>",self.paint) 


# Functions are defined here

# Paint Function for Drawing the lines on Canvas
    def paint(self,event):       
        x1,y1 = (event.x-2), (event.y-2)  
        x2,y2 = (event.x+2), (event.y+2)  

        self.background.create_oval(x1,y1,x2,y2,fill=self.pointer,outline=self.pointer,width=self.pointer_size.get())

# Function for choosing the color of pointer  
    def select_color(self, col):
        self.pointer = col

# Function for defining the eraser
    def choose_pointer_color(self):
        color = colorchooser.askcolor(title="Choose Pointer Color")
        if color[1]:
            self.pointer = color[1]

# Function for choosing the background color of the Canvas    
    def canvas_color(self):
        color=colorchooser.askcolor()
        self.background.configure(background=color[1])
        self.erase= color[1]

# Function for saving the image file in Local Computer
    from PIL import Image

    def save_drawing(self):
        try:
            file_ss = filedialog.asksaveasfilename(defaultextension='jpg')
            print(file_ss)

            # Lấy tọa độ và kích thước của khung vẽ
            x = self.background.winfo_x()
            y = self.background.winfo_y()
            width = self.background.winfo_width()
            height = self.background.winfo_height()

            # Tính toán tọa độ của khung vẽ trong cửa sổ gốc
            root_x = self.root.winfo_rootx()
            root_y = self.root.winfo_rooty()
            x += root_x
            y += root_y

            # Điều chỉnh tọa độ để bỏ đi một phần bên trái và bên trên
            adjustment_x = 30  # Số pixel bên trái cần bỏ đi
            adjustment_y = 30  # Số pixel bên trên cần bỏ đi
            x += adjustment_x
            y += adjustment_y
            width -= adjustment_x
            height -= adjustment_y

            x1 = x + width
            y1 = y + height
            print(x, y, x1, y1)

            ImageGrab.grab().crop((x, y, x1, y1)).save(file_ss)

            messagebox.showinfo('Screenshot Successfully Saved as', str(file_ss))

            # Configure the message box to set the foreground color to black

            # Đường dẫn tới tập tin ảnh
            file_path = file_ss

            # Đọc ảnh từ tập tin
            image = Image.open(file_path)

            # Thay đổi kích thước ảnh thành 28x28 pixel
            resized_image = image.resize((28, 28))

            # Lưu ảnh đã thay đổi kích thước
            resized_image.save(file_ss)

        except Exception as e:
            print("Error in saving the screenshot:", str(e))

if __name__ =="__main__":
    root = Tk()
    p= Draw(root)
    root.mainloop()