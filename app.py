from flask import Flask, abort, render_template, request, redirect, url_for
from entities.monster import Monster

app = Flask(__name__)


@app.route('/')
def index():
    monsters = Monster.get_all()
    return render_template('index.html', monsters=monsters)


@app.route('/monster', methods=['POST'])
def save_monster():
    monster = Monster(name=request.form['name'],
                      power=request.form['power'])
    monster.save()
    return redirect('/')


@app.route('/monster/<int:monster_id>/edit', methods=['GET', 'POST'])
def edit_monster(monster_id):
    monster = Monster.get_by_id(monster_id)
    if monster is None:
        abort(404)

    if request.method == 'POST':
        updated_monster = Monster(
            name=request.form['name'].strip(),
            power=request.form['power'].strip(),
            id=monster_id
        )
        updated_monster.update()
        return redirect(url_for('index'))

    return render_template('edit_monster.html', monster=monster)


if __name__ == '__main__':
    app.run(debug=True)
