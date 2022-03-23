from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def core(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof.lower())


@app.route('/list_prof/<rend>')
def list_prof(rend):
    prof_list = ['инженер-исследователь',
                 'пилот',
                 "строитель",
                 "экзобиолог",
                 "врач",
                 "инженер по терраформированию",
                 "климатолог",
                 "специалист по радиационной защите",
                 "астрогеолог",
                 "гляциолог",
                 "инженер жизнеобеспечения",
                 "метеоролог",
                 "оператор марсохода",
                 "киберинженер",
                 "штурман",
                 "пилот дронов"]
    return render_template('list_prof.html', prof_list=prof_list, rend=rend)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
