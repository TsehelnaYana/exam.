import heapq
from flask import Flask

app = Flask(__name__)

lombard = []
#number = 0
#item_name = ''


@app.route('/')
def add_to_lombard():
    heapq.heappush(lombard, (1, "phone"))
    heapq.heappush(lombard, (2, "earrings"))
    heapq.heappush(lombard, (3, "necklace"))
    heapq.heappush(lombard, (4, "TV"))	
    return lombard
    
def print_lombard(b):
    while b:
        print(heapq.heappop(b))

add_to_lombard()
print_lombard(lombard)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
