# ShutDown App

from tkinter import*
import os

# creating Function - to integrate with os
def restart():
    os.system("shutdown/r/t 1")
def restart_time():
    os.system("shutdown/r/t 20")
def logout():
    os.system("shutdown /l")
def shutdown():
    os.system("shutdown/s/t 20")

st = Tk()   #creating obj ,TK here is class of tkinter
st.title("ShutDown App")  #This is title for the ShutDown App
st.geometry("500x500")  #This is the shape of  webapp
st.config(bg = "Blue")   #This is background Colour

## Buttons -

# Restart -
r_button = Button(st,text="Restart",font=("Time New Roman",30,"bold"),
                  relief=RAISED,cursor="plus",command=restart)    #Restart Button
r_button.place(x=150,y=60,height=50,width=200)   #Placement

# Restart with Time - 
rt_button = Button(st,text="Restart Time",font=("Time New Roman",25,"bold"),
                   relief=RAISED,cursor="plus",command=restart_time)    #Restart Button
rt_button.place(x=150,y=160,height=50,width=200)   

# Log Out -
lg_button = Button(st,text="Log Out",font=("Time New Roman",30,"bold"),
                   relief=RAISED,cursor="plus",command=logout)    #Restart Button
lg_button.place(x=150,y=260,height=50,width=200)

# Shut Down -
st_button = Button(st,text="Shut Down",font=("Time New Roman",30,"bold"),
                   relief=RAISED,cursor="plus",command=shutdown)    #Restart Button
st_button.place(x=150,y=360,height=50,width=200) 

st.mainloop()