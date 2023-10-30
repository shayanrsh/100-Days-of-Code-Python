from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.create_score()
        self.create_box()
        self.create_buttons()

        self.get_next_question()

        self.window.mainloop()

    def create_score(self):
        self.score = Label(text="score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

    def create_box(self):
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="test",
                                                     width=280,
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

    def create_buttons(self):
        self.correct_button_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=self.correct_button_image, highlightthickness=0, command=self.true_pressed)
        self.correct_button.grid(row=2, column=0)

        self.wrong_button_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_button_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=" You've reached the end of the quiz.")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

