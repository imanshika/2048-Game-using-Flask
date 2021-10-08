from flask import Flask, render_template
from werkzeug.utils import redirect
import logic
app = Flask(__name__)

grid = [[0 for i in range(4)] for j in range(4)]
status = 0
color = {0: "#bab76340", 2: "#ffeb3b1a", 4: "#ffeb3b66", 8: "#ff572273", 16: "#ff5722a8", 32: "#ff5722f2", 64: "#f44336bd", 128: "#f44336f5",
     256: "#8bc34a73", 512:"#8bc34aab", 1024: "#4caf50a1", 2048:"#4caf50e8"}


@app.route('/')
def index():
    if logic.isEmpty(grid):
        return redirect('/newGame')
    else:
        return render_template("index.html", grid = grid, color = color, status = status)

@app.route('/newGame')
def newGame():
    global grid
    global status
    grid = logic.start_game()
    status = 0
    return redirect('/')

@app.route('/left')
def left():
    new_grid, change = logic.move_left(grid)
    return check(new_grid, change)


@app.route('/right')
def right():
    new_grid, change = logic.move_right(grid)
    return check(new_grid, change)


@app.route('/up')
def up():
    new_grid, change = logic.move_up(grid)
    return check(new_grid, change)


@app.route('/down')
def down():
    new_grid, change = logic.move_down(grid)
    return check(new_grid, change)


def check(new_grid, change):
    global grid
    global status
    status = logic.get_current_state(new_grid)
    if change and status == 0:
        logic.add_new_2(new_grid)
    grid = new_grid
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=False)