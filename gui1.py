from tkinter import *
from my_functions import *

class Gui:
    def __init__(self, window) -> None:
        self.window = window

        """Number input frame"""
        self.frame_input = Frame(self.window)
        self.label_input = Label(self.frame_input, text='Enter Numbers (e.g., 1, 2, 3):', font=('Palatino', 12, 'bold'))
        self.entry_input = Entry(self.frame_input, width=40)
        self.label_input.pack(pady=5)
        self.entry_input.pack(pady=5, padx=20, fill='x')
        self.frame_input.pack(anchor='center', pady=10)

        """Select operation buttons"""
        self.frame_operations = Frame(self.window)
        self.label_operations = Label(self.frame_operations, text='Select an Operation:', font=('Palatino', 12, 'bold'))
        self.num_operation = IntVar()
        self.num_operation.set(0)

        self.radio_add = Radiobutton(self.frame_operations, text='Add', variable=self.num_operation, value=1, font=('Palatino', 12), command=self.update_info)
        self.radio_subtract = Radiobutton(self.frame_operations, text='Subtract', variable=self.num_operation, value=2, font=('Palatino', 12), command=self.update_info)
        self.radio_multiply = Radiobutton(self.frame_operations, text='Multiply', variable=self.num_operation, value=3, font=('Palatino', 12), command=self.update_info)
        self.radio_divide = Radiobutton(self.frame_operations, text='Divide', variable=self.num_operation, value=4, font=('Palatino', 12), command=self.update_info)
        self.radio_choose = Radiobutton(self.frame_operations, text='Choose', variable=self.num_operation, value=5, font=('Palatino', 12), command=self.update_info)

        self.label_operations.pack(pady=5)
        self.radio_add.pack(anchor='w', padx=20)
        self.radio_subtract.pack(anchor='w', padx=20)
        self.radio_multiply.pack(anchor='w', padx=20)
        self.radio_divide.pack(anchor='w', padx=20)
        self.radio_choose.pack(anchor='w', padx=20)
        self.frame_operations.pack(anchor='w', pady=10)

        """Operation info/description frame"""
        self.frame_info = Frame(self.window)
        self.label_info = Label(self.frame_info, text='Select an operation to see more details', font=('Palatino', 10), fg='blue')
        self.label_info.pack(pady=5)
        self.frame_info.pack(anchor='w', padx=20)

        """Answer frame"""
        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result, font=('Palatino', 12, 'bold'))
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        """Calculate and clear button frame"""
        self.frame_buttons = Frame(self.window)
        self.calc_button = Button(self.frame_buttons, text='Calculate', command=self.calculate, font=('Palatino', 12))
        self.clear_button = Button(self.frame_buttons, text='Clear', command=self.clear, font=('Palatino', 12))
        self.calc_button.pack(side='left', padx=10, pady=10)
        self.clear_button.pack(side='left', padx=10, pady=10)
        self.frame_buttons.pack()
        
    def update_info(self) -> None:
        """Operation description key/value pairs"""
        operation = self.num_operation.get()
        op_description = {
            1: "Add: Adds all negative numbers together",
            2: "Subtract: Subtracts each number from each other, starting with the first number",
            3: "Multiply: Multiplies all numbers together",
            4: "Divide: Divides each number from each other; Cannot divide by zero",
            5: "Choose: Chooses a random number from the list"
        }
        self.label_info.config(text=op_description.get(operation, "Choose an operation for more details"))

    def calculate(self) -> None:
        try:
            """Separating and turning input into floats"""
            numbers = [float(x.strip()) for x in self.entry_input.get().split(',') if x.strip()]
            if len(numbers) < 2:
                raise ValueError("Please provide at least two numbers.")

            """Getting the operation and calling the function from my_functions"""
            operation = self.num_operation.get()
            if operation == 0:
                raise ValueError("Please select an operation.")

            if operation == 1:
                result = add(numbers)
            elif operation == 2:
                result = subtract(numbers)
            elif operation == 3:
                result = multiply(numbers)
            elif operation == 4:
                result = divide(numbers)
            elif operation == 5:
                result = choose(numbers)

            """Displays the result"""
            self.label_result.config(text=f"Answer = {result:.2f}", fg='green')
        except ZeroDivisionError:
            self.label_result.config(text="Cannot divide by zero.", fg='red')
        except ValueError:
            self.label_result.config(text="Invalid input: Please enter at least two numbers", fg='red')



    def clear(self) -> None:
        """Clearing entry numbers and operations"""
        self.entry_input.delete(0, END)
        self.num_operation.set(0)
        self.label_result.config(text='')
        self.label_info.config(text='Choose an operation to see more details')

if __name__ == '__main__':
    root = Tk()
    root.title('Operation Calculator')
    root.geometry('500x400')
    Gui(root)
    root.mainloop()