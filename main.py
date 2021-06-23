from flask import Flask, request, abort
import calculator.calc_functions as calc_functions

def read_number(number_id):
    number = input(f"Please Enter an integer Number {number_id}: ")
    return int(number)


app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the calculator app"

@app.route('/add/<int:number1>/<int:number2>')
def perform_add(number1, number2):
    return str(calc_functions.add(number1, number2))

@app.route('/add')
def perform_add_query():
    number1 = request.args.get('num1', type=int)
    number2 = request.args.get('num2', type=int)

    if number1 is None or number2 is None:
        abort(401)

@app.route('/subtract/<int:number1>/<int:number2>')
def perform_subtract(number1, number2):
    return str(calc_functions.subtract(number1, number2))

@app.route('/subtract')
def perform_subtract_query():
    number1 = request.args.get('num1', type=int)
    number2 = request.args.get('num2', type=int)

    if number1 is None or number2 is None:
        abort(401)

    return str(calc_functions.subtract(number1, number2))


@app.route('/multiply/<int:number1>/<int:number2>')
def perform_multiply(number1, number2):
    return str(calc_functions.multiply(number1, number2))

@app.route('/multiply')
def perform_multiply_query():
    number1 = request.args.get('num1', type=int)
    number2 = request.args.get('num2', type=int)

    if number1 is None or number2 is None:
        abort(401)

    return str(calc_functions.multiply(number1, number2))

@app.route('/divide/<int:number1>/<int:number2>')
def perform_divide(number1, number2):
    return str(calc_functions.divide(number1, number2))

@app.route('/divide')
def perform_divide_query():
    number1 = request.args.get('num1', type=int)
    number2 = request.args.get('num2', type=int)

    if number1 is None or number2 is None:
        abort(401)

    return str(calc_functions.divide(number1, number2))

# if __name__ == "__main__":
    # number1 = read_number(1)
    # number2 = read_number(2)
    #
    # result = calc_functions.add(number1, number2)
    # print(result)
