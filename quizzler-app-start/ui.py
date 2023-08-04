from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(padx=20, pady=20, background=THEME_COLOR)
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", background=THEME_COLOR, foreground='white',
                                 font=("Arial", 10, "bold"))
        # self.score_label.configure(pady=20, padx=20)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 120, width=280, text="question", font=("Arial", 20, "italic")
                                                     , fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.correct_photo = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=self.correct_photo, highlightthickness=0, command=self.correct_clicked)
        self.correct_button.grid(column=0, row=2)

        self.wrong_photo = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_photo, highlightthickness=0, command=self.wrong_clicked)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(background="white")
        if self.quiz.still_has_questions():
            self.score_label.configure(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz. Your final score was:"
                                                            f" {self.quiz.score}/{self.quiz.question_number}")
            self.correct_button.configure(state="disabled")
            self.wrong_button.configure(state="disabled")

    def correct_clicked(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_clicked(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(background="green")
        else:
            self.canvas.configure(background="red")
        self.window.after(1000, self.get_next_question)
