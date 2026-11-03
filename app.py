from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Python Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #f4f4f9; }
        .calculator { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center; width: 300px; }
        input, select, button { margin: 10px 0; padding: 10px; width: 100%; border-radius: 5px; border: 1px solid #ccc; font-size: 16px; box-sizing: border-box; }
        button { background-color: #007bff; color: white; border: none; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .result { margin-top: 15px; font-weight: bold; font-size: 18px; color: #333; }
    </style>
</head>
<body>
    <div class="calculator">
        <h2>Web Calculator</h2>
        <form method="POST">
            <input type="number" step="any" name="num1" placeholder="First Number" required value="{{ num1 or '' }}">
            <select name="operation">
                <option value="add" {% if op == 'add' %}selected{% endif %}>+</option>
                <option value="subtract" {% if op == 'subtract' %}selected{% endif %}>-</option>
                <option value="multiply" {% if op == 'multiply' %}selected{% endif %}>*</option>
                <option value="divide" {% if op == 'divide' %}selected{% endif %}>/</option>
            </select>
            <input type="number" step="any" name="num2" placeholder="Second Number" required value="{{ num2 or '' }}">
            <button type="submit">Calculate</button>
        </form>
        {% if result is not none %}
            <div class="result">Result: {{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def calculate():
    result = None
    num1 = None
    num2 = None
    op = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            op = request.form['operation']
            if op == 'add':
                result = num1 + num2
            elif op == 'subtract':
                result = num1 - num2
            elif op == 'multiply':
                result = num1 * num2
            elif op == 'divide':
                result = num1 / num2 if num2 != 0 else 'Error: Division by zero'
        except ValueError:
            result = 'Invalid Input'
    return render_template_string(HTML_TEMPLATE, result=result, num1=num1, num2=num2, op=op)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
