from tkinter import *
import customtkinter
import string
import random as rd
import pyperclip
from tkinter import messagebox,filedialog
customtkinter.set_appearance_mode("dark")
def generate_button_event():
    pass_display.delete(0,END)
    small=string.ascii_lowercase
    capital=string.ascii_uppercase
    numbers=string.digits
    special=string.punctuation
    allp=small+capital+numbers+special
    pass_len=lenbox.get()
    if pass_len == "Password Length" or pass_len in small or pass_len in capital or pass_len in special  :
        messagebox.showerror("Error","Please input a valid number for password length")    
    if choice.get()==1 :
        pass_display.insert(0,rd.sample(small+numbers,int(pass_len)))
    elif choice.get()==2 :
        pass_display.insert(0,rd.sample(small+numbers+special,int(pass_len)))
    elif choice.get()==3 :    
        pass_display.insert(0,rd.sample(allp,int(pass_len)))
    else :
        messagebox.showwarning("Warning","Please select the kind of paasword")
def copy_button_event():
    copied_pass=pass_display.get()
    pyperclip.copy(copied_pass)
root=customtkinter.CTk()
root.geometry("300x340")
root.resizable(False,False)
root.title("Password Generator")
choice=IntVar()
label1 = customtkinter.CTkLabel(master=root, text="Password Generator",font=('times new roman',23,'bold'),justify="center")
label1.place(relx=0.5,rely=0.05, anchor=CENTER)
weakradio = customtkinter.CTkRadioButton(master=root, text="Weak",value=1,variable=choice,font=('times new roman',20,'bold'),hover_color="Blue")
mediumradio = customtkinter.CTkRadioButton(master=root, text="Medium",value=2,variable=choice,font=('times new roman',20,'bold'),hover_color="Blue")
strongradio = customtkinter.CTkRadioButton(master=root, text="Strong",value=3,variable=choice,font=('times new roman',20,'bold'),hover_color="Blue")
weakradio.place(relx=0.5,rely=0.15,anchor=CENTER)
mediumradio.place(relx=0.5,rely=0.25,anchor=CENTER)
strongradio.place(relx=0.5,rely=0.35,anchor=CENTER)
lenbox_var = StringVar(value="Password Length")
lenbox = customtkinter.CTkComboBox(master=root,values=["5","6","7","8","9","10"],variable=lenbox_var,font=('times new roman',20,'bold'),width=190,button_hover_color="Blue",dropdown_hover_color="Blue",dropdown_font=('times new roman',20,'bold'))
lenbox.place(relx=0.23,rely=0.43)    
button = customtkinter.CTkButton(master=root,width=120,height=32,hover=True,hover_color="Blue",fg_color="transparent",border_width=1.5,corner_radius=8,text="Generate",font=('times new roman',20,'bold'),command=generate_button_event)
button.place(relx=0.52, rely=0.6, anchor=CENTER)
pass_display = customtkinter.CTkEntry(master=root,width=220,border_width=2,corner_radius=10,font=('times new roman',20,'bold'))
pass_display.place(relx=0.5, rely=0.73, anchor=CENTER)
button = customtkinter.CTkButton(master=root,width=120,height=32,text_color=("gray10", "#DCE4EE"),hover=True,hover_color="Blue",fg_color="transparent",border_width=1.5,corner_radius=8,text="Copy",font=('times new roman',20,'bold'),command=copy_button_event)
button.place(relx=0.52, rely=0.86, anchor=CENTER)
root.mainloop()
