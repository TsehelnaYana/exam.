from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    n = 3
    a1 = 2
    a2 = 5
    d = a2 - a1
    result = sumOfAP(a1, d, n)
    return f
    <p>
    <p>Сума н перших членів арифметичної прогресії: {result}

if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0')


