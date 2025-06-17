HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("No history available.")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(HISTORY_FILE, "w")
    file.close()
    print("History cleared.")


def save_to_history(expression, result):
    file =  open(HISTORY_FILE, "a")
    file.write(expression +"= "+ str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split() #Split the input into parts
    if len(parts) != 3:
        print("Invalid input. Please enter in the format: number operator number (eg. 5 + 3)")
        return
    
    num1 = float(parts[0])  # Convert the first part to a float
    operator = parts[1]     # The operator is the second part
    num2 = float(parts[2])  # Convert the third part to a float

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return

    if int(result) == result:
        result = int(result)
    print(f"The result of {user_input} is: {result}")
    save_to_history(user_input, result)    

    #brain

def main():
    print("Welcome to the Calculator with History!")
    print("Type 'history' to view calculation history or 'clear' to clear history.")
    while True:
        user_input = input("Enter your calculation ( +, -, *, /)or command (history, clear or exit): ").strip()
        if user_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        elif user_input.lower() == 'history':
            show_history()
        elif user_input.lower() == 'clear':
            clear_history()
        else:
            calculate(user_input)

main()


    


