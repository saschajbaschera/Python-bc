from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)
        # Question box
        self.canvas = Canvas(width=300, height=250, background="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_box_text = self.canvas.create_text(150, 125, width=280, text="Here is the question placed", font=("Arial", 20, "italic"), fill="black")
        # Score label
        self.score_label = Label(text=f"Score: {self.quiz.score}", font=("Arial", 18), bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        # Correct Button
        correct_button_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_button_image, bg=THEME_COLOR, command=self.is_correct)
        self.correct_button.grid(column=0, row=2)
        # Wrong Button
        wrong_button_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_button_image, command=self.is_wrong, bg=THEME_COLOR)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_box_text, text=question_text)
        else:
            self.canvas.itemconfig(self.question_box_text, text=f"The END, you knew {self.quiz.score} out of"
                                                                f" {self.quiz.question_number} questions ")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def is_correct(self):
        response = self.quiz.check_answer("true")
        self.give_feedback(response)

    def is_wrong(self):
        response = self.quiz.check_answer("false")
        self.give_feedback(response)

    def give_feedback(self, response):
        if response:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)










