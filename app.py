import datetime
from datetime import date
from flask import Flask

app = Flask(__name__)

@app.route('/')
today = datetime.datetime.now()
bday = datetime.datetime(2023,12,16,14,45)
time_diff = bday - today
print(f"Your birthday is in {time_diff}")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
