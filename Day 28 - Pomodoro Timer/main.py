from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# I know this program is not optimized and might be buggy.
# But I don't want to copy and paste the solution to preserve my original efforts.

window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

check_mark_label = Label(text="✅", fg=GREEN, bg=YELLOW)
check_mark_label.config(pady=30, bg=YELLOW)
check_mark_label.grid(row=2, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

round_count = 1


def reset_window():
    canvas.itemconfig(text, text="00:00")
    check_mark_label.config(text="✅", fg=GREEN, bg=YELLOW)
    global round_count
    round_count = 1


def timer_func():
    for minute in range(24, -1, -1):
        for second in range(59, -1, -1):
            if second < 10 and minute < 10:
                canvas.itemconfig(text, text=f"0{minute}:0{second}")
            elif second < 10:
                canvas.itemconfig(text, text=f"{minute}:0{second}")
            elif minute < 10:
                canvas.itemconfig(text, text=f"0{minute}:{second}")
            else:
                canvas.itemconfig(text, text=f"{minute}:{second}")
            window.update()
            window.after(1000)


def short_break_time():
    for minute in range(4, -1, -1):
        for second in range(59, -1, -1):
            if second < 10 and minute < 10:
                canvas.itemconfig(text, text=f"0{minute}:0{second}")
            elif second < 10:
                canvas.itemconfig(text, text=f"{minute}:0{second}")
            elif minute < 10:
                canvas.itemconfig(text, text=f"0{minute}:{second}")
            else:
                canvas.itemconfig(text, text=f"{minute}:{second}")
            window.update()
            window.after(1000)


def long_break_time():
    for minute in range(14, -1, -1):
        for second in range(59, -1, -1):
            if second < 10 and minute < 10:
                canvas.itemconfig(text, text=f"0{minute}:0{second}")
            elif second < 10:
                canvas.itemconfig(text, text=f"{minute}:0{second}")
            elif minute < 10:
                canvas.itemconfig(text, text=f"0{minute}:{second}")
            else:
                canvas.itemconfig(text, text=f"{minute}:{second}")
            window.update()
            window.after(1000)


def start():
    global round_count
    for _ in range(4):
        timer_func()
        check_mark_label.config(text="✅" * round_count, fg=GREEN, bg=YELLOW)
        round_count += 1
        short_break_time()
    long_break_time()
    reset_window()


start_button = Button(text="Start", command=start)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_window)
reset_button.grid(row=2, column=2)

window.mainloop()
