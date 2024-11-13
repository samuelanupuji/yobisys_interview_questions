def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error evaluating expression: {e}"

expression = input()
result = evaluate_expression(expression)
print(result)