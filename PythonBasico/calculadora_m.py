import math


def calculator(operador, num_1, num_2):
    match operador:
        case "+":
            return num_1 + num_2
        case "-":
            return num_1 - num_2
        case "/":
            return num_1 / num_2
        case "*":
            return num_1 * num_2
        case "r":
            return f"A raiz de {num_1} é {math.sqrt(num_1):.2f} e de {num_2} é {math.sqrt(num_2):.2f}"
        case default:
            return "Operador não digitado"
