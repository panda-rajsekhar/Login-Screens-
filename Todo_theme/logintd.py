from tkinter import*
import tkinter
import customtkinter
from tkinter import messagebox
from maininterface import Main_Interface
from PIL import Image,ImageTk

customtkinter.set_appearance_mode("dark")#will set the appearance to dark or light
customtkinter.set_default_color_theme("green")#will set the theme to green

def main():
    win = Tk()
    app = App(win)
    win.mainloop()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #Configure the window
        self.title("DO IT")
        self.geometry(f"{1080}x{720}+0+0")
        self.resizable(0,0)
        #-------------------------Functions 4 buttons------------------------------------
        # for the login button
        def login_button():         
                if self.username.get()==""or self.password.get()=="":
                     messagebox.showerror("Error","All fields are required")
                else:
                     if self.username.get()=="Rajsekhar Panda" and self.password.get()=="mainahibataunga":
                          self.new_window = Toplevel(self)
                          self.app =Main_Interface(self.new_window)
                     else:
                          messagebox.showerror("Error ","Use Correct Id and Password")



        #Adding the image
        self.bg_image = customtkinter.CTkImage(Image.open("leaves-g76a4513a2_1920.png"),size=(1080,720))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        #Making the Frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=15,height= 370,width=400,)
        self.login_frame.place(relx = 0.5,rely = 0.5, anchor = tkinter.CENTER)

        #Adding the LOgo hehe :-)
        self.frm_img = customtkinter.CTkImage(Image.open("text-16814987764671.png"),size=(200,78))
        self.frm_img_label = customtkinter.CTkLabel(self.login_frame,image= self.frm_img,text="")
        self.frm_img_label.place(x = 105,y = 20)

        #Adding the text in the Label
        self.login_label = customtkinter.CTkLabel(self.login_frame,text="Log-In:",font=("Century Gothic",27,"bold"))
        self.login_label.place(x = 155,y= 117) 

        #Taking the entries :
        self.username = customtkinter.CTkEntry(self.login_frame,width = 250,placeholder_text="Username",font=("Century Gothic",25,))
        self.username.place(x = 70,y =180)

        #entryfield for password 
        self.password = customtkinter.CTkEntry(self.login_frame,width = 250,placeholder_text="Password",font=("Century Gothic",25,),show = "•")
        self.password.place(x = 70,y =240)

        #adding the button
        button = customtkinter.CTkButton(self.login_frame,width = 100,text = "LOGIN",corner_radius=6,font=("Century Gothic",25,"bold"),command=login_button)
        button.place(x =150,y =310)







if __name__ == "__main__":
    app = App()
    app.mainloop()