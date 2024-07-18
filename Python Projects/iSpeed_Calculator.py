# Internet speed meter

from tkinter import*
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()  #Initialisation(for all remain same)
    sp.get_servers()
    down =str(round(sp.download()/(10**6))) +"Mbps"    #to convert speed to mbps
    up = str(round(sp.download()/(10**6))) +"Mbps"
    lab_Down.config(text=down)
    lab_Up.config(text=up)


#def on_button_click(event):
#    print("Button clicked!")

sp = Tk()
sp.title("Internet Speed Meter")    # Name
sp.geometry("500x700") #Dimension
sp.config(bg = "Black")

lab = Label(sp,text="i-Speed",font=("ROG Fonts",40,"bold"),fg="Grey")
lab.place(x=50,y=80,height=50,width=300)

lab_Down = Label(sp,text="Download Speed",font=("STXinwei",30,"bold"),fg="Red")
lab_Down.place(x=20,y=200,height=50,width=350)

lab_Down = Label(sp,text="00",font=("STXinwei",30,"bold"),fg="Red")
lab_Down.place(x=20,y=260,height=40,width=350)

lab_Up = Label(sp,text="Upload Speed",font=("STXinwei",30,"bold"),fg="Green")
lab_Up.place(x=20,y=320,height=50,width=350)

lab_Up = Label(sp,text="00",font=("STXinwei",30,"bold"),fg="Green")
lab_Up.place(x=20,y=380,height=40,width=350)

#Button - 
#canvas = Canvas(sp,bg= "Black", bd=1,highlightthickness=0, relief=RAISED )
#canvas.place(x=100, y=450)
#circle = canvas.create_oval(20, 20, 110, 110, fill='White')
#text = canvas.create_text(50,50,text ="GO",fill="Green")
#canvas.tag_bind(circle, '<ButtonPress-1>', on_button_click)

button = Button(sp,text="GO",font=("Time New Roman", 30, "bold"), relief=RAISED,command=speedcheck)
button.place(x=20,y=440,height=50,width=350)

sp.mainloop()   #It will provide a window
