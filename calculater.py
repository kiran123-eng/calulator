 #calcutater to do all calculation
import tkinter as tk
import math

# Functions for calculator operations
sum = lambda a,b: a+b
subtract = lambda a,b: a-b
multiply = lambda a,b: a*b
square = lambda c: c*c
square_root = lambda a: math.sqrt(a)
division = lambda a,b: a/b if b!=0 else "Division by zero is invalid"

# Main application window
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")

        self.expression = ""

        # Entry widget to display the expression
        self.entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4)

        # Button layout for the calculator
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('**', 5, 0), ('sqrt', 5, 1), ('^2', 5, 2), ('exit', 5, 3)
        ]

        # Creating buttons and placing them in the grid
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 16),
                               command=lambda text=text: self.on_button_click(text))
            button.grid(row=row, column=col)

    # Function to handle button clicks
    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                result = eval(self.expression)
                self.expression = str(result)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, self.expression)
            except Exception as e:
                self.expression = "Error"
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, self.expression)
        elif char == 'exit':
            self.root.quit()
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
