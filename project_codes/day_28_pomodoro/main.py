import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# ---------------------------- GLOBALS ------------------------------- #
reps = 0
check = ""
clock = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_clicked():
    """stops and resets the timer"""
    global reps, check

    window.after_cancel(clock)
    reps = 0
    check = ""
    check_mark.config(text=check)
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(count_number, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_clicked():
    """starts the timer everytime the start button is click"""
    global reps, check
    reps += 1

    work_time = math.floor(WORK_MIN * 60)
    short_break = math.floor(SHORT_BREAK_MIN * 60)
    long_break = math.floor(LONG_BREAK_MIN * 60)
    if reps % 8 == 0:
        timer_count(long_break)
        timer.config(text="Long Break", fg=RED)
        check += "✓"
        check_mark.config(text=check)
    elif reps % 2 == 0:
        timer_count(short_break)
        timer.config(text="Short Break", fg=PINK)
        check += "✓"
        check_mark.config(text=check)
    else:
        timer_count(work_time)
        timer.config(text="Work Time", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def timer_count(count):
    """displays the current count in the screen"""
    global clock
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif len(str(count_sec)) < 2:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(count_number, text=f"{count_min}:{count_sec}")
    if count > 0:
        clock = window.after(1000, timer_count, count-1)
    else:
        start_clicked()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# import image
tomato_pic = tkinter.PhotoImage(file="tomato.png")
# create a canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_pic)
count_number = canvas.create_text(100, 133, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# create a label
timer = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer.grid(row=0, column=1)

check_mark = tkinter.Label(text=check, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
check_mark.grid(row=3, column=1)
# create a button
start_button = tkinter.Button(text="Start", command=start_clicked)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", command=reset_clicked)
reset_button.grid(row=2, column=2)

window.mainloop()
