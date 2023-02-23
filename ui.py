from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizzlet")

        self.canvas = Canvas()
        self.canvas.config(height=250, width=300, bg="white", highlightthickness=0)
        self.quiz_text = self.canvas.create_text(150, 125, text="Amazon text", font=("Arial", 20, "italic"), fill="black", width=280)
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)

        self.label = Label(text="Score: 0", bg=THEME_COLOR, padx=20)
        self.label.grid(column=1, row=0)

        tick_image = PhotoImage(file="images/true.png")
        self.tick = Button(image=tick_image, highlightthickness=0, command=self.right)
        self.tick.grid(column=0, row=2)

        cross_image = PhotoImage(file="images/false.png")
        self.wrong = Button(image=cross_image, highlightthickness=0, command=self.wrong)
        self.wrong.grid(column=1, row=2)

        self.get_next_qn()

        self.window.mainloop()

    def get_next_qn(self):
        text = self.quiz.next_question()

        if text == False:
            self.window.destroy()
        else:
            score = self.quiz.score
            self.canvas.itemconfig(self.quiz_text, text=text)
            self.label.config(text=f"Score:{score}")
            self.canvas.config(bg="white")

    def right(self):
        is_right = self.quiz.check_answer(True)
        self.give_feedback(is_right)

    def wrong(self):
        is_right = self.quiz.check_answer(False)
        self.give_feedback(is_right)

    def give_feedback(self, check):

        if check == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_qn)



