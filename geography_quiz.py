import tkinter as tk
from random import shuffle

class GeographyQuiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Geography Quiz")
        self.questions = self.load_questions()
        self.current_question_index = 0
        self.score = 0
        
        self.question_label = tk.Label(master, text="")
        self.question_label.pack()
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(master, text="", command=lambda i=i: self.check_answer(i))
            button.pack(fill=tk.BOTH, expand=True)
            self.option_buttons.append(button)
        
        self.display_question()
    
    def load_questions(self):
        try:
            with open("questions.txt", "r") as file:
                lines = file.readlines()
                questions = [tuple(lines[i:i+5]) for i in range(0, len(lines), 5)]
                return questions
        except FileNotFoundError:
            print("Error: questions.txt not found!")
            return []
    
    def display_question(self):
        if self.current_question_index < len(self.questions):
            question, *options = self.questions[self.current_question_index]
            self.question_label.config(text=question)
            shuffle(options)
            for button, option in zip(self.option_buttons, options):
                button.config(text=option.strip("+"))
        else:
            self.show_result()
    
    def check_answer(self, index):
        correct_answer = self.questions[self.current_question_index][1].strip("+")
        selected_answer = self.option_buttons[index]["text"]
        if selected_answer == correct_answer:
            self.score += 1
        self.current_question_index += 1
        self.display_question()
    
    def show_result(self):
        result_text = f"Quiz Finished!\nYour Score: {self.score}/{len(self.questions)}"
        result_label = tk.Label(self.master, text=result_text)
        result_label.pack()

def main():
    root = tk.Tk()
    app = GeographyQuiz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
