def add(n1,n2):
    """Add two numbers"""
    return n1 + n2

def subtract(n1,n2):
    """Subtract two numbers"""    
    return n1 - n2

def multiply(n1,n2):
    """Multiply two numbers"""    
    return n1 * n2

def divide(n1,n2):
    """Divide two numbers"""    
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}    

num1 = float(input("What is the first number?: "))
num2 = float(input("What is the second number?: "))

def calc_function():
    is_finished = True
    while is_finished:
        for operator in operations:
            print(operator)
            operator_symbol = input("Pick an operator symbol from the line above: ")
            calc_function = operations[operator_symbol]
            answer = calc_function(num1, num2)
            do_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit")
            if do_continue == "y":
                answer = (calc_function(answer, num2))
            elif do_continue == "n":
                is_finished = False
            else: 
                print("You must enter 'y' or 'n")
                calc_function()
                is_finished = False    
    print(f"{num1} {operator_symbol} {num2} = {answer}")
    print(do_continue)

calc_function()    
