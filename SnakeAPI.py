from flask import Flask, request
from flask_cors import CORS
from SnakeGame import SnakeGame
import json

app = Flask(__name__)
CORS(app)
sg = SnakeGame()


@app.route("/", methods=['GET'])
def index():
    grid = sg.plot_snake(sg.grid, sg.head_val)
    return json.dumps(grid.tolist()), 200


@app.route("/<string:direction>", methods=['GET'])
def move(direction):
    if direction in ["up", "down", "left", "right"]:
        sg.move_snake(direction)
    elif direction == "reset":
        sg.reset_snake()
    grid = sg.plot_snake(sg.grid, sg.head_val)
    return json.dumps(grid.tolist()), 200


if __name__ == '__main__':
    app.run(debug=True)