from flask import  Flask, request
from datetime import datetime
app = Flask(__name__)
last_events = [

]

class Posicao:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y
        }

class Event:
    def __init__(self, pos):
        self.pos = pos
        self.time = datetime.now()

    def to_dict(self):
        return {
            "pos": self.pos.to_dict(),
            "time": self.time
        }

@app.route('/sensor')
def get():
    return last_events

@app.route('/enter', methods=['POST'])
def enter():
    data = request.get_json()
    last_events.append(Event(Posicao(data['x'], data['y'])).to_dict())
    return "ok"

if __name__ == '__main__':
    app.run(debug=True)