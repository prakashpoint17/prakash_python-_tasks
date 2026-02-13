#calculator using expressions

def evaluate_expression(expression: str) -> float:
    try:
        result = eval(expression)
        print(f"The result is: {result}")
    
    except Exception as e:
        print(f"Error Evaluating expression : {e}")
    
expression = input("Enter an expression (e.g., 2 + 3): ")
evaluate_expression(expression)