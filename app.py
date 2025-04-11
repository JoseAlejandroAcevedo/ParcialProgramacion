from flask import Flask, request

app = Flask(__name__)

@app.route("/calc")
def calc():
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
        op = request.args.get("opción")
        
        if op == "suma":
            result = num1 + num2
        elif op == "resta":
            result = num1 - num2
        elif op == "multiplicación":
            result = num1 * num2
        elif op == "división":
            if num2 == 0:
                return "Error: División por cero"
            result = num1 / num2
        else:
            return "Operación no válida. Usa: suma, resta, multiplicación o división."

        return f"Resultado: {result}"
    
    except (TypeError, ValueError):
        return "Error: Parámetros inválidos. Asegúrate de pasar num1, num2 y opción."

if __name__ == "__main__":
    app.run(debug=True)
