# split operands and operator
x, y, z = input("Expression: ").split()

match y:
    case "+":
        print(f"{(int(x) + int(z)):.1f}")
    case "-":
        print(f"{(int(x) - int(z)):.1f}")
    case "*":
        print(f"{(int(x) * int(z)):.1f}")
    case "/":
        print(f"{(int(x) / int(z)):.1f}")
