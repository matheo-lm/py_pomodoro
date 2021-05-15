from tkinter import *
import pygame
import math
#TODO: pop up or end after 4 long breaks
#TODO: sound at start, sound at short break, sound at long break, sound at reset
#TODO: Make round buttons
#TODO: packagae app v1 to standalone binary once the above is completed
#TODO: share with a few users for feedback

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GRAY = "#464646"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "Pomodoro Timer", fg=GRAY)
    check_label.config(text = " ")
    global reps
    reps = 0
    button_start.config(command=start_timer)


# ---------------------------- Sounds ------------------------------- #

pygame.mixer.init()
def play_start():
    pygame.mixer.music.load("")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    button_start.config(command="Error")

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="  Long Break  ", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="  Short Break ", fg=PINK)


    else:
        count_down(work_sec)
        title_label.config(text="   Work Time  ", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = " "
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Time Management Technique")
window.config(padx=40, pady=20, bg=YELLOW)

title_label = Label(text="Pomodoro Timer")
title_label.config(fg=GRAY, bg=YELLOW, padx=10, pady=20, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=2, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

button_start = Button(text="Start", command=start_timer,
                      highlightthickness=0, padx=10, pady=20,
                      font=(FONT_NAME, 20, "bold"))
button_start.grid(column=1, row=3)

button_stop = Button(text="Reset", command=reset_timer,
                     highlightthickness=0, padx=10, pady=20,
                     font=(FONT_NAME, 20, "bold"))
button_stop.grid(column=3, row=3)


check_label = Label()
check_label.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
check_label.grid(column=2, row=4)

window.resizable(False, False)
window.mainloop()