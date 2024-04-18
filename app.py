from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            if operation == '+':
                result = num1 + num2
                result_str = f"{num1} + {num2} = {result}"
            elif operation == '-':
                result = num1 - num2
                result_str = f"{num1} - {num2} = {result}"
            elif operation == '*':
                result = num1 * num2
                result_str = f"{num1} * {num2} = {result}"
            elif operation == '/':
                result = num1 / num2
                result_str = f"{num1} / {num2} = {result}"
        except Exception as e:
            result_str = "Error: " + str(e)
    else:
        result_str = ""
    return render_template('index.html', result=result_str)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
