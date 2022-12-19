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
    return f'''
    <p>Сума н перших членів арифметичної прогресії: {result}
    '''
def sumsumOfAP(a, d, n):
    sum = (n / 2) * (5 * a + (n-2) * d)
    return sum 
if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0')


