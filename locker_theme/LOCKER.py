from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()
class Login_Window:#widget for login window
    print("Authenticcation Stage 1 Working")
    def __init__(self,root):
        self.root=root
        self.root.title("ADMIN AUTHENTICATION")
        self.root.geometry("1080x720")
        self.root.resizable(False, False)



        # tricking by making the frame as of te same size of the window hehe ;-)
        frame = Frame(self.root,bg="black")
        frame.place(x=0,y=0,width=1080,height=720)
        # heading
        Usr_lin= Label(frame,text="AUTHENTICATION REQUIRED TO PROCEED",font=(" century gothic",25),fg="aqua",bg="black")
        Usr_lin.place(x=180,y=280)

        #Adding the logo
        img1 = Image.open(r"text-1681277975948.png")# r is to read
        img1 = img1.resize((1000,200))
        """#Anti-aliasing is the smoothing of jagged edges in digital images by averaging the colors of the pixels at a boundary"""
        self.photoimage =ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage,bg="White",borderwidth=0)
        lblimg1.place(x =55,y=30,width=1000,height=200)

        #taking the input
        #for admin id
        username =  lbl= Label(frame,text="ADMIN ID:",font=("century gothic",20),fg="aqua",bg="black")
        username.place(x = 220,y = 350)
        self.adid = Entry(frame,width = 25,fg ="aqua",border = 0,bg = "black",font=(" century gothic",25))
        self.adid.place(x = 400,y  = 350)      
        Frame(frame,width = 452,height = 3,bg="aqua").place(x = 400,y =390)
        
        # for admin password 
        password =  lbl= Label(frame,text="PASSWORD:",font=("century gothic",20),fg="aqua",bg="black")
        password.place(x = 220,y = 450)
        self.adps = Entry(frame,width = 25,fg ="aqua",border = 0,bg = "black",font=(" century gothic",25),show = "♣")
        self.adps.place(x = 400,y  = 450)      
        Frame(frame,width = 452,height = 3,bg="aqua").place(x = 400,y =490)

        print("Authenticcation Stage 2 Working")
        #adding the login button
        loginbtn = Button(frame,command=self.login,text="LOGIN",font=("century gothic",16,"bold"),bd=0,relief= RIDGE,fg="black",bg="aqua")
        loginbtn.place(x=435,y=560,width=220,height=50)

        #defining the function for login button
    def login(self):
        if self.adid.get()=="" or self.adps.get()=="":
            messagebox.showerror("Error","All fields are required")    
       
# continue the code from here and make whatever you desire




if __name__=="__main__":
    main() 
