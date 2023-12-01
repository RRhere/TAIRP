import tkinter as tk
from tkinter import *
from tkinter import messagebox
import threading
import time

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")

        self.score = 0
        self.question_number = 0
        self.questions = [
            {"question": "To prevent a DC return between source and load, it is necessary to use", "options": ["resistor between source and load","inductor between source and load","capacitor between source and load","either (a) or (b)"], "correct_option": 3, "time_limit": 10},
            {"question": "For a base current of 10 μA, what is the value of collector current in common emitter if βdc = 100", "options": ["10 μA","100 μA","1 mA","10 mA"], "correct_option": 1, "time_limit": 10},
            {"question": "Which of the following oscillators is suitable for frequencies in the range of mega hertz?", "options":["RC phase shift","Wien bridge","Hartley","Both (a) and (c)"], "correct_option": 2, "time_limit":10},
            {"question": "The load impedance ZL of a CE amplifier has R and L in series. The phase difference between output and input will be", "options":["180°","0","more than 90° but less than 180°","more than 180° but less than 270°"], "correct_option": 3, "time_limit":10},
            {"question": "If an amplifier with gain of - 1000 and feedback factor β = - 0.1 had a gain change of 20percent due to temperature, the change in gain of the feedback amplifier would be", "options": ["10%","5%","0.2%","0.01%"], "correct_option": 2, "time_limit": 10},
            {"question": "To protect the diodes in a rectifier and capacitor input filter circuit it is necessary to use", "options": ["surge resistor","surge inductor","surge capacitor","both (a) and (b)"], "correct_option": 0, "time_limit": 10},
            {"question": "For a system to work, as oscillator the total phase shift of the loop gain must be equal to", "options": ["90°","45°","270°","360°"], "correct_option": 3, "time_limit": 10},
            {"question": "An amplifier has a large ac input signal. The clipping occurs on both the peaks. The output voltage will be nearly a", "options": ["sine wave","square wave","triangular wave","(a) or (c)"], "correct_option": 1, "time_limit": 10},
            {"question": "Which power amplifier can deliver maximum load power?", "options": ["Class A","Class AB","Class B","Class C"], "correct_option": 3, "time_limit": 10},
            {"question": "A CB amplifier has re = 6 Ω, RL = 600 Ω and a = 0.98. The voltage gain is", "options": ["100","600 x 0.98","98","6"], "correct_option": 2, "time_limit": 10} 
        ]
        
        self.timer_label = tk.Label(root, text="Time left:")
        self.timer_label.pack(pady=10)

        self.question_label = tk.Label(root, text="")
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(btn)
            btn.pack(pady=5)

        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Quiz", command=self.stop_quiz, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.pause_button = tk.Button(root, text="Pause Quiz", command=self.pause_quiz, state=tk.DISABLED)
        self.pause_button.pack(pady=5)

        self.resume_button = tk.Button(root, text="Resume Quiz", command=self.resume_quiz, state=tk.DISABLED)
        self.resume_button.pack(pady=5)

        self.current_timer = None
        self.paused = False
        
        self.default_time_limit = 10

    def start_quiz(self):
        self.score = 0
        self.question_number = 0
        self.update_question()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.NORMAL)
        self.resume_button.config(state=tk.DISABLED)

    def stop_quiz(self):
        self.root.after_cancel(self.current_timer)
        self.show_results()

    def pause_quiz(self):
        self.paused = True
        self.resume_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.root.after_cancel(self.current_timer)

    def resume_quiz(self):
        self.paused = False
        self.resume_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.update_timer()

    def check_answer(self, selected_option):
        if not self.paused:
            correct_option = self.questions[self.question_number]["correct_option"]
            if selected_option == correct_option:
                self.score += 1
            self.question_number += 1

            if self.question_number < len(self.questions):
                self.update_question()
            else:
                self.show_results()

    def update_question(self):
        if not self.paused:
            self.question_label.config(text=self.questions[self.question_number]["question"])

            options = self.questions[self.question_number]["options"]
            for i in range(4):
                self.option_buttons[i].config(text=options[i])

        
            self.questions[self.question_number]["time_limit"] = self.default_time_limit
            self.update_timer()

    def update_timer(self):
        if not self.paused:
            time_limit = self.questions[self.question_number]["time_limit"]
            self.timer_label.config(text=f"Time left: {time_limit}s")

            if time_limit > 0:
                self.current_timer = self.root.after(1000, self.update_timer)
                self.questions[self.question_number]["time_limit"] -= 1
            else:
                self.show_results()

    def show_results(self):
        self.timer_label.config(text="Time's up!")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.DISABLED)
        self.resume_button.config(state=tk.DISABLED)

        result_message = f"You scored {self.score} out of {len(self.questions)}."
        messagebox.showinfo("Quiz Results", result_message)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('990x660+0+0')
    root.title("Quiz App")
    app = QuizApp(root)
    root.mainloop()