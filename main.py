from tkinter import *
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
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    print("Resetting...")
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_seconds = 10
    short_break_seconds = 5
    long_break_seconds = 20

    if reps == 8:
        timer_label.config(text="¡A descansar!", fg=RED)
        countdown(long_break_seconds)
    elif reps % 2 == 0:
        timer_label.config(text="¡A descansar!", fg=PINK)
        countdown(short_break_seconds)
    else:
        timer_label.config(text="¡A trabajar!", fg=GREEN)
        countdown(work_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = "0" + str(count_seconds)

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmarks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Display the Timer title label
timer_label = Label(window, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=2, row=0)

# Display tomato.png onto the canvas in tkinter
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# Display the timer text
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Display Start & Reset button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

# Display pomodoro checkmark
checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14))
checkmarks.grid(column=2, row=4)


window.mainloop()