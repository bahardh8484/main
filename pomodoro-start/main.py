from  tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(tomato_text,text = "00:00")
    check_mark["text"] = ""
    timer["text"] = "Timer"
    global rep
    rep = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
#count = 5
rep = 0
def start_command():
    global rep
    rep+=1

    if rep%2 != 0:
          timer.config(text = "Work",fg = GREEN)
          count_down(WORK_MIN)
    elif rep == 8 :
        timer.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN)
    elif rep%2 == 0 :
        timer.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN)

## ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    remainder = (count%60)
    if  count%60 == 0:
        remainder = "00"
    elif len(str(remainder))<2:
        remainder = f"0{count%60}"

    canvas.itemconfig(tomato_text,text = f"{int(count/60)}:{remainder}")
    if count >0:
        global TIMER
        TIMER =  window.after(1000,count_down,count - 1)
    else:
        if rep%2!=0:
            check_mark["text"]+="✔"
        start_command()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pamadoro")
window.config(padx=100,pady=50,bg = YELLOW)
canvas = Canvas(width = 200 , height = 224,bg= YELLOW,highlightthickness=0)
tomato = PhotoImage(file = "tomato.png")
canvas.create_image(100,112,image = tomato)
tomato_text = canvas.create_text(100,130,text = "00:00",fill = "white", font = (FONT_NAME,35,"bold"))
canvas.grid(column = 1,row=1)
timer = Label(text = "Timer",fg = GREEN,bg = YELLOW , font = (FONT_NAME,35,"bold"))
timer.grid(column = 1,row = 0)
check_mark = Label(bg = YELLOW,fg = GREEN,font = (FONT_NAME,10,"bold"))
check_mark.grid(column = 1,row = 3)
check_mark.config(pady = 20)

start_buttom = Button(text="start",command=start_command,fg = "black",bg = "white",font = (FONT_NAME,10,"bold"))
start_buttom.grid(column = 0,row = 2)
restart_buttom = Button(text="restart",fg = "black",bg = "white",font = (FONT_NAME,10,"bold"),command = reset_timer)
restart_buttom.grid(column = 2,row = 2)






window.mainloop()










